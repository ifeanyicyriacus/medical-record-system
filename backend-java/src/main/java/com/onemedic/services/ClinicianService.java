package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface ClinicianService {
    Patient createPatient(Patient patient);
    Page<Patient> getAllPatients(Pageable pageable);
    Patient updatePatient(String id, Patient patientDetails);
    Patient getPatientById(String id);
    Patient getPatientByEmail(String email);

    Appointment createAppointment(Appointment appointment);
    Appointment getAppointmentById(String id);
    Appointment updateAppointment(String id, Appointment appointmentDetails);
    Page<Appointment> getAllAppointments(Pageable pageable);
    Page<Appointment> getAllMyAppointmentsByClinicianId(String clinicianId, Pageable pageable);

    MedicalRecord getPatientMedicalRecord(String patientId);
    MedicalRecord.MedicalNote addMedicalNoteToRecord(String patientId, MedicalRecord.MedicalNote medicalNote);
}
