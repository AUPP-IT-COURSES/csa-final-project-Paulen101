# final_project_test.py

from datetime import datetime

class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.appointments = []

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.appointments = []

class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def get_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def schedule_appointment(self, patient_id, doctor_id, date_time):
        patient = self.get_patient_by_id(patient_id)
        doctor = self.get_doctor_by_id(doctor_id)

        if not patient or not doctor:
            return None

        # Convert the date_time string to a datetime object
        date_time_obj = datetime.strptime(date_time, "%Y-%m-%d %I:%M %p")

        # Check for overlapping appointments
        if any(
            appt.date_time == date_time_obj
            for appt in self.appointments
        ):
            return None  # Return None if the appointment already exists

        appointment = Appointment(patient, doctor, date_time_obj)
        self.appointments.append(appointment)
        patient.appointments.append(appointment)
        doctor.appointments.append(appointment)

        return appointment

    def register_doctor(self, doctor_id, name, specialization):
        doctor = Doctor(doctor_id, name, specialization)
        self.add_doctor(doctor)
        return doctor

    def get_all_appointments(self):
        appointments = []
        for patient in self.patients.values():
            for appointment in patient.appointments:
                appointments.append(appointment)
        return appointments

