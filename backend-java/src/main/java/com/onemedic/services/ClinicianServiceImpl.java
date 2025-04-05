package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.Clinician;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import com.onemedic.repositories.*;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ClinicianServiceImpl implements ClinicianService {
    private final ClinicianRepository clinicianRepository;
    private final PatientRepository       patientRepository;
    private final AppointmentRepository   appointmentRepository;
    private final MedicalRecordRepository medicalRecordRepository;
    private final MedicalNoteRepository   medicalNoteRepository;

    public ClinicianServiceImpl(ClinicianRepository clinicianRepository,
                                PatientRepository patientRepository,
                                MedicalRecordRepository medicalRecordRepository,
                                AppointmentRepository appointmentRepository, MedicalNoteRepository medicalNoteRepository) {
        this.clinicianRepository = clinicianRepository;
        this.patientRepository = patientRepository;
        this.medicalRecordRepository = medicalRecordRepository;
        this.appointmentRepository = appointmentRepository;
        this.medicalNoteRepository = medicalNoteRepository;
    }


    @Override
    public Appointment createAppointment(Appointment appointment) {
        return appointmentRepository.save(appointment);
    }

    @Override
    public Appointment updateAppointment(Appointment appointment) {
        return appointmentRepository.save(appointment);
    }

    @Override
    public Page<Appointment> getAllMyAppointmentsByClinicianId(Pageable pageable, String clinicianId) {
        return appointmentRepository.findAllByClinicianId(clinicianId);
    }

    @Override
    public Patient createPatient(Patient patient) {
        return patientRepository.save(patient);
    }

    @Override
    public Patient getPatientById(String id) {
        return patientRepository.findById(id).orElse(null);
    }

    @Override
    public Patient getPatientByEmail(String email) {
        return patientRepository.findByEmail(email).orElse(null);
    }

    @Override
    public MedicalRecord getPatientMedicalRecord(String patientId) {
        Optional<Patient> patient = patientRepository.findById(patientId);
        return patient.map(Patient::getMedicalRecord).orElse(null);
    }

    @Override
    public Clinician updateClinician(Clinician clinician) {
        return clinicianRepository.save(clinician);
    }

    @Override
    public MedicalRecord.MedicalNote addMedicalNoteToRecord(MedicalRecord.MedicalNote medicalNote, String patientId){
        MedicalRecord.MedicalNote newMedicalNote = medicalNoteRepository.save(medicalNote);
        MedicalRecord medicalRecord = getPatientMedicalRecord(patientId);
        medicalRecord.getMedicalNotes().add(newMedicalNote);
        medicalRecordRepository.save(medicalRecord);
        return newMedicalNote;
    }
}
