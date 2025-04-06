package com.onemedic.services.impl;


import com.onemedic.exceptions.AppointmentNotFoundException;
import com.onemedic.exceptions.UserNotFoundException;
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
    public Appointment createAppointment(Appointment appointment) {
        return appointmentRepository.save(appointment);
    }

    @Override
    public Appointment updateAppointment(String id, Appointment appointmentDetails) {
        Appointment appointment = getAppointmentById(id);
        Updater.updateAppointment(appointment, appointmentDetails);
        return appointmentRepository.save(appointment);
    }

    private Appointment getAppointmentById(String id) {
        return appointmentRepository.findById(id)
                .orElseThrow(AppointmentNotFoundException::new);
    }

    @Override
    public Page<Appointment> getAllAppointmentsByPatientId(String patientId, Pageable pageable) {
        return appointmentRepository.findAllByPatientId(patientId, pageable);
    }

    @Override
    public MedicalRecord getMedicalRecord(String patientId) {
        Optional<Patient> patient = patientRepository.findById(patientId);
        return patient.map(Patient::getMedicalRecord)
                .orElseThrow(() -> new UserNotFoundException("Patient"));
    }

}
