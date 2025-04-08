package com.onemedic.services.impl;

import com.onemedic.dtos.requests.auth.LoginDto;
import com.onemedic.dtos.responses.auth.AuthResponse;
import com.onemedic.security.jwt.JwtUtils;
import com.onemedic.security.services.UnifiedUserDetailsService;
import com.onemedic.services.AuthenticationService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthenticationServiceImpl implements AuthenticationService {
    private final JwtUtils              jwtUtils;
    private final AuthenticationManager authenticationManager;

    @Override
    public AuthResponse login(LoginDto loginDto) {

        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        loginDto.getEmail(),
                        loginDto.getPassword()
                )
        );
        SecurityContextHolder.getContext().setAuthentication(authentication);
        UserDetails userDetails = (UserDetails) authentication.getPrincipal();

        String jwt = jwtUtils.generateToken(userDetails);
        UnifiedUserDetailsService.AuthUser authUser =
                (UnifiedUserDetailsService.AuthUser) userDetails;

        return ResponseEntity.ok(new AuthResponse(
                jwt,
                authUser.id(),
                authUser.email(),
                authUser.userType().name()
        )).getBody();
    }

}
