from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from hospital.models import Doctor, Patient, Appointment, PatientDischargeDetails
import datetime

class HospitalViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_public_views(self):
        routes = ['/', '/aboutus', '/contactus', '/adminclick', '/doctorclick', '/patientclick', '/adminlogin', '/doctorlogin', '/patientlogin']
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, f"Route {route} failed with status {response.status_code}")

    def test_signup_views_get(self):
        routes = ['/adminsignup', '/doctorsignup', '/patientsignup']
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, f"Signup GET {route} failed")

class HospitalAuthenticatedViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Admin setup
        self.admin_group, _ = Group.objects.get_or_create(name='ADMIN')
        self.admin_user = User.objects.create_user(username='adminuser', password='password123', first_name='Admin', last_name='User')
        self.admin_user.groups.add(self.admin_group)
        
        # Doctor setup
        self.doctor_group, _ = Group.objects.get_or_create(name='DOCTOR')
        self.doctor_user = User.objects.create_user(username='doctoruser', password='password123', first_name='DrJohn', last_name='Doe')
        self.doctor_user.groups.add(self.doctor_group)
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            address='123 Medical Way',
            mobile='9876543210',
            department='Cardiologist',
            status=True
        )

        # Patient setup
        self.patient_group, _ = Group.objects.get_or_create(name='PATIENT')
        self.patient_user = User.objects.create_user(username='patientuser', password='password123', first_name='Jane', last_name='Smith')
        self.patient_user.groups.add(self.patient_group)
        self.patient = Patient.objects.create(
            user=self.patient_user,
            address='456 Health Ave',
            mobile='1234567890',
            symptoms='Fever and Cold',
            assignedDoctorId=self.doctor_user.id,
            status=True
        )

    def test_admin_dashboard(self):
        self.client.login(username='adminuser', password='password123')
        response = self.client.get('/admin-dashboard')
        self.assertEqual(response.status_code, 200)

    def test_doctor_dashboard(self):
        self.client.login(username='doctoruser', password='password123')
        response = self.client.get('/doctor-dashboard')
        self.assertEqual(response.status_code, 200)

    def test_doctor_search_view(self):
        self.client.login(username='doctoruser', password='password123')
        response = self.client.get('/search?query=Fever')
        self.assertEqual(response.status_code, 200)

    def test_patient_dashboard(self):
        self.client.login(username='patientuser', password='password123')
        response = self.client.get('/patient-dashboard')
        self.assertEqual(response.status_code, 200)

    def test_patient_view_doctor(self):
        self.client.login(username='patientuser', password='password123')
        response = self.client.get('/patient-view-doctor')
        self.assertEqual(response.status_code, 200)

    def test_patient_search_doctor(self):
        self.client.login(username='patientuser', password='password123')
        response = self.client.get('/searchdoctor?query=Cardiologist')
        self.assertEqual(response.status_code, 200)

    def test_download_pdf_view_missing(self):
        # Requesting discharge bill PDF for non-discharged patient should return 404
        self.client.login(username='adminuser', password='password123')
        response = self.client.get(f'/download-pdf/{self.patient.id}')
        self.assertEqual(response.status_code, 404)

class HospitalModelTests(TestCase):
    def setUp(self):
        self.user_doc = User.objects.create_user(username='doc1', first_name='John', last_name='Doe')
        self.doctor = Doctor.objects.create(
            user=self.user_doc,
            address='123 Hospital St',
            mobile='1234567890',
            department='Cardiologist',
            status=True
        )
        self.user_pat = User.objects.create_user(username='pat1', first_name='Jane', last_name='Smith')
        self.patient = Patient.objects.create(
            user=self.user_pat,
            address='456 Patient Rd',
            mobile='0987654321',
            symptoms='Fever',
            assignedDoctorId=self.user_doc.id,
            status=True
        )

    def test_doctor_str_and_properties(self):
        self.assertEqual(str(self.doctor), 'John (Cardiologist)')
        self.assertEqual(self.doctor.get_name, 'John Doe')
        self.assertEqual(self.doctor.get_id, self.user_doc.id)

    def test_patient_str_and_properties(self):
        self.assertEqual(str(self.patient), 'Jane (Fever)')
        self.assertEqual(self.patient.get_name, 'Jane Smith')
        self.assertEqual(self.patient.get_id, self.user_pat.id)
