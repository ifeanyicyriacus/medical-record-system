package com.onemedic.models;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDate;


@Data
public abstract class User {
    private String    email;
    private String    password;
    private String    firstName;
    private String    lastName;
    private String    phone;
    private LocalDate date0fBirth;
    private Gender    gender;
//    private UserType type;
}
