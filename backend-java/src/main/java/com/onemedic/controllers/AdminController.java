package com.onemedic.controllers;

import com.onemedic.models.Clinician;
import com.onemedic.services.AdminService;
import com.onemedic.services.impl.AdminServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/clinicians")
public class AdminController {
    private final AdminService adminService;

    public AdminController(AdminServiceImpl adminService) {
        this.adminService = adminService;
    }

    @PostMapping
    public Clinician createClinician(@RequestBody Clinician clinician) {
        return adminService.createClinician(clinician);
    }

    @GetMapping
    public Page<Clinician> getAllClinicians(Pageable pageable) {
        return adminService.getAllClinicians(pageable);
    }

    @GetMapping("/{id}")
    public Clinician getClinicianById(@PathVariable String id) {
        return adminService.getClinicianById(id);
    }

    @GetMapping("/{email}")
    public Clinician getClinicianByEmail(@PathVariable String email) {
        return adminService.getClinicianByEmail(email);
    }

    @PutMapping("/{id}")
    public Clinician updateClinician(@PathVariable String id,
                                     @RequestBody Clinician clinicianDetails) {
        return adminService.updateClinician(id, clinicianDetails);
    }
}
