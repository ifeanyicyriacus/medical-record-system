package com.onemedic.controllers;

import com.onemedic.services.ClinicianService;
import com.onemedic.services.impl.ClinicianServiceImpl;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/clinicians")
public class ClinicianController {
    private ClinicianService clinicianService;

    public ClinicianController(ClinicianServiceImpl clinicianService) {
        this.clinicianService = clinicianService;
    }

}
