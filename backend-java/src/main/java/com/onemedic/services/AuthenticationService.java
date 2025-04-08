package com.onemedic.services;

import com.onemedic.dtos.requests.auth.LoginDto;
import com.onemedic.dtos.responses.auth.AuthResponse;


public interface AuthenticationService {
    AuthResponse login(LoginDto loginRequestDto);
//    ChangePasswordResponseDto changePassword(ChangePasswordRequestDto changePasswordRequestDto);
}
