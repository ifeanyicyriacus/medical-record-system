package com.onemedic.services;

import com.onemedic.dtos.requests.ChangePasswordRequestDto;
import com.onemedic.dtos.requests.LoginRequestDto;
import com.onemedic.dtos.responses.ChangePasswordResponseDto;
import com.onemedic.dtos.responses.LoginResponseDto;


public interface AuthenticationService {
    LoginResponseDto login(LoginRequestDto loginRequestDto);
    ChangePasswordResponseDto changePassword(ChangePasswordRequestDto changePasswordRequestDto);
}
