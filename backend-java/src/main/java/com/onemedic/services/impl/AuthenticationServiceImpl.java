package com.onemedic.services.impl;

import com.onemedic.dtos.requests.ChangePasswordRequestDto;
import com.onemedic.dtos.requests.LoginRequestDto;
import com.onemedic.dtos.responses.ChangePasswordResponseDto;
import com.onemedic.dtos.responses.LoginResponseDto;
import com.onemedic.exceptions.IncorrectCredentialException;
import com.onemedic.exceptions.UserNotFoundException;
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
    public LoginResponseDto login(LoginRequestDto loginRequestDto) {
        String email = loginRequestDto.getEmail();
        String password = loginRequestDto.getPassword();
        String userType = loginRequestDto.getType();

        return switch (userType) {
            case "SUPER_ADMIN", "ADMIN" -> loginAdmin(email, password);
            case "CLINICIAN" -> loginClinician(email, password);
            case "PATIENT" -> loginPatient(email, password);
            default -> throw new IllegalStateException("Unexpected value: " + userType);
        };
    }

    @Override
    public ChangePasswordResponseDto changePassword(ChangePasswordRequestDto changePasswordRequestDto) {

        String email = changePasswordRequestDto.getEmail();
        String userType = changePasswordRequestDto.getType();
        String password = changePasswordRequestDto.getPassword();
        String newPassword = changePasswordRequestDto.getNewPassword();

        User user = switch (userType) {
            case "SUPER_ADMIN", "ADMIN" -> adminRepository.findByEmail(email)
                    .orElseThrow(() -> new UserNotFoundException("Admin"));
            case "CLINICIAN" -> clinicianRepository.findByEmail(email)
                    .orElseThrow(() -> new UserNotFoundException("Clinician"));
            case "PATIENT" -> patientRepository.findByEmail(email)
                    .orElseThrow(() -> new UserNotFoundException("Patient"));
            default -> throw new IllegalStateException("Unexpected value: " + userType);
        };

        final boolean correctPasswordConfirmation = user.getPassword().equals(password);
        if (correctPasswordConfirmation) {
            user.setPassword(newPassword);
            switch (userType) {
                case "SUPER_ADMIN", "ADMIN" -> adminRepository.save((Admin)user);
                case "CLINICIAN" -> clinicianRepository.save((Clinician)user);
                case "PATIENT" -> patientRepository.save((Patient)user);
            }
        }

        ChangePasswordResponseDto changePasswordResponseDto = new ChangePasswordResponseDto();
        changePasswordResponseDto.setSuccess(correctPasswordConfirmation);
        changePasswordResponseDto.setMessage((correctPasswordConfirmation)
                ? "Password changed successfully!"
                : "Password unchanged failed!");

        return changePasswordResponseDto;
    }

    private LoginResponseDto loginAdmin(String email, String password) {
        Admin admin = adminRepository.findByEmail(email).orElse(null);
        if (admin == null || !admin.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return mapToLoginResponse(admin);
    }

    private LoginResponseDto loginClinician(String email, String password) {
        Clinician clinician = clinicianRepository.findByEmail(email).orElse(null);
        if (clinician == null || !clinician.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return mapToLoginResponse(clinician);
    }

    private LoginResponseDto loginPatient(String email, String password) {
        Patient patient = patientRepository.findByEmail(email).orElse(null);
        if (patient == null || !patient.getPassword().equals(password))
            throw new IncorrectCredentialException();
        return mapToLoginResponse(patient);
    }

    private LoginResponseDto mapToLoginResponse(User user) {
        LoginResponseDto responseDto = new LoginResponseDto();
        responseDto.setId(user.getId());
        responseDto.setEmail(user.getEmail());
        responseDto.setFirstName(user.getFirstName());
        responseDto.setLastName(user.getLastName());
        responseDto.setUserType(user.getType().toString());
        responseDto.setGender(user.getGender().toString());
        responseDto.setPhoneNumber(user.getPhoneNumber());
        return responseDto;
    }
}
