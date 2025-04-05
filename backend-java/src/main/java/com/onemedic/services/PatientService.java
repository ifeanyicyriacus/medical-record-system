package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface PatientService {
    Patient updatePatient(Patient patient);
    Appointment createAppointment(Appointment appointment);
    Appointment updateAppointment(Appointment appointment);
    Page<Appointment> getAllAppointmentsByPatientId(Pageable pageable, String patientId);
    MedicalRecord getPatientMedicalRecord(String patientId);
}
