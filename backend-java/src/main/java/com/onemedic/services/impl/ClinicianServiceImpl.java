package com.onemedic.services.impl;

import com.onemedic.exceptions.AppointmentNotFoundException;
import com.onemedic.exceptions.UserNotFoundException;
import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import com.onemedic.repositories.*;
import com.onemedic.services.ClinicianService;
import com.onemedic.utils.UpdateMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class ClinicianServiceImpl implements ClinicianService {
    private final PatientRepository       patientRepository;
    private final AppointmentRepository   appointmentRepository;
    private final MedicalRecordRepository medicalRecordRepository;
    private final MedicalNoteRepository   medicalNoteRepository;

    public ClinicianServiceImpl(PatientRepository patientRepository,
                                MedicalRecordRepository medicalRecordRepository,
                                AppointmentRepository appointmentRepository,
                                MedicalNoteRepository medicalNoteRepository) {
        this.patientRepository = patientRepository;
        this.medicalRecordRepository = medicalRecordRepository;
        this.appointmentRepository = appointmentRepository;
        this.medicalNoteRepository = medicalNoteRepository;
    }

    @Override
    public Patient createPatient(Patient patient) {
        return patientRepository.save(patient);
    }

    @Override
    public Page<Patient> getAllPatients(Pageable pageable) {
        return patientRepository.findAll(pageable);
    }

    @Override
    public Patient updatePatient(String id, Patient patientDetails) {
        Patient patient = getPatientById(id);
        UpdateMapper.updateUser(patient, patientDetails);
        return patientRepository.save(patient);
    }

    @Override
    public Patient getPatientById(String id) {
        return patientRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException("Patient"));
    }

    @Override
    public Patient getPatientByEmail(String email) {
        return patientRepository.findByEmail(email)
                .orElseThrow(() -> new UserNotFoundException("Patient"));
    }

    @Override
    public Appointment createAppointment(Appointment appointment) {
        return appointmentRepository.save(appointment);
    }

    @Override
    public Appointment getAppointmentById(String id) {
        return appointmentRepository.findById(id)
                .orElseThrow(AppointmentNotFoundException::new);
    }

    @Override
    public Appointment updateAppointment(String id, Appointment appointmentDetails) {
        Appointment appointment = getAppointmentById(id);
        UpdateMapper.updateAppointment(appointment, appointmentDetails);
        return appointmentRepository.save(appointment);
    }

    @Override
    public Page<Appointment> getAllAppointments(Pageable pageable) {
        return appointmentRepository.findAll(pageable);
    }

    @Override
    public Page<Appointment> getAllMyAppointmentsByClinicianId(String clinicianId, Pageable pageable) {
        return appointmentRepository.findAllByClinicianId(clinicianId, pageable);
    }

    @Override
    public MedicalRecord getPatientMedicalRecord(String patientId) {
        return getPatientById(patientId).getMedicalRecord();
    }

    @Override
    public MedicalRecord.MedicalNote addMedicalNoteToRecord(String patientId, MedicalRecord.MedicalNote medicalNote){
        MedicalRecord.MedicalNote newMedicalNote = medicalNoteRepository.save(medicalNote);
        MedicalRecord medicalRecord = getPatientMedicalRecord(patientId);
        medicalRecord.getMedicalNotes().add(newMedicalNote);
        medicalRecordRepository.save(medicalRecord);
        return newMedicalNote;
    }
}
