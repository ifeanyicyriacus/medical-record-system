package com.onemedic.dtos.responses;

import lombok.Data;

@Data
final public class LoginResponseDto {
    String id;
    String userType;
    String email;
    String firstName;
    String lastName;
    String dateOfBirth;
    String gender;
    String phoneNumber;
}
