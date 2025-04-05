package com.onemedic.services;

import com.onemedic.models.Admin;
import com.onemedic.models.Clinician;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface AdminService {
    Clinician createClinician(Clinician clinician);
    Page<Clinician> getAllClinicians(Pageable pageable);
    Clinician getClinicianById(String id);
    Clinician getByEmail(String email);
    Clinician updateClinician(Clinician clinician);
    Admin updateAdmin(Admin admin);
    Admin getAdminByEmail(String email);
    Admin getAdminById(String id);
}
