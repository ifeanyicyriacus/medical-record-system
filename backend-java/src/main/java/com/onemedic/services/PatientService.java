package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface PatientService {
    Appointment createAppointment(Appointment appointment);
    Appointment updateAppointment(String id, Appointment appointmentDetails);
    Page<Appointment> getAllAppointmentsByPatientId(String patientId, Pageable pageable);
    MedicalRecord getMedicalRecord(String patientId);
}
