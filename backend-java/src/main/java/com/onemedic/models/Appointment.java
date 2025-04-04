package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDate;

@Document(collection = "appointments")
@Data
public class Appointment {
    @Id
    private String            id;
    private String            patientId;
    private String            clinicianId;
    private AppointmentStatus status;
    private LocalDate         date; //a time in the future
}
