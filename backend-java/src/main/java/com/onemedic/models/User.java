package com.onemedic.models;

import lombok.Data;
import org.springframework.data.mongodb.core.index.Indexed;

import java.time.LocalDate;


@Data
public abstract class User {
    @Indexed(unique = true)
    private String    email;
    private String    password;
    private String    firstName;
    private String    lastName;
    private String    phoneNumber;
    private LocalDate date0fBirth;
    private Gender    gender;
//    private UserType type;
}
