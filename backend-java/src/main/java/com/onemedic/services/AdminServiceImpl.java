package com.onemedic.services;

import com.onemedic.models.Admin;
import com.onemedic.models.Clinician;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.repositories.ClinicianRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class AdminServiceImpl implements AdminService {
    private final ClinicianRepository clinicianRepository;
    private final AdminRepository adminRepository;

    public AdminServiceImpl(ClinicianRepository clinicianRepository, AdminRepository adminRepository) {
        this.clinicianRepository = clinicianRepository;
        this.adminRepository = adminRepository;
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
        return clinicianRepository.findById(id).orElse(null);
    }

    @Override
    public Clinician getByEmail(String email) {
        return clinicianRepository.findByEmail(email).orElse(null);
    }

    @Override
    public Clinician updateClinician(Clinician clinician) {
        return clinicianRepository.save(clinician);
    }

    @Override
    public Admin updateAdmin(Admin admin) {
        return adminRepository.save(admin);
    }

    @Override
    public Admin getAdminByEmail(String email) {
        return adminRepository.findByEmail(email).orElse(null);
    }

    @Override
    public Admin getAdminById(String id) {
        return adminRepository.findById(id).orElse(null);
    }
}
