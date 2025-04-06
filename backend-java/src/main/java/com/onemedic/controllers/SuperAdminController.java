package com.onemedic.controllers;

import com.onemedic.models.Admin;
import com.onemedic.services.SuperAdminService;
import com.onemedic.services.impl.SuperAdminServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/admins")
public class SuperAdminController {
    private final SuperAdminService superAdminService;

    public SuperAdminController(SuperAdminServiceImpl superAdminService) {
        this.superAdminService = superAdminService;
    }

    @GetMapping
    public Page<Admin> getAllAdmins(Pageable pageable) {
        return this.superAdminService.getAllAdmins(pageable);
    }

    @GetMapping("/{id}")
    public Admin getAdmin(@PathVariable String id) {
        return superAdminService.getAdminById(id);
    }

    @GetMapping("/{email}")
    public Admin getAdminByEmail(@PathVariable String email) {
        return superAdminService.getAdminByEmail(email);
    }

    @PostMapping
    public Admin createAdmin(@RequestBody Admin admin) {
        return superAdminService.createAdmin(admin);
    }

    @PutMapping("/{id}")
    public Admin updateAdmin(@PathVariable String id, @RequestBody Admin adminDetails) {
        return superAdminService.updateAdmin(id, adminDetails);
    }

    @DeleteMapping("{id}")
    public void deleteAdmin(@PathVariable String id) {
        superAdminService.deleteById(id);
    }
}
