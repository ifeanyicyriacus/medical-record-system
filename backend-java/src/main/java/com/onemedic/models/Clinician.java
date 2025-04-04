package com.onemedic.models;

import lombok.Data;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDate;
import java.util.Date;


//@Getter
@Data
@Document(collection = "clinicians")
public class Clinician extends User {

    @Id
    private String         id;
    private String         licenseNumber;
    private Specialization specialization;

//    public Clinician(String email, String password, String firstName, String lastName, String phone, LocalDate date0fBirth, Gender gender) {
//        super(email, password, firstName, lastName, phone, date0fBirth, gender);
//    }
}
