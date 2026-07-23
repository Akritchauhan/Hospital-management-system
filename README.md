# Hospital Management System
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Akrit%20Chauhan-blue)
---

## Screenshots

### Homepage
![homepage snap](https://raw.githubusercontent.com/Akritchauhan/Hospital-management-system/main/static/screenshots/homepage.png)

### Admin Dashboard
![dashboard snap](https://raw.githubusercontent.com/Akritchauhan/Hospital-management-system/main/static/screenshots/admin_dashboard.png)

### Invoice
![invoice snap](https://raw.githubusercontent.com/Akritchauhan/Hospital-management-system/main/static/screenshots/invoice.png)

### Doctor List
![doctor snap](https://raw.githubusercontent.com/Akritchauhan/Hospital-management-system/main/static/screenshots/admin_doctor.png)

---

## Features & Roles

### Admin Module
- **Account Creation**: Signup & immediate access (no external approval required).
- **Doctor Management**: Register, view, approve, reject, and remove doctors (approval workflow for applicant doctors).
- **Patient Management**: Admit, view, approve, reject, and discharge patients (with date tracking & fee calculation).
- **Invoice Generation**: Generate & download PDF invoices detailing room charges, doctor fees, medicine costs, and misc expenses.
- **Appointment Management**: View, create, and approve patient-requested appointment slots.

### Doctor Module
- **Application & Approval**: Apply for a hospital role; access granted upon Admin approval.
- **Patient Tracking**: View assigned active patient profiles (symptoms, contact info, admit status).
- **Discharged Records**: Review history of discharged patients assigned to the doctor.
- **Appointment Schedule**: View and manage confirmed patient appointments.

### Patient Module
- **Hospital Registration**: Create an account for admission; access granted upon Admin approval.
- **Doctor Details**: View assigned doctor details (specialization, department, contact information).
- **Appointment Booking**: Request appointment slots with doctors (requires Admin confirmation).
- **Billing & Discharge**: View and download final PDF invoice upon discharge.

---

## How to Run This Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Akritchauhan/Hospital-management-system.git
   cd Hospital-management-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run Automated Tests**:
   ```bash
   python manage.py test
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the web app at `http://127.0.0.1:8000/`.

---

## Configuration

### Contact Us Email Setup
To enable email notifications on the contact page, configure the following settings in `hospitalmanagement/settings.py`:
```python
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
EMAIL_RECEIVING_USER = ['destination_email@gmail.com']
```

---

## Repository & Maintainer

- **Repository**: [https://github.com/Akritchauhan/Hospital-management-system](https://github.com/Akritchauhan/Hospital-management-system)
- **Maintainer**: Akrit Chauhan
