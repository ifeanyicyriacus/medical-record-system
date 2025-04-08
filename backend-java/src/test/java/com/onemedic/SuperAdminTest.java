package com.onemedic;

import com.onemedic.models.Admin;
import com.onemedic.repositories.AdminRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.annotation.DirtiesContext;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
public class SuperAdminTest {

    @Autowired
    private AdminRepository adminRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @Test
    void thatSystemCreatesSuperAdminOnStartup() {
        Optional<Admin> admin = adminRepository.findByEmail("testadmin@example.com");
        assertTrue(admin.isPresent());
        assertEquals("SUPER_ADMIN", admin.get().getType().toString());
        assertTrue(passwordEncoder.matches("testStrongPassword123!", admin.get().getPassword()));
    }

}
