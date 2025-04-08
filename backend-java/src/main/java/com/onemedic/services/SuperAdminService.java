package com.onemedic.services;


import com.onemedic.models.Admin;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface SuperAdminService {
    void createSuperAdminIfNotExists(String email, String password);
    Admin createAdmin(Admin admin);
    Page<Admin> getAllAdmins(Pageable pageable);
    Admin updateAdmin(String id, Admin admin);
    Admin getAdminByEmail(String email);
    Admin getAdminById(String id);
//    void deactivateById(String id);
//    void reactivateById(String id);
}
