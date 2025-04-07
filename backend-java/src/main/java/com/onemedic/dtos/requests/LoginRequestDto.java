package com.onemedic.dtos.requests;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
final public class LoginRequestDto {
    @NotBlank(message = "Email is required")
    @Size(min = 2, max = 50)
    private String email;

    @NotBlank(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    private String password;

    @NotBlank(message = "User-type is required")
    private String type;
}
