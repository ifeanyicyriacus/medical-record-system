package com.onemedic.services;

import com.onemedic.models.Admin;
import com.onemedic.repositories.AdminRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class AdminServiceImpl implements AdminService, AuthenticationService {
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
            adminRepository.save(admin);
        }
    }

    @Override
    public Admin login(String email, String password) {
        Optional<Admin> admin = adminRepository.findByEmail(email);
        if (admin.isPresent()) {
            if (passwordEncoder.matches(password, admin.get().getPassword())) {
                return admin.get();
            }else return null;
        } else return null;
    }
}
