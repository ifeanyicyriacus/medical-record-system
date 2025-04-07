package com.onemedic;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class OneMedicApplication {
    public static void main(String[] args) {
        SpringApplication.run(OneMedicApplication.class, args);
        initialiseTheSuperAdmin();
    }

    private static void initialiseTheSuperAdmin() {

    }
}