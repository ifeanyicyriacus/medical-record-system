package com.onemedic.services.impl;

import com.onemedic.exceptions.UserNotFoundException;
import com.onemedic.models.Clinician;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.repositories.ClinicianRepository;
import com.onemedic.services.AdminService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class AdminServiceImpl implements AdminService {
    private final ClinicianRepository clinicianRepository;

    public AdminServiceImpl(ClinicianRepository clinicianRepository, AdminRepository adminRepository) {
        this.clinicianRepository = clinicianRepository;
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
        clinician.setDate0fBirth(clinicianDetails.getDate0fBirth());
        clinician.setEmail(clinicianDetails.getEmail());
        clinician.setFirstName(clinicianDetails.getFirstName());
        clinician.setLastName(clinicianDetails.getLastName());
        clinician.setGender(clinicianDetails.getGender());
        clinician.setPhoneNumber(clinicianDetails.getPhoneNumber());
        return clinicianRepository.save(clinician);
    }
}
