package com.onemedic.dtos.responses;

import com.onemedic.models.User;
import lombok.Getter;

@Getter
final public class LoginResponse {
    String id;
    String userType;
    String email;
    String firstName;
    String lastName;
    String dateOfBirth;
    String gender;
    String phoneNumber;

    public LoginResponse(User user) {
        this.id = user.getId();
        this.userType = user.getType().toString();
        this.email = user.getEmail();
        this.firstName = user.getFirstName();
        this.lastName = user.getLastName();
        this.dateOfBirth = user.getDate0fBirth().toString();
        this.gender = user.getGender().toString();
        this.phoneNumber = user.getPhoneNumber();
    }
}
