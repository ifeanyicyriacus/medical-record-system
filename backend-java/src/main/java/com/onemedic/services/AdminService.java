package com.onemedic.services;

public interface AdminService {
    void createSuperAdminIfNotExist(String email, String password, String role);
}
