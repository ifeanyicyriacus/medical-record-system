package com.onemedic.dtos.requests;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
final public class LoginRequest {
    private String email;
    private String password;
    private String type;
}
