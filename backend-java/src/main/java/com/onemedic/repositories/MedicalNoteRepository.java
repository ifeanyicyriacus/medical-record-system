package com.onemedic.repositories;

import com.onemedic.models.MedicalRecord;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MedicalNoteRepository extends MongoRepository<MedicalRecord.MedicalNote, String> {
}
