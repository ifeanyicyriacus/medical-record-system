package com.onemedic.controllers;

import com.onemedic.models.Clinician;
import com.onemedic.services.AdminService;
import com.onemedic.services.impl.AdminServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/admins/{id}/clinicians")
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
    public Page<Clinician> getAllClinicians(Pageable pageable, @PathVariable String id) {
        return adminService.getAllClinicians(pageable);
    }

    @GetMapping("?id={clinicianId}")
    public Clinician getClinicianById(@PathVariable String id, @PathVariable String clinicianId) {
        return adminService.getClinicianById(clinicianId);
    }

    @GetMapping("?email={email}")
    public Clinician getClinicianByEmail(@PathVariable String email, @PathVariable String id) {
        return adminService.getClinicianByEmail(email);
    }

    @PutMapping("/{clinicianId}")
    public Clinician updateClinician(@PathVariable String id, @PathVariable String clinicianId,
                                     @RequestBody Clinician clinicianDetails) {
        return adminService.updateClinician(clinicianId, clinicianDetails);
    }
}
