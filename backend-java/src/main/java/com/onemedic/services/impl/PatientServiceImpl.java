package com.onemedic.services.impl;


import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import com.onemedic.repositories.AppointmentRepository;
import com.onemedic.repositories.PatientRepository;
import com.onemedic.services.PatientService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class PatientServiceImpl implements PatientService {
    private final PatientRepository     patientRepository;
    private final AppointmentRepository   appointmentRepository;

    public PatientServiceImpl(PatientRepository patientRepository,
                              AppointmentRepository appointmentRepository) {
        this.patientRepository = patientRepository;
        this.appointmentRepository = appointmentRepository;
    }
    
    @Override
    public Patient updatePatient(Patient patient) {
        return patientRepository.save(patient);
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
    public Page<Appointment> getAllAppointmentsByPatientId(Pageable pageable, String patientId) {
        return appointmentRepository.findAllByPatientId(pageable, patientId);
    }

    @Override
    public MedicalRecord getPatientMedicalRecord(String patientId) {
        Optional<Patient> patient = patientRepository.findById(patientId);
        return patient.map(Patient::getMedicalRecord).orElse(null);
    }

}
