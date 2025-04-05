package com.onemedic.services;

import com.onemedic.models.User;

public interface AuthenticationService {
    User login(String username, String password);
}
