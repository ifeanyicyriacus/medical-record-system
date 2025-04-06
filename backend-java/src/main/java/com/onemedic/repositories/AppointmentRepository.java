package com.onemedic.repositories;

import com.onemedic.models.Appointment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface AppointmentRepository extends MongoRepository<Appointment, String> {
    Page<Appointment> findAllByClinicianId(String clinicianId, Pageable pageable);
    Page<Appointment> findAllByPatientId(String patientId, Pageable pageable);
}
