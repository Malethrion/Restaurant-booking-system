# Restaurant Booking System

**Restaurant Booking System** is a web application designed to streamline restaurant reservation processes and menu management. This project provides a user-friendly platform for diners to book tables and for restaurant administrators to manage reservations and menus efficiently. It leverages Django’s MVC framework, secure authentication, and responsive design to meet real-world restaurant needs.

Explore the live application at: [Deployed Site](https://restaurant-booking-system123-2102e902d1fa.herokuapp.com/).

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
   - [User Features](#user-features)
   - [Admin Features](#admin-features)
3. [Design Process](#design-process)
   - [Wireframes and Mockups](#wireframes-and-mockups)
   - [Design Reasoning](#design-reasoning)
4. [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Python Libraries](#python-libraries)
   - [Other Technologies](#other-technologies)
5. [Testing](#testing)
   - [Manual Testing](#manual-testing)
   - [Automated Testing](#automated-testing)
   - [Lighthouse](#lighthouse)
   - [Code Validation](#code-validation)
   - [Browser and Device Testing](#browser-and-device-testing)
6. [Known Issues](#known-issues)
7. [Agile Methodology](#agile-methodology)
   - [User Stories, Epics, and Prioritization](#user-stories-epics-and-prioritization)
   - [User Acceptance Criteria](#user-acceptance-criteria)
8. [Data Model](#data-model)
   - [Schema and Relationships](#schema-and-relationships)
9. [Security and Data Features](#security-and-data-features)
10. [Deployment](#deployment)
    - [Pre-Deployment Checklist](#pre-deployment-checklist)
    - [Deploying on Heroku](#deploying-on-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
    - [Running Locally](#running-locally)
11. [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
12. [References](#references)
13. [Credits](#credits)
14. [Acknowledgements](#acknowledgements)

---

## Project Overview

The **Restaurant Booking System** aims to enhance restaurant operations by providing a secure, intuitive platform for table reservations and menu management. It addresses real-world needs for diners to book tables easily and for administrators to manage bookings efficiently, using Django’s robust authentication, CRUD operations, and responsive Bootstrap styling.

---

## Features

### User Features
- **Account Registration and Login**: Users can register and log in securely using Django’s `UserCreationForm`, with authentication status displayed in the navbar.
  - **Register**: Users fill out a form to create an account, receiving success/error messages.
  - **Login/Logout**: Users can log in/out, with appropriate redirects and feedback.
- **Reservation Management**: Users can create, view, update, and delete reservations, with form validation and user-specific access.
  - **Create Reservation**: Fill out a form with customer name, date, time, guests, and email.
  - **View Reservations**: See a list of current reservations with edit/delete options.
  - **Update Reservation**: Modify existing bookings with pre-filled forms.
  - **Delete Reservation**: Remove bookings with confirmation.

### Admin Features
- **Reservation Management**: Administrators (logged-in users) can manage all reservations via CRUD operations, with secure access control.

---

## Design Process

### Wireframes and Mockups
*Include visual representations of the design process here. Provide images of wireframes or mockups for each page (e.g., Home, Reservations, Menu). Save these as `static/img/wireframe_home.png`, `static/img/mockup_reservations.png`, etc., and link them below:*
- **Home Page Wireframe**: ![Home Wireframe](static/img/wireframe_home.png) "Wireframe showing the hero section and navigation."
- **Reservations Page Mockup**: ![Reservations Mockup](static/img/mockup_reservations.png) "Mockup of the reservation list and form."
- **Menu Page Wireframe**: ![Menu Wireframe](static/img/wireframe_menu.png) "Wireframe showing menu categories and images."

### Design Reasoning
The design prioritizes user experience (UX) with a clean, responsive layout using Bootstrap 5 and custom CSS. Key decisions include:
- **Navigation**: A navbar with clear links for Reservations, Menu, Login/Register/Logout, ensuring accessibility.
- **Forms**: Intuitive reservation forms with date/time pickers and validation, styled for readability.
- **Responsiveness**: Media queries ensure compatibility across devices (mobile, tablet, desktop), adhering to UX principles.

---

## Technologies Used

### Languages Used
- **HTML5**: For structuring web pages.
- **CSS3**: For styling with Bootstrap and custom styles.
- **JavaScript**: For dynamic interactions (via Bootstrap).
- **Python**: For backend logic with Django.

### Python Libraries
- [Django](https://www.djangoproject.com/) - MVC framework for web development.
- [Gunicorn](https://gunicorn.org/) - WSGI server for deployment.
- [Psycopg2](https://www.psycopg.org/) - PostgreSQL adapter for database operations.
- [Whitenoise](https://whitenoise.evans.io/) - Static file serving for production.

### Other Technologies
- [Git](https://git-scm.com/) - Version control system.
- [Heroku](https://www.heroku.com/) - Cloud platform for deployment (updated below for current use).
- [Bootstrap 5](https://getbootstrap.com/) - Responsive CSS framework.

---

## Testing

### Manual Testing
| Feature                  | Action                          | Expected Result                                      | Actual Result                                      |
|--------------------------|---------------------------------|-----------------------------------------------------|---------------------------------------------------|
| Home Page                | View landing page               | Displays hero section, navigation, and reservation call-to-action | Functions as intended                              |
| Registration             | Register a new user             | Creates account, logs in, shows success message     | Functions as intended                              |
| Login/Logout             | Log in/out with credentials     | Logs in/out, updates navbar, shows feedback         | Functions as intended                              |
| Create Reservation       | Fill and submit reservation form | Creates reservation, redirects to list, shows success | Functions as intended                              |
| View Reservations        | View user reservations          | Lists all reservations with edit/delete options     | Functions as intended                              |
| Update Reservation       | Edit an existing reservation    | Updates reservation, shows success, redirects       | Functions as intended                              |
| Delete Reservation       | Delete a reservation            | Removes reservation, shows success, redirects       | Functions as intended                              |
| Menu Page                | View menu items                 | Displays menu categories with images and prices     | Functions as intended                              |


#### Screenshots and Evidence
- **Home Page**: 

![Home Page](static/img/homepage.png) 

"Screenshot of the landing page with hero section."

- **Registration**: 

![Register](static/img/register_main.png) 

"Screenshot of the registration button." 

![Register Form](static/img/registration2.png) 

"Screenshot of a filled registration form."

- **Login**:

![Login](static/img/login2.png) 

"Screenshot of the login form."

- **Logout**:

![Logout](static/img/logout.png) 

"Screenshot of the logout action in the navbar."

- **Reservations**: 

![Reservations](static/img/reservations2.png) 

"Screenshot of the reservation list." 

![Create Reservation](static/img/create_reservation.png) 

"Screenshot of the reservation form." 

![Current Reservations](static/img/current_reservations.png) 

"Screenshot of listed reservations." 

![Deleted Reservations](static/img/deleted_reservations.png) 

"Screenshot of a deleted reservation confirmation."

- **Menu**: 

![Menu](static/img/menu.png) 

"Screenshot of the menu page."

### Automated Testing
| Test Case                | Method                          | Expected Result                                      | Actual Result                                      |
|--------------------------|---------------------------------|-----------------------------------------------------|---------------------------------------------------|
| Test Reservation Model   | `test_reservation_model`        | Validates `Reservation` model fields (e.g., `customer_name`, `date`) | Functions as intended                              |
| Test Reservation CRUD    | `test_reservation_crud`         | Ensures create, read, update, delete operations work | Functions as intended                              |
| Test User Authentication | `test_user_auth`                | Verifies registration, login, logout functionality  | Functions as intended                              |
| *Expand automated tests in `tests.py` to cover forms, views, and edge cases (e.g., invalid dates, negative guests). Document results here.* |

### Lighthouse
- Audits performed using Google Lighthouse to ensure high performance, accessibility, and SEO scores.

- **Screenshots**: ![Lighthouse Report](static/img/lighthouse_report.png) 

"Screenshot of Lighthouse scores for performance, accessibility, SEO."

### Code Validation
- **HTML Validation**: Verified using W3C HTML Validator, passing without errors. 

![HTML Validation](static/img/html_validation.png) 

"Screenshot of W3C HTML validation results."

- **CSS Validation**: Verified using W3C CSS Validator, passing without errors. 

![CSS Validation](static/img/css_validation.png) 

"Screenshot of W3C CSS validation results."

- **Python Validation**: Confirmed adherence to PEP8 standards using `flake8` or similar tools, resolving minor issues (e.g., line length, blank lines). 

![Python Validation](static/img/python_validation.png) 

"Screenshot of Python validation results."

### Browser and Device Testing
- Tested on Chrome, Firefox, Edge (desktop), and Safari (mobile) using BrowserStack or local testing.

- **Screenshots**: ![Browser Testing](static/img/browsers.png) 

"Screenshot of browser compatibility across Chrome, Firefox, Edge."

- Ensured responsiveness on mobile, tablet, and desktop devices (e.g., iPhone, iPad, 13” laptop).

---

## Known Issues
No known issues at this time.
*If you discover bugs (e.g., validation errors, performance issues), list them here with details (e.g., “Reservation form accepts past dates”). Update after final testing.*

---

## Agile Methodology

### User Stories, Epics, and Prioritization
*Include a screenshot or description of your GitHub Projects/Kanban board showing user stories mapped to epics, prioritized, and segmented into sprints. Save as `static/img/kanban_board.png` and link below:*
- **Kanban Board**: ![Kanban Board](static/img/kanban_board.png) "Screenshot of GitHub Projects showing user stories, epics, and sprints."

### User Acceptance Criteria
- **User Story 1 (Register)**: “As a user, I can register an account to access reservation features.”
  - Acceptance Criteria: Form validates username (unique, 150 chars max), passwords match, shows success/error messages, redirects to login.
- **User Story 2 (Create Reservation)**: “As a user, I can book a table with details (name, date, time, guests, email).”
  - Acceptance Criteria: Form validates date (future only), time (restaurant hours), guests (positive integers), email, creates reservation, shows feedback.
- **User Story 3 (View Reservations)**: “As a user, I can view my reservations.”
  - Acceptance Criteria: Lists all user reservations, shows edit/delete options, handles empty lists.

---

## Data Model

### Schema and Relationships
- **Reservation Model**: Stores booking details (`customer_name`, `date`, `time`, `guests`, `contact_email`, linked to `User` via `ForeignKey`).
  - **Diagram**: ![Data Model](static/img/data_model.png) "Diagram showing `Reservation` and `User` relationships."
- **User Model**: Uses Django’s default `User` model for authentication, linked to `Reservation` for ownership.

---

## Security and Data Features
- **Authentication**: Uses Django’s `auth` system for secure user registration, login, logout, with navigation updates.
- **Authorization**: `@login_required` decorator restricts reservation CRUD to authenticated users.
- **Data Storage**: Uses PostgreSQL via `psycopg2` and `dj-database-url`, with `DATABASE_URL` hidden in `.env`.
- **CRUD Operations**: Securely manages reservations with form validation, ensuring data integrity.
- **Environment Variables**: `SECRET_KEY`, `DATABASE_URL`, `EMAIL_*` stored in `.env`, excluded from Git via `.gitignore`.



## Deployment

### Pre-Deployment Checklist
1. Update `requirements.txt` using `pip freeze > requirements.txt`.
2. Add a `Procfile` with `web: gunicorn restaurant_booking_system.wsgi:application`.
3. Configure environment variables in `.env`:
   - `SECRET_KEY`
   - `DATABASE_URL` (PostgreSQL on Heroku)
   - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` (optional for email)
4. Ensure `DEBUG = False` in `settings.py` for production.

### Deploying on Heroku
1. Create a Heroku account and install the Heroku CLI.
2. Log in to Heroku:
   ```bash
   heroku login
3. Create a new Heroku app:
   ```bash
   heroku create restaurant-booking-system
4. Set environment variables in Heroku:
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DATABASE_URL="your-postgres-url"
   heroku config:set EMAIL_HOST_USER="your-email"
   heroku config:set EMAIL_HOST_PASSWORD="your-password"
5. Deploy the app:
   ```bash
   git push heroku main
6. Test live functionality at [Deployed Site](https://restaurant-booking-system123-2102e902d1fa.herokuapp.com/).

---

## Forking the Repository
1. Navigate to [GitHub repository](https://github.com/Malethrion/Restaurant-booking-system).
2. Click the Fork button in the top-right corner to create a copy in your GitHub account.

## Cloning the Repository
1. Click the Code button on the repository page and copy the HTTPS URL.
2. In your terminal, clone the repository:
   ```bash
   git clone https://github.com/Malethrion/Restaurant-booking-system.git
3. Navigate to the project directory:
   ```bash
   cd Restaurant-booking-system

## Running Locally

1. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\activate  # Windows
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Apply migrations:
   ```bash
   python manage.py migrate
4. Run the development server:
   ```bash
   python manage.py runserver
5. Access the app at http://127.0.0.1:8000/.

---

## Deployment Evidence
- Heroku Dashboard:

![Heroku Dashboard](static/img/HerokuDashboard.png)

"Screenshot of Heroku deployment dashboard."

- Heroku Logs:

![Heroku Logs](static/img/HerokuLogs.png)

"Screenshot of Heroku deployment logs."
## Bugs

### Fixed Bugs:
1. Resolved issues with placeholder text not displaying on forms.
2. Corrected improper `aria-label` assignments for accessibility compliance.
3. Fixed a bug preventing static files from loading in production.

## Unfixed Bugs
- No unfixed bugs at this time.

---

## References

- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Bootstrap Documentation**: [https://getbootstrap.com/](https://getbootstrap.com/)
- **Stack Overflow**: Adapted logic for form handling and error validation.

---

## Credits

- Inspiration from real-world restaurant reservation systems (e.g., OpenTable, Resy).

### Media:
- Images sourced from [Unsplash](https://unsplash.com).

### Code:
- UI styling was implemented using [Bootstrap](https://getbootstrap.com).
- Form handling and validation adapted from [Django's official documentation](https://docs.djangoproject.com/en/5.1/).

---

## Acknowledgements

- Thanks to Rory Patrick for guidance and feedback throughout the project.
- Appreciation to Code Institute for providing the learning platform and resources.
- Gratitude to the Django, Bootstrap, and Heroku communities for documentation and support.

---

This README provides a structured overview of the **Restaurant Booking System**, ensuring clarity and accessibility for collaborators and end-users.

