package com.onemedic.repositories;

import com.onemedic.models.Clinician;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface DoctorRepository extends MongoRepository<Clinician, String> {
}
