import tkinter as tk
from tkinter import ttk, messagebox
from hospital_system import HospitalSystem, Patient, Doctor

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital System")

        self.hospital_system = HospitalSystem()

        style = ttk.Style()
        style.theme_use('default')

        frame = ttk.Frame(root, padding=(20, 20, 20, 20))
        frame.grid(row=0, column=0, sticky="nsew")

        # Patient Entry
        ttk.Label(frame, text="Patient Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.patient_name_entry = ttk.Entry(frame)
        self.patient_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Patient Age:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.patient_age_entry = ttk.Entry(frame)
        self.patient_age_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Patient Condition:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.patient_condition_entry = ttk.Entry(frame)
        self.patient_condition_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Doctor Entry
        ttk.Label(frame, text="Doctor Name:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.doctor_name_entry = ttk.Entry(frame)
        self.doctor_name_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Doctor Specialization:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.specialization_entry = ttk.Entry(frame)
        self.specialization_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # Buttons
        ttk.Button(frame, text="Add Patient", command=self.add_patient).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="Add Doctor", command=self.add_doctor).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="Check In", command=self.check_in_patient).grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="View Records", command=self.view_records).grid(row=8, column=0, columnspan=2, pady=10, sticky="ew")

        # Center the content within the frame
        for i in range(9):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Make the entire window resizable
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def add_patient(self):
        name = self.patient_name_entry.get()
        age = int(self.patient_age_entry.get())
        condition = self.patient_condition_entry.get()

        patient = Patient(name, age, condition)
        self.hospital_system.add_patient(patient)
        messagebox.showinfo("Success", f"Patient {name} added successfully!")

    def add_doctor(self):
        name = self.doctor_name_entry.get()
        specialization = self.specialization_entry.get()

        doctor = Doctor(name, specialization)
        self.hospital_system.add_doctor(doctor)
        messagebox.showinfo("Success", f"Doctor {name} added successfully!")

    def check_in_patient(self):
        patient_name = self.patient_name_entry.get()
        result = self.hospital_system.check_in_patient(patient_name)
        messagebox.showinfo("Check In", result)

    def view_records(self):
        patient_records = self.hospital_system.view_patients_record()
        doctor_records = self.hospital_system.view_doctors_record()

        records_text = "\nPatient Records:\n"
        records_text += "\n".join(patient_records)

        records_text += "\n\nDoctor Records:\n"
        records_text += "\n".join(doctor_records)

        messagebox.showinfo("Records", records_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
