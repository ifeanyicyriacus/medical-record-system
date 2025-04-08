package com.onemedic.services;

import com.onemedic.models.Patient;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface PatientService {
    Patient createPatient(Patient patient);
    Patient getPatient(String id);
//    Patient updatePatient(Patient patient);
    Page<Patient> getAllPatients(Pageable pageable);
}
