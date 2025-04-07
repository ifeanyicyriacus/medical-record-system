

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

class ValidationError(MedicalRecordSystemException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DatabaseError(MedicalRecordSystemException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class UnauthorizedAccessException(MedicalRecordSystemException):
    def __init__(self, message="Unauthorized access"):
        self.message = message
        super().__init__(self.message)

class IncorrectLoginCredentialsException(MedicalRecordSystemException):
    def __init__(self):
        self.message = "Incorrect login credentials."
        super().__init__(self.message)

class EmailAlreadyExistsException(MedicalRecordSystemException):
    def __init__(self, email):
        self.message = f"Email {email} already exists."
        super().__init__(self.message)


class UserNotFoundException:
    def __init__(self, email):
        self.message = "User not found"
        super().__init__(self.message)