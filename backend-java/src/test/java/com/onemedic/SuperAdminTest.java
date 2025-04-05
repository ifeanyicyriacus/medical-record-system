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
//    @Autowired
//    private SuperAdminServiceImpl adminService;


    @Test
    void thatSystemCreatesSuperAdminOnStartup() {
        Optional<Admin> admin = adminRepository.findByEmail("testadmin@example.com");
        assertTrue(admin.isPresent());
        assertEquals("SUPER_ADMIN", admin.get().getRole());
        assertTrue(passwordEncoder.matches("testStrongPassword123!", admin.get().getPassword()));
    }


//    @Test
//    void thatSuperAdminCanLogin() {
//        String correctEmail = "testadmin@example.com";
//        String correctPassword = passwordEncoder.encode("testStrongPassword123!");
//        Admin admin = adminService.login(correctEmail, correctPassword);
//        assertNotNull(admin);
//    }



}
