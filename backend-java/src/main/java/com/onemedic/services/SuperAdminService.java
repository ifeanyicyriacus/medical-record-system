package com.onemedic.services;


import com.onemedic.models.Admin;

public interface SuperAdminService {
    void createSuperAdminIfNotExist(String email, String password, String role);
    Admin createAdmin(Admin admin);
}
