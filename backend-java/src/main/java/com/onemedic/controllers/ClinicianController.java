package com.onemedic.controllers;

import com.onemedic.models.Clinician;
import com.onemedic.services.ClinicianService;
import com.onemedic.services.ClinicianServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/doctors")
public class ClinicianController {
    private ClinicianService clinicianService;

    public ClinicianController(ClinicianServiceImpl clinicianService) {
        this.clinicianService = clinicianService;
    }

    @GetMapping
    public Page<Clinician> getAllClinicians(Pageable pageable) {
        return clinicianService.getAllPatients(pageable);
    }
}
