package com.onemedic.services;

import com.onemedic.models.User;

public interface AuthenticationService {
    User login(String email, String password, String userType);
}
