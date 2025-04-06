package com.onemedic.models;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Data
@Document(collection = "system-logs")
public class SystemLog {
    @Id
    private final String        id;
    private final UserType      userType;
    private final String        userId;
    private final String        message;
    private final LocalDateTime dateTime = LocalDateTime.now();
}
