package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;

import java.time.LocalDate;

@Data
public class MedicalNote {
    @Id
    private String    id;
    private String    primaryComplaint;
    private String    otherComplaint;
    private String    vitals;
    private String    observations;
    private String    primaryDiagnosis;
    private String    doctorId;
    private LocalDate noteDate;
}
