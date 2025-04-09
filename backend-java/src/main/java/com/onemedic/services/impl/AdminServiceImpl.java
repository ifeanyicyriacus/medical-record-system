package com.onemedic.services.impl;

import com.onemedic.exceptions.UserNotFoundException;
import com.onemedic.models.Appointment;
import com.onemedic.models.Clinician;
import com.onemedic.repositories.AppointmentRepository;
import com.onemedic.repositories.ClinicianRepository;
import com.onemedic.services.AdminService;
import com.onemedic.utils.UpdateMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class AdminServiceImpl implements AdminService {
    private final ClinicianRepository   clinicianRepository;
    private final AppointmentRepository appointmentRepository;

    public AdminServiceImpl(ClinicianRepository clinicianRepository, AppointmentRepository appointmentRepository) {
        this.clinicianRepository = clinicianRepository;
        this.appointmentRepository = appointmentRepository;
    }

    @Override
    public Clinician createClinician(Clinician clinician) {
        return clinicianRepository.save(clinician);
    }

    @Override
    public Page<Clinician> getAllClinicians(Pageable pageable) {
        return clinicianRepository.findAll(pageable);
    }

    @Override
    public Clinician getClinicianById(String id) {
        return clinicianRepository.findById(id).orElseThrow(() -> new UserNotFoundException("Clinician"));
    }

    @Override
    public Clinician getClinicianByEmail(String email) {
        return clinicianRepository.findByEmail(email).orElseThrow(() -> new UserNotFoundException("Clinician"));
    }

    @Override
    public Clinician updateClinician(String id, Clinician clinicianDetails) {
        Clinician clinician = getClinicianById(id);
        clinician.setLicenseNumber(clinicianDetails.getLicenseNumber());
        clinician.setSpecialization(clinicianDetails.getSpecialization());
        UpdateMapper.updateUser(clinician, clinicianDetails);
        return clinicianRepository.save(clinician);
    }

    @Override
    public Page<Appointment> getAllAppointments(Pageable pageable) {
        return appointmentRepository.findAll(pageable);
    }

    @Override
    public Page<Appointment> getAllAppointmentsByClinicianId(String clinicianId, Pageable pageable) {
        return appointmentRepository.findAllByClinicianId(clinicianId, pageable);
    }
}
