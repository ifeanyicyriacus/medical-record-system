package com.onemedic.repositories;

import com.onemedic.models.MedicalNote;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MedicalNoteRepository extends MongoRepository<MedicalNote, String> {
}
