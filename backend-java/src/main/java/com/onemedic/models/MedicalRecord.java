package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDate;
import java.util.List;

@Data
@Document(collection = "medical_records")
public class MedicalRecord {
    @Id
    private String id;
    private final List<MedicalNote> medicalNotes;

    @Data
    @Document(collection = "medical_notes")
    public static class MedicalNote {
        @Id
        private String    id;
        @Indexed(unique = false)
        private final String    doctorId;
        private final String    primaryComplaint;
        private final String    otherComplaint;
        private final String    vitals;
        private final String    observations;
        private final String    primaryDiagnosis;
        private final LocalDate date = LocalDate.now();

    }
}


