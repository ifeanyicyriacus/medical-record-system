package com.onemedic.services.impl;

import com.onemedic.models.Admin;
import com.onemedic.models.Gender;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.repositories.ClinicianRepository;
import com.onemedic.services.SuperAdminService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;

@Service
public class SuperAdminServiceImpl extends AdminServiceImpl implements SuperAdminService {
    private final AdminRepository adminRepository;
    private final PasswordEncoder passwordEncoder;

    public SuperAdminServiceImpl(ClinicianRepository clinicianRepository, AdminRepository adminRepository, PasswordEncoder passwordEncoder) {
        super(clinicianRepository, adminRepository);
        this.adminRepository = adminRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    @Transactional
    public void createSuperAdminIfNotExist(String email, String rawPassword, String role) {
        if (!adminRepository.existsByEmail(email)) {
            Admin admin = new Admin();
            admin.setEmail(email);
            admin.setPassword(passwordEncoder.encode(rawPassword));
            admin.setRole(role);
            admin.setFirstName("SuperAdmin");
            admin.setLastName("Admin");
            admin.setPhoneNumber("+2348000000001");
            admin.setDate0fBirth(LocalDate.of(1900, 1, 1));
            admin.setGender(Gender.FEMALE);
            adminRepository.save(admin);
        }
    }

    @Override
    public Admin createAdmin(Admin admin) {
        return adminRepository.save(admin);
    }

    @Override
    public Page<Admin> getAdmins(Pageable pageable) {
        return adminRepository.findAll(pageable);
    }
}
