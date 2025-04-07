package com.onemedic.models;

import lombok.Data;

import java.util.Date;


@Data
public abstract class  User {
    private String firstName;
    private String lastName;
    private String email;
    private String phone;
    private Date date0fBirth;
    private Gender gender;
    private UserType type;
}
