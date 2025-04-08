package com.onemedic.security.services;

import com.onemedic.models.Admin;
import com.onemedic.models.Clinician;
import com.onemedic.models.Patient;
import com.onemedic.models.UserType;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.repositories.ClinicianRepository;
import com.onemedic.repositories.PatientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.List;

@Service
@RequiredArgsConstructor
public class UnifiedUserDetailsService implements UserDetailsService {

    private final AdminRepository     adminRepository;
    private final ClinicianRepository clinicianRepository;
    private final PatientRepository   patientRepository;


    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        System.out.println("Searching for email: " + email); // Temporary log


        return adminRepository.findByEmail(email).map(admin -> admin.getType().equals(UserType.SUPER_ADMIN)
                                ? new AuthUser(admin, UserType.SUPER_ADMIN)
                                : new AuthUser(admin, UserType.ADMIN))
                .or(() -> {
                    System.out.println("Not fount in admin: " + email);
                    return clinicianRepository.findByEmail(email).map(clinician ->
                            new AuthUser(clinician, UserType.CLINICIAN));
                })
                .or(() -> {
                    System.out.println("Not fount in clinician: " + email);
                    return patientRepository.findByEmail(email).map(patient ->
                            new AuthUser(patient, UserType.PATIENT));
                })
                .orElseThrow(() -> {
                    System.out.println("Not fount in patient: " + email);
                    return new UsernameNotFoundException("User not found: " + email);
                });
    }

    public record AuthUser(String id, String email, String password, UserType userType) implements UserDetails {

        public AuthUser(Object entity, UserType userType) {
            this(
                    getEntityId(entity),
                    getEntityEmail(entity),
                    getEntityPassword(entity),
                    userType
            );
        }

        @Override
        public Collection<? extends GrantedAuthority> getAuthorities() {
            return List.of(new SimpleGrantedAuthority("ROLE_" + userType.name()));
        }

        @Override
        public String getPassword() {
            return this.password;
        }

        @Override
        public String getUsername() {
            return this.email;
        }
    }

    private static String getEntityId(Object entity) {
        if (entity instanceof Admin admin) return admin.getId();
        if (entity instanceof Clinician clinician) return clinician.getId();
        if (entity instanceof Patient patient) return patient.getId();
        throw new IllegalArgumentException("Invalid entity: " + entity);
    }

    private static String getEntityEmail(Object entity) {
        if (entity instanceof Admin admin) return admin.getEmail();
        if (entity instanceof Clinician clinician) return clinician.getEmail();
        if (entity instanceof Patient patient) return patient.getEmail();
        throw new IllegalArgumentException("Invalid entity: " + entity);
    }

    private static String getEntityPassword(Object entity) {
        if (entity instanceof Admin admin) return admin.getPassword();
        if (entity instanceof Clinician clinician) return clinician.getPassword();
        if (entity instanceof Patient patient) return patient.getPassword();
        throw new IllegalArgumentException("Invalid entity: " + entity);
    }
}
