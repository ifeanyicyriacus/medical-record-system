package com.onemedic.configs;

import com.onemedic.models.UserType;
import com.onemedic.services.SuperAdminService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@RequiredArgsConstructor
public class InitialAdminConfig {
    private final SuperAdminService superAdminService;

    @Value("${super-admin.email}")
    private String superAdminEmail;

    @Value("${super-admin.password}")
    private String superAdminPassword;

    @Bean
    public CommandLineRunner createInitialAdmin() {
        return _ -> superAdminService.createSuperAdminIfNotExist(superAdminEmail, superAdminPassword);
    }
}
