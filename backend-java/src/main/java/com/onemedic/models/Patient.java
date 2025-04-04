package com.onemedic.models;
import lombok.Data;
import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;


//@Getter
@Data
@Document(collection = "patients")
public class Patient extends User {

    @Id
    private String id;
    private final List<Appointment> appointment;
    private final List<MedicalNote> medicalNotes;

//    public Patient(String email, String password, String firstName, String lastName, String phone, LocalDate date0fBirth, Gender gender) {
//        super(email, password, firstName, lastName, phone, date0fBirth, gender);
//        this.appointment = new ArrayList<>();
//        this.medicalNotes = new ArrayList<>();
//    }
}

