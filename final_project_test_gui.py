import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from final_project_test import Patient, Doctor, HospitalSystem, Appointment

class HospitalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital System")

        # Define a style for buttons
        self.button_style = ttk.Style()
        self.button_style.configure('TButton', font=('Sans Serif', 12), padding=5)

        # Define a style for labels
        self.label_style = ttk.Style()
        self.label_style.configure('TLabel', font=('Sans Serif', 12), padding=5)

        # Define a style for entry widgets
        self.entry_style = ttk.Style()
        self.entry_style.configure('TEntry', font=('Sans', 12), padding=5)

        # Create a separator line
        ttk.Separator(self.master, orient='horizontal').pack(fill='x', pady=10)

        self.hospital_system = HospitalSystem()

        self.create_widgets()

    def create_widgets(self):
        # Create main menu frame
        main_menu_frame = tk.Frame(self.master)
        main_menu_frame.pack(pady=20)

        ttk.Button(main_menu_frame, text="Patient Registration", command=self.show_patient_registration).grid(row=0, column=0, padx=10)
        ttk.Button(main_menu_frame, text="Doctor Registration", command=self.show_doctor_registration).grid(row=0, column=1, padx=10)
        ttk.Button(main_menu_frame, text="Appointment Scheduling", command=self.show_appointment_scheduling).grid(row=0, column=2, padx=10)
        ttk.Button(main_menu_frame, text="View All Appointments", command=self.show_all_appointments).grid(row=0, column=3, padx=10)

        # Create patient registration frame
        self.patient_frame = tk.Frame(self.master)

        ttk.Label(self.patient_frame, text="Patient ID:").grid(row=0, column=0)
        ttk.Label(self.patient_frame, text="Name:").grid(row=1, column=0)
        ttk.Label(self.patient_frame, text="Age:").grid(row=2, column=0)
        ttk.Label(self.patient_frame, text="Gender:").grid(row=3, column=0)

        self.patient_id_entry = ttk.Entry(self.patient_frame)
        self.patient_id_entry.grid(row=0, column=1)
        self.name_entry = ttk.Entry(self.patient_frame)
        self.name_entry.grid(row=1, column=1)
        self.age_entry = ttk.Entry(self.patient_frame)
        self.age_entry.grid(row=2, column=1)
        self.gender_entry = ttk.Entry(self.patient_frame)
        self.gender_entry.grid(row=3, column=1)

        ttk.Button(self.patient_frame, text="Register Patient", command=self.register_patient).grid(row=4, column=0, columnspan=2, pady=10)

        # Create doctor registration frame
        self.doctor_frame = tk.Frame(self.master)

        ttk.Label(self.doctor_frame, text="Doctor ID:").grid(row=0, column=0)
        ttk.Label(self.doctor_frame, text="Name:").grid(row=1, column=0)
        ttk.Label(self.doctor_frame, text="Specialization:").grid(row=2, column=0)

        self.doctor_id_entry = ttk.Entry(self.doctor_frame)
        self.doctor_id_entry.grid(row=0, column=1)
        self.doctor_name_entry = ttk.Entry(self.doctor_frame)
        self.doctor_name_entry.grid(row=1, column=1)
        self.specialization_entry = ttk.Entry(self.doctor_frame)
        self.specialization_entry.grid(row=2, column=1)

        ttk.Button(self.doctor_frame, text="Register Doctor", command=self.register_doctor).grid(row=3, column=0, columnspan=2, pady=10)

        # Create appointment scheduling frame
        self.appointment_frame = tk.Frame(self.master)

        ttk.Label(self.appointment_frame, text="Patient ID:").grid(row=0, column=0)
        ttk.Label(self.appointment_frame, text="Doctor ID:").grid(row=1, column=0)
        ttk.Label(self.appointment_frame, text="Date:").grid(row=2, column=0)
        ttk.Label(self.appointment_frame, text="Time:").grid(row=3, column=0)

        self.patient_id_app_entry = ttk.Entry(self.appointment_frame)
        self.patient_id_app_entry.grid(row=0, column=1)
        self.doctor_id_app_entry = ttk.Entry(self.appointment_frame)
        self.doctor_id_app_entry.grid(row=1, column=1)

        # Use DateEntry for date selection
        self.date_picker = DateEntry(self.appointment_frame, width=12, background='darkblue',
                                     foreground='white', borderwidth=2)
        self.date_picker.grid(row=2, column=1, pady=10)

        # Use Combobox for time selection
        self.time_combobox = ttk.Combobox(self.appointment_frame, values=["09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM",
                                                                         "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM",
                                                                         "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM",
                                                                         "03:00 PM", "03:30 PM", "04:00 PM", "04:30 PM"])
        self.time_combobox.grid(row=3, column=1, pady=10)

        ttk.Button(self.appointment_frame, text="Schedule Appointment", command=self.schedule_appointment).grid(row=4, column=0, columnspan=2, pady=10)

        # Create view all appointments frame
        self.view_appointments_frame = tk.Frame(self.master)

        self.appointments_listbox = tk.Listbox(self.view_appointments_frame, width=50, font=('Arial', 12))
        self.appointments_listbox.pack(pady=10)
        ttk.Button(self.view_appointments_frame, text="Refresh Appointments", command=self.refresh_appointments).pack(pady=10)
        ttk.Button(self.view_appointments_frame, text="Clear Appointments", command=self.clear_appointments).pack(pady=10)

    def show_patient_registration(self):
        self.hide_frames()
        self.patient_frame.pack(pady=20)

    def show_doctor_registration(self):
        self.hide_frames()
        self.doctor_frame.pack(pady=20)

    def show_appointment_scheduling(self):
        self.hide_frames()
        self.appointment_frame.pack(pady=20)

    def show_all_appointments(self):
        self.hide_frames()
        self.refresh_appointments()
        self.view_appointments_frame.pack(pady=20)

    def hide_frames(self):
        self.patient_frame.pack_forget()
        self.doctor_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.view_appointments_frame.pack_forget()

    def refresh_appointments(self):
        self.appointments_listbox.delete(0, tk.END)
        appointments = self.hospital_system.get_all_appointments()
        for appointment in appointments:
            self.appointments_listbox.insert(tk.END, f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date and Time: {appointment.date_time}")

    def clear_appointments(self):
        patient_id = self.patient_id_entry.get()  # Get patient ID from entry (you may need to modify this based on your structure)
        patient = self.hospital_system.get_patient_by_id(patient_id)

        if patient:
            patient.appointments = []
            self.refresh_appointments()
            messagebox.showinfo("Success", f"Appointments for Patient {patient.name} cleared successfully!")
        else:
            messagebox.showerror("Error", f"Patient with ID {patient_id} not found. Please enter a valid patient ID.")


    def register_patient(self):
        patient_id = self.patient_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
            return
        patient = Patient(patient_id, name, age, gender)
        self.hospital_system.add_patient(patient)
        messagebox.showinfo("Success", f"Patient {name} registered successfully!")

    def register_doctor(self):
        doctor_id = self.doctor_id_entry.get()
        name = self.doctor_name_entry.get()
        specialization = self.specialization_entry.get()

        try:
            # Add validation for doctor_id as well, ensuring it's unique
            doctor_id = int(doctor_id)
        except ValueError:
            messagebox.showerror("Error", "Invalid doctor ID. Please enter a valid number.")
            return

        doctor = self.hospital_system.register_doctor(doctor_id, name, specialization)
        messagebox.showinfo("Success", f"Doctor {name} registered successfully!\nID: {doctor.doctor_id}, Specialization: {doctor.specialization}")

    def schedule_appointment(self):
        patient_id = self.patient_id_app_entry.get()
        doctor_id = self.doctor_id_app_entry.get()
        date = self.date_picker.get()
        time = self.time_combobox.get()

        # Validate patient_id and doctor_id
        patient = self.hospital_system.get_patient_by_id(patient_id)
        doctor = self.hospital_system.get_doctor_by_id(doctor_id)

        if not patient or not doctor:
            messagebox.showerror("Error", "Invalid patient ID or doctor ID. Please check and try again.")
            return

        try:
            # Add validation for patient_id and doctor_id
            appointment = self.hospital_system.schedule_appointment(patient_id, doctor_id, f"{date} {time}")
            if appointment:
                messagebox.showinfo("Success", f"Appointment scheduled successfully!\nPatient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date and Time: {appointment.date_time}")
            else:
                messagebox.showerror("Error", "Unable to schedule the appointment. Please try again.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
