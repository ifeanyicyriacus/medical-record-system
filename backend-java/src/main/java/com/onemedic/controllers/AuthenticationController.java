package com.onemedic.controllers;

import com.onemedic.dtos.requests.ChangePasswordRequestDto;
import com.onemedic.dtos.requests.LoginRequestDto;
import com.onemedic.dtos.responses.ChangePasswordResponseDto;
import com.onemedic.dtos.responses.LoginResponseDto;
import com.onemedic.services.AuthenticationService;
import com.onemedic.services.impl.AuthenticationServiceImpl;
import jakarta.validation.Valid;
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
    public LoginResponseDto login(@Valid @RequestBody LoginRequestDto loginRequestDto) {
        return authenticationService.login(loginRequestDto);
    }

    @PostMapping("/change-password")
    public ChangePasswordResponseDto changePassword(@RequestBody ChangePasswordRequestDto changePasswordRequestDto) {
        return authenticationService.changePassword(changePasswordRequestDto);
    }

}
