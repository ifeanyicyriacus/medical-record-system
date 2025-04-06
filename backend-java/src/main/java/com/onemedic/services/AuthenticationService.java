package com.onemedic.services;

import com.onemedic.models.User;


public interface AuthenticationService {
    User login(String email, String password, String userType);
    boolean changePassword(String email, String userType, String password, String newPassword);
}
