package com.onemedic.controllers;

import com.onemedic.models.Admin;
import com.onemedic.services.SuperAdminService;
import com.onemedic.services.impl.SuperAdminServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/sudo/{id}")
public class SuperAdminController {
    private final SuperAdminService superAdminService;

    public SuperAdminController(SuperAdminServiceImpl superAdminService) {
        this.superAdminService = superAdminService;
    }

    @GetMapping
    public Page<Admin> getAllAdmins(Pageable pageable, @PathVariable String id) {
        return this.superAdminService.getAllAdmins(pageable);
    }

    @GetMapping("/{adminId}")
    public Admin getAdmin(@PathVariable String id, @PathVariable String adminId) {
        return superAdminService.getAdminById(adminId);
    }

    @GetMapping("/{email}")
    public Admin getAdminByEmail(@PathVariable String email, @PathVariable String id) {
        return superAdminService.getAdminByEmail(email);
    }

    @PostMapping
    public Admin createAdmin(@RequestBody Admin admin) {
        return superAdminService.createAdmin(admin);
    }

    @PutMapping("/{adminId}")
    public Admin updateAdmin(@PathVariable String id, @PathVariable String adminId,
                             @RequestBody Admin adminDetails) {
        return superAdminService.updateAdmin(adminId, adminDetails);
    }
//    Start Mapping Logs Here (Log has Only get request)
}
