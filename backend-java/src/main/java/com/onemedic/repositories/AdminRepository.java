package com.onemedic.repositories;

import com.onemedic.models.Admin;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface AdminRepository extends MongoRepository<Admin, String> {
    boolean existsByEmail(String email);
    Optional<Admin> findByEmail(String email);
}
