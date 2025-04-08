package com.onemedic.controllers;

import com.onemedic.models.Appointment;
import com.onemedic.models.MedicalRecord;
import com.onemedic.models.Patient;
import com.onemedic.services.ClinicianService;
import com.onemedic.services.impl.ClinicianServiceImpl;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/clinicians/{id}")
public class ClinicianController {
    private final ClinicianService clinicianService;

    public ClinicianController(ClinicianServiceImpl clinicianService) {
        this.clinicianService = clinicianService;
    }

    @PostMapping("/patients")
    public Patient createPatient(@PathVariable String id, @RequestBody Patient patient) {
        return clinicianService.createPatient(patient);
    }

    @GetMapping("/patients")
    public Page<Patient> getAllPatients(Pageable pageable, @PathVariable String id) {
        return clinicianService.getAllPatients(pageable);
    }

    @PutMapping("/patients/{patientId}")
    public Patient updatePatient(@PathVariable String id, @PathVariable String patientId, @RequestBody Patient patientDetails) {
        return clinicianService.updatePatient(patientId, patientDetails);
    }

    @GetMapping("/patients?id={patientId}")
    public Patient getPatientById(@PathVariable String id, @PathVariable String patientId) {
        return clinicianService.getPatientById(patientId);
    }

    @GetMapping("/patients?email={email}")
    public Patient getPatientByEmail(@PathVariable String id, @PathVariable String email) {
        return clinicianService.getPatientByEmail(email);
    }




    @PostMapping("/appointments")
    public Appointment createAppointment(@PathVariable String id, @RequestBody Appointment appointment) {
        return clinicianService.createAppointment(appointment);
    }

    @PutMapping("/appointments/{appointmentId}")
    public Appointment updateAppointment(@PathVariable String id, @PathVariable String appointmentId,
                                         @RequestBody Appointment appointment) {
        return clinicianService.updateAppointment(appointmentId, appointment);
    }

    @GetMapping("/appointments")
    public Page<Appointment> getAllAppointments(@PathVariable String id, Pageable pageable) {
        return clinicianService.getAllAppointments(pageable);
    }

    @GetMapping("/appointments")
    public Page<Appointment> getAllAppointmentsByClinicianId(@PathVariable String id, Pageable pageable) {
        return clinicianService.getAllMyAppointmentsByClinicianId(id, pageable);
    }



    @GetMapping("/medical-records/{patientId}")
    public MedicalRecord getPatientMedicalRecord(@PathVariable String id, @PathVariable String patientId) {
        return clinicianService.getPatientMedicalRecord(patientId);
    }

    @PutMapping("/medical-records/{patientId}")
    public MedicalRecord.MedicalNote addNoteToMedicalRecord(@PathVariable String id, @PathVariable String patientId,
                                                            MedicalRecord.MedicalNote medicalNote) {
        return clinicianService.addMedicalNoteToRecord(patientId, medicalNote);
    }
}
