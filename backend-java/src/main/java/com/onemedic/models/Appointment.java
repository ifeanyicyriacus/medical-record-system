package com.onemedic.models;

import lombok.Data;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDate;

@Document(collection = "appointments")
@Data
public class Appointment {
    @Indexed(unique = true)
    private String            patientId;
    @Indexed(unique = true)
    private String            clinicianId;
    private AppointmentStatus status;
    private String            remark;
    private LocalDate         date; //a time in the future
}
