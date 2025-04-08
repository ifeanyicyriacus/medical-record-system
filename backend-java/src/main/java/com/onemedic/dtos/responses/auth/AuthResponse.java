package com.onemedic.dtos.responses.auth;

public record AuthResponse(
        String token,
        String userId,
        String email,
        String userType
) {}