from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from hospital.models import Doctor, Patient, Appointment, PatientDischargeDetails, departments

class HospitalViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_view(self):
        response = self.client.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_contactus_view(self):
        response = self.client.get('/contactus')
        self.assertEqual(response.status_code, 200)

    def test_adminclick_view(self):
        response = self.client.get('/adminclick')
        self.assertEqual(response.status_code, 200)

    def test_doctorclick_view(self):
        response = self.client.get('/doctorclick')
        self.assertEqual(response.status_code, 200)

    def test_patientclick_view(self):
        response = self.client.get('/patientclick')
        self.assertEqual(response.status_code, 200)

    def test_adminlogin_view(self):
        response = self.client.get('/adminlogin')
        self.assertEqual(response.status_code, 200)

    def test_doctorlogin_view(self):
        response = self.client.get('/doctorlogin')
        self.assertEqual(response.status_code, 200)

    def test_patientlogin_view(self):
        response = self.client.get('/patientlogin')
        self.assertEqual(response.status_code, 200)

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
