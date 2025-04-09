package com.onemedic.exceptions;

public class IncorrectCredentialException extends RuntimeException {
    public IncorrectCredentialException() {
        super("Incorrect email or password");
    }
}