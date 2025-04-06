package com.onemedic.repositories;

import com.onemedic.models.SystemLog;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface SystemLogRepository extends MongoRepository<SystemLog, String> {
}
