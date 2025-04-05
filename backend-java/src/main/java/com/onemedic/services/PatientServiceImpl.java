package com.onemedic.services;


import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import com.onemedic.repositories.AppointmentRepository;
import com.onemedic.repositories.MedicalRecordRepository;
import com.onemedic.repositories.PatientRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class PatientServiceImpl implements PatientService {
    private final PatientRepository     patientRepository;
    private final AppointmentRepository   appointmentRepository;
    private final MedicalRecordRepository medicalRecordRepository;

    public PatientServiceImpl(PatientRepository patientRepository,
                              AppointmentRepository appointmentRepository, 
                              MedicalRecordRepository medicalRecordRepository) {
        this.patientRepository = patientRepository;
        this.appointmentRepository = appointmentRepository;
        this.medicalRecordRepository = medicalRecordRepository;
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
    public MedicalRecord getPatientMedicalRecord(String patientId) {
        Optional<Patient> patient = patientRepository.findById(patientId);
        return patient.map(Patient::getMedicalRecord).orElse(null);
    }

}
