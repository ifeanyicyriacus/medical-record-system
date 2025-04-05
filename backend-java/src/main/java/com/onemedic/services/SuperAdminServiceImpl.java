package com.onemedic.services;

import com.onemedic.models.Admin;
import com.onemedic.models.Gender;
import com.onemedic.models.User;
import com.onemedic.repositories.AdminRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;

@Service
@RequiredArgsConstructor
public class SuperAdminServiceImpl implements SuperAdminService, AuthenticationService {
    private final AdminRepository adminRepository;
    private final PasswordEncoder passwordEncoder;

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
    public User login(String username, String password) {
        return null;
    }
}
