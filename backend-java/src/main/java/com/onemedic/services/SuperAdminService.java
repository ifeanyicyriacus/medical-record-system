package com.onemedic.services;


import com.onemedic.models.Admin;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface SuperAdminService {
    void createSuperAdminIfNotExist(String email, String password, String role);
    Admin createAdmin(Admin admin);
    Page<Admin> getAdmins(Pageable pageable);
}
