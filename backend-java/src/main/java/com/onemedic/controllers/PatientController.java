package com.onemedic.controllers;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.services.impl.PatientServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/api/patients/{id}")
public class PatientController {

    private final PatientServiceImpl patientService;

    public PatientController(PatientServiceImpl patientService) {
        this.patientService = patientService;
    }

    @PostMapping("/appointments")
    public Appointment createAppointment(@PathVariable String id, @RequestBody Appointment appointment) {
        return patientService.createAppointment(appointment);
    }

    @PutMapping("/appointments/{appointmentId}")
    public Appointment updateAppointment(@PathVariable String id, @PathVariable String appointmentId, @RequestBody Appointment appointmentDetails) {
        return patientService.updateAppointment(appointmentId, appointmentDetails);
    }

    @GetMapping("/appointments")
    public Page<Appointment> getAllMyAppointments(@PathVariable String id, Pageable pageable) {
        return patientService.getAllMyAppointments(id, pageable);
    }

    @GetMapping("/medical-record")
    public MedicalRecord getMedicalRecord(@PathVariable String id) {
        return patientService.getMedicalRecord(id);
    }
}
//how to expose DTOs