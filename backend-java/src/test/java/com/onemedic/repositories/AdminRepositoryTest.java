package com.onemedic.repositories;

import com.onemedic.models.Admin;
import com.onemedic.models.Gender;
import com.onemedic.models.UserType;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.data.mongo.DataMongoTest;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

@DataMongoTest
public class AdminRepositoryTest {

    @Autowired
    private AdminRepository adminRepository;

    @Test
    public void shouldSaveAdmin() {
        Admin admin = new Admin();
        admin.setFirstName("John");
        admin.setLastName("Smith");
        admin.setType(UserType.ADMIN);
        admin.setGender(Gender.MALE);
        admin.setDate0fBirth(LocalDate.of(1995, 2, 14));
        admin.setPhoneNumber("+234706600");
        admin.setEmail("john.smith@gmail.com");
        admin.setPassword("password");

        assertNull(admin.getId());
        adminRepository.save(admin);

        boolean exists = adminRepository.existsByEmail(admin.getEmail());
        assertTrue(exists);

        assertNotNull(admin.getId());
    }
}
