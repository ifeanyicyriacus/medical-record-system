package com.onemedic.dtos.responses;

import lombok.Data;

@Data
final public class ChangePasswordResponseDto {
    private boolean success;
    private String message;
}
