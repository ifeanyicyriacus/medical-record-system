package com.onemedic.dtos.requests;

import lombok.Data;

@Data
final public class ChangePasswordRequestDto {
    private String email;
    private String type;
    private String password;
    private String newPassword;
}
