package com.onemedic.services;

import com.onemedic.models.Admin;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.services.impl.SuperAdminServiceImpl;
import org.junit.jupiter.api.Test;
import org.mockito.ArgumentCaptor;
import org.springframework.security.crypto.password.PasswordEncoder;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

class SuperAdminServiceTest {
    private final AdminRepository adminRepository = mock(AdminRepository.class);
    private final PasswordEncoder   passwordEncoder   = mock(PasswordEncoder.class);
    private final SuperAdminService superAdminService = new SuperAdminServiceImpl(adminRepository, passwordEncoder);

    @Test
    public void shouldCreateAdminWhenNotExists() {
        // Given
        String email = "newadmin@example.com";
        String password = "password";


        when(adminRepository.existsByEmail(email)).thenReturn(false);
        when(passwordEncoder.encode(password)).thenReturn("encodedPassword");

        // When
        superAdminService.createSuperAdminIfNotExists(email, password);

        // Then
        ArgumentCaptor<Admin> adminCaptor = ArgumentCaptor.forClass(Admin.class);
        verify(adminRepository).save(adminCaptor.capture());

        Admin savedAdmin = adminCaptor.getValue();
        assertEquals(email, savedAdmin.getEmail());
        assertEquals("encodedPassword", savedAdmin.getPassword());
        assertEquals("SUPER_ADMIN", savedAdmin.getType().toString());
    }

    @Test
    public void shouldNotCreateAdminWhenExists() {
        // Given
        String email = "existing@example.com";
        when(adminRepository.existsByEmail(email)).thenReturn(true);

        // When
        superAdminService.createSuperAdminIfNotExists(email, "anyPassword");

        // Then
        verify(adminRepository, never()).save(any());
    }

}