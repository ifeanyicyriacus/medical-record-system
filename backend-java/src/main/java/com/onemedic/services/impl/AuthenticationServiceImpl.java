package com.onemedic.services.impl;

import com.onemedic.exceptions.IncorrectCredentialException;
import com.onemedic.models.Admin;
import com.onemedic.models.Clinician;
import com.onemedic.models.Patient;
import com.onemedic.models.User;
import com.onemedic.repositories.AdminRepository;
import com.onemedic.repositories.ClinicianRepository;
import com.onemedic.repositories.PatientRepository;
import com.onemedic.services.AuthenticationService;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationServiceImpl implements AuthenticationService {
    private final AdminRepository adminRepository;
    private final ClinicianRepository clinicianRepository;
    private final PatientRepository   patientRepository;

    public AuthenticationServiceImpl(AdminRepository adminRepository,
                                     ClinicianRepository clinicianRepository,
                                     PatientRepository patientRepository) {
        this.adminRepository = adminRepository;
        this.clinicianRepository = clinicianRepository;
        this.patientRepository = patientRepository;
    }


    @Override
    public User login(String email, String password, String userType) {
        return switch (userType) {
            case "SUPER_ADMIN", "ADMIN" -> loginAdmin(email, password);
            case "CLINICIAN" -> loginClinician(email, password);
            case "PATIENT" -> loginPatient(email, password);
            default -> throw new IllegalStateException("Unexpected value: " + userType);
        };
    }

    @Override
    public boolean changePassword(String email, String userType, String password, String newPassword) {

        return false;
    }

    private Admin loginAdmin(String email, String password) {
        Admin admin = adminRepository.findByEmail(email).orElse(null);
        if (admin == null || !admin.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return admin;

    }

    private Clinician loginClinician(String email, String password) {
        Clinician clinician = clinicianRepository.findByEmail(email).orElse(null);
        if (clinician == null || !clinician.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return clinician;
    }

    private Patient loginPatient(String email, String password) {
        Patient patient = patientRepository.findByEmail(email).orElse(null);
        if (patient == null || !patient.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return patient;
    }


}
