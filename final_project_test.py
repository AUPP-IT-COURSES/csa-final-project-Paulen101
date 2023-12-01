import datetime

class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.appointments = []

    def schedule_appointment(self, doctor, date_time):
        appointment = Appointment(self, doctor, date_time)
        self.appointments.append(appointment)
        doctor.add_appointment(appointment)
        return appointment

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def register_doctor(self, doctor_id, name, specialization):
        doctor = Doctor(doctor_id, name, specialization)
        self.add_doctor(doctor)
        return doctor

    def schedule_appointment(self, patient_id, doctor_id, date_time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)

        if patient and doctor:
            return patient.schedule_appointment(doctor, date_time)
        else:
            return None
    
    def get_all_appointments(self):
        appointments = []
        for patient in self.patients:
            for appointment in patient.appointments:
                appointments.append(appointment)
        return appointments
