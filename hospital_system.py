class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition

    def checkin(self):
        self.checkin = True

    def update_information(self, age=None, condition=None):
        if age:
            self.age = age
        if condition:
            self.condition = condition
    def display_information(self):
        return f"Name: {self.name}, Age: {self.age}, Condition: {self.condition}"

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)

    def view_patients(self):
        return [patient.name for patient in self.patients]

    def display_information(self):
        patient_list = ', '.join(self.view_patients())
        return f"Name: {self.name}, Specialization: {self.specialization}, Patients: {patient_list}"

class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def find_patient(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                return patient
        return None
    
    def checkin_patient(self, patient_name):
        patient = self.find_patient(patient_name)
        if patient:
            patient.checkin()
            return f"{patient.name} has been checked in."
        return f"{patient_name} not found."
    
    def view_patients_record(self):
        return [patient.display_information() for patient in self.patients]
    
    def view_doctors_record(self):
        return [doctor.display_information() for doctor in self.doctors]
