package com.onemedic.controllers;

import com.onemedic.services.SuperAdminService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/admins")
public class AdminController {
    private final SuperAdminService superAdminService;
    public AdminController(SuperAdminService superAdminService) {
        this.superAdminService = superAdminService;
    }


}
