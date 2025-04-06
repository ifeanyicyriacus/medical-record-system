package com.onemedic.dtos.responses;

import lombok.Getter;

@Getter
final public class ChangePasswordResponse {

    private boolean success;
    private final String message;
    public ChangePasswordResponse(boolean success) {
        this.success = success;
        this.message = (success ?
                "Password changed successfully!" :
                "Password changed failed!");
    }
}
