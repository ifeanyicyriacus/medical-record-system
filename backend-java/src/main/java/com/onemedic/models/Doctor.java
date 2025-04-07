package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;


@Data
@Document(collection = "doctors")
public class Doctor extends User {

    @Id
    private String            id;
    private Specialization    specialization;
    private List<Appointment> appointment;
}
