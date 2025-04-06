package com.onemedic.services.impl;

import com.onemedic.exceptions.UserNotFoundException;
import com.onemedic.models.Admin;
import com.onemedic.models.Gender;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.services.SuperAdminService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;

@Service
public class SuperAdminServiceImpl implements SuperAdminService {
    private final AdminRepository adminRepository;
    private final PasswordEncoder passwordEncoder;

    public SuperAdminServiceImpl(AdminRepository adminRepository, PasswordEncoder passwordEncoder) {
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
    public Page<Admin> getAllAdmins(Pageable pageable) {
        return adminRepository.findAll(pageable);
    }

    @Override
    public Admin updateAdmin(String id, Admin adminDetails) {
        Admin admin = getAdminById(id);
        Updater.updateUser(admin, adminDetails);
        return adminRepository.save(admin);
    }

    @Override
    public Admin getAdminByEmail(String email) {
        return adminRepository.findByEmail(email).orElseThrow(() -> new UserNotFoundException("Admin"));
    }

    @Override
    public Admin getAdminById(String id) {
        return adminRepository.findById(id).orElseThrow(() -> new UserNotFoundException("Admin"));
    }

}
