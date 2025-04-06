package com.onemedic.controllers;

import com.onemedic.dtos.requests.ChangePasswordRequest;
import com.onemedic.dtos.requests.LoginRequest;
import com.onemedic.dtos.responses.ChangePasswordResponse;
import com.onemedic.dtos.responses.LoginResponse;
import com.onemedic.services.AuthenticationService;
import com.onemedic.services.impl.AuthenticationServiceImpl;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/auth")
public class AuthenticationController {
    private final AuthenticationService authenticationService;

    public AuthenticationController(AuthenticationServiceImpl authenticationService) {
        this.authenticationService = authenticationService;
    }

    @PostMapping("/login")
    public LoginResponse login(@RequestBody LoginRequest loginRequest) {
        String email = loginRequest.getEmail();
        String password = loginRequest.getPassword();
        String userType = loginRequest.getType();
        return new LoginResponse(authenticationService.login(email, password, userType));
    }

    @PostMapping("/change-password")
    public ChangePasswordResponse changePassword(@RequestBody ChangePasswordRequest changePasswordRequest) {
        String email = changePasswordRequest.getEmail();
        String userType = changePasswordRequest.getType();
        String password = changePasswordRequest.getPassword();
        String newPassword = changePasswordRequest.getNewPassword();
        return  new ChangePasswordResponse(
                authenticationService.changePassword(email, userType, password, newPassword));
    }


}
