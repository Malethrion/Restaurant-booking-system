from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm
from datetime import date, time


class ReservationTests(TestCase):
    def setUp(self):
        """Set up a test client and user for all test cases."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_reservation_model(self):
        """Test that the Reservation model creates and retrieves data correctly."""
        reservation = Reservation.objects.create(
            customer_name='Test User',
            date=date.today(),
            time=time(18, 0),
            guests=4,
            contact_email='test@gmail.com',
            user=self.user
        )
        self.assertEqual(reservation.customer_name, 'Test User')
        self.assertEqual(reservation.guests, 4)

    def test_reservation_create_view(self):
        """Test the create reservation view renders and processes form submissions."""
        response = self.client.get('/reservations/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_reservation.html')

        response = self.client.post('/reservations/new/', {
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'test@gmail.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(Reservation.objects.filter(customer_name='Test User').exists())

    def test_reservation_form_validation(self):
        """Test the ReservationForm validation for valid and invalid inputs."""
        # Test valid form submission
        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'test@gmail.com'
        })
        self.assertTrue(form.is_valid())

        # Test invalid cases
        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date(2023, 1, 1),  # Past date
            'time': '18:00',
            'guests': 4,
            'contact_email': 'test@gmail.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': -1,  # Negative guests
            'contact_email': 'test@gmail.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors)

        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '09:00',  # Outside hours
            'guests': 4,
            'contact_email': 'test@gmail.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)

        # Test invalid email formats
        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'not_an_email'  # No @ symbol
        })
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors)
        self.assertEqual(form.errors['contact_email'], ['Enter a valid email address (e.g., user@example.com).'])

        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'user@'  # Incomplete domain
        })
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors)

        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'user@domain'  # Missing top-level domain
        })
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors)

        # Test valid email with non-Gmail/Yahoo domain
        form = ReservationForm(data={
            'customer_name': 'Test User',
            'date': date.today().isoformat(),
            'time': '18:00',
            'guests': 4,
            'contact_email': 'jin.norden@hotmail.com'  # Valid email, previously rejected
        })
        self.assertTrue(form.is_valid())

    def test_reservation_list_view(self):
        """Test the reservation list view displays user reservations correctly."""
        Reservation.objects.create(
            customer_name='Test User',
            date=date.today(),
            time=time(18, 0),
            guests=4,
            contact_email='test@gmail.com',
            user=self.user
        )
        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/list_reservations.html')
        self.assertContains(response, 'Test User')

    def test_unauthenticated_access(self):
        """Test that unauthenticated users are redirected to the login page."""
        self.client.logout()
        response = self.client.get('/reservations/new/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, '/login/?next=/reservations/new/')