package com.onemedic.services.impl;

import com.onemedic.models.Appointment;
import com.onemedic.models.User;

public class Updater {

    static void updateUser(User user, User newUserDetails) {
        user.setEmail(newUserDetails.getEmail());
        user.setFirstName(newUserDetails.getFirstName());
        user.setLastName(newUserDetails.getLastName());
        user.setGender(newUserDetails.getGender());
        user.setDate0fBirth(newUserDetails.getDate0fBirth());
        user.setPhoneNumber(newUserDetails.getPhoneNumber());
    }

    public static void updateAppointment(Appointment appointment, Appointment appointmentDetails) {
        appointment.setStatus(appointmentDetails.getStatus());
        appointment.setRemark(appointmentDetails.getRemark());
    }
}
