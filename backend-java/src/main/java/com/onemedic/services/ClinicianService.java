package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.Clinician;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface ClinicianService {
    Appointment createAppointment(Appointment appointment);
    Appointment updateAppointment(Appointment appointment);
    Page<Appointment> getAllMyAppointmentsByClinicianId(Pageable pageable, String clinicianId);
    Patient createPatient(Patient patient);
    Patient getPatientById(String id);
    Patient getPatientByEmail(String email);
    MedicalRecord getPatientMedicalRecord(String patientId);
    Clinician updateClinician(Clinician clinician);
    MedicalRecord.MedicalNote addMedicalNoteToRecord(MedicalRecord.MedicalNote medicalNote, String patientId);
}
