package com.onemedic.services;

import com.onemedic.models.Appointment;
import com.onemedic.models.Clinician;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface AdminService {
    Clinician createClinician(Clinician clinician);
    Page<Clinician> getAllClinicians(Pageable pageable);
    Clinician getClinicianById(String id);
    Clinician getClinicianByEmail(String email);
    Clinician updateClinician(String id, Clinician clinicianDetails);
    Page<Appointment> getAllAppointments(Pageable pageable);
    Page<Appointment> getAllAppointmentsByClinicianId(String clinicianId, Pageable pageable);
}
