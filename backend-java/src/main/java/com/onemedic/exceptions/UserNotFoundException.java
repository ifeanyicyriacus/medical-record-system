package com.onemedic.exceptions;

public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String userType) {
        super("(" + userType + ") User not found");
    }
}