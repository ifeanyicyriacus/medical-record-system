package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;

public interface PatientService {
    Patient updatePatient(Patient patient);
    Appointment createAppointment(Appointment appointment);
    Appointment updateAppointment(Appointment appointment);
    MedicalRecord getPatientMedicalRecord(String patientId);
}
