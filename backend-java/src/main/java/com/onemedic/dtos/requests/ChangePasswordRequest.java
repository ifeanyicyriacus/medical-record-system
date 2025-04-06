package com.onemedic.dtos.requests;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
final public class ChangePasswordRequest {
    private String email;
    private String type;
    private String password;
    private String newPassword;
}
