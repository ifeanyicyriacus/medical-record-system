class MedicalRecordSystemException(Exception):
    pass

class PatientNotFoundException(MedicalRecordSystemException):
    def __init__(self, patient_id):
        self.message = f"Patient with ID {patient_id} not found."
        super().__init__(self.message)

class DoctorNotFoundException(MedicalRecordSystemException):
    def __init__(self, doctor_id):
        self.message = f"Doctor with ID {doctor_id} not found."
        super().__init__(self.message)

class AppointmentNotFoundException(MedicalRecordSystemException):
    def __init__(self, appointment_id):
        self.message = f"Appointment with ID {appointment_id} not found."
        super().__init__(self.message)