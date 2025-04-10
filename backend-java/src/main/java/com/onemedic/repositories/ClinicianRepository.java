package com.onemedic.repositories;

import com.onemedic.models.Clinician;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface ClinicianRepository extends MongoRepository<Clinician, String> {
    Optional<Clinician> findByEmail(String email);
}
