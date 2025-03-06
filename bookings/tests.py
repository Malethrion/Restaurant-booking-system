from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm
from datetime import date, time

class ReservationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_reservation_model(self):
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
            'contact_email': 'test@invalid.com'  # Invalid email
        })
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)
        self.assertIn('contact_email', form.errors)

    def test_reservation_list_view(self):
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
        self.client.logout()
        response = self.client.get('/reservations/new/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, '/login/?next=/reservations/new/')