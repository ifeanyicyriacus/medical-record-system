package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document(collection = "clinicians")
public class Clinician extends User {

    @Id
    private String         id;
    private String         licenseNumber;
    private Specialization specialization;
}
