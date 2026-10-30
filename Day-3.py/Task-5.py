# Assignment 5: Network Security Log Analyzer  


# Sample Input:  

security_logs = [  
"2024-01-15 09:15:23 | LOGIN_SUCCESS | user1@company.com | 192.168.1.10 | OFFICE",  
"2024-01-15 09:16:45 | LOGIN_FAILED | admin@company.com | 203.45.67.89 | EXTERNAL",  
"2024-01-15 09:17:12 | LOGIN_FAILED | admin@company.com | 203.45.67.89 | EXTERNAL",  
"2024-01-15 09:17:45 | LOGIN_FAILED | admin@company.com | 203.45.67.89 | EXTERNAL",  
"2024-01-15 09:18:01 | LOGIN_FAILED | root@company.com | 203.45.67.89 | EXTERNAL",  
"2024-01-15 14:30:22 | LOGIN_SUCCESS | user2@company.com | 192.168.1.25 | OFFICE",  
"2024-01-15 23:45:15 | LOGIN_SUCCESS | admin@company.com | 10.0.0.100 | VPN",  
"2024-01-15 23:46:33 | DATA_ACCESS | admin@company.com | 10.0.0.100 | DATABASE",  
"2024-01-15 02:15:44 | LOGIN_FAILED | guest@company.com | 156.78.90.123 | EXTERNAL",  
"2024-01-15 02:16:12 | LOGIN_FAILED | guest@company.com | 156.78.90.123 | EXTERNAL" 
] 
suspicious_ips = {"203.45.67.89", "156.78.90.123"}  
office_hours = {"09", "10", "11", "12", "13", "14", "15", "16", "17"}  
critical_accounts = {"admin@company.com", "root@company.com"} 

# 1. Identify suspicious IP addresses and access patterns  

suspicious_access_logs = []
for log in security_logs:
    log_parts = log.split(" | ")
    timestamp = log_parts[0]
    event_type = log_parts[1]
    user_email = log_parts[2]
    ip_address = log_parts[3]
    location = log_parts[4]

    if ip_address in suspicious_ips:
        suspicious_access_logs.append(log)
        print(f"Suspicious Access Detected: {log}")

# 2. Track failed login attempts and potential brute force attacks 


failed_login_attempts = []
for log in security_logs:
    log_parts = log.split(" | ")
    timestamp = log_parts[0]
    event_type = log_parts[1]
    user_email = log_parts[2]
    ip_address = log_parts[3]
    location = log_parts[4]

    if event_type == "LOGIN_FAILED":
        failed_login_attempts.append(log)
        print(f"Failed Login Attempt Detected: {log}")


# 3. Monitor unusual access times and frequency 

unusual_access_logs = []
for log in security_logs:
    log_parts = log.split(" | ")
    timestamp = log_parts[0]
    event_type = log_parts[1]
    user_email = log_parts[2]
    ip_address = log_parts[3]
    location = log_parts[4]

    hour = timestamp.split(" ")[1].split(":")[0]
    if hour not in office_hours:
        unusual_access_logs.append(log)
        print(f"Unusual Access Time Detected: {log}")   

# 4. Generate security alerts and recommendations


security_alerts = []
for log in security_logs:
    log_parts = log.split(" | ")
    timestamp = log_parts[0]
    event_type = log_parts[1]
    user_email = log_parts[2]
    ip_address = log_parts[3]
    location = log_parts[4]

    if event_type == "LOGIN_FAILED" and user_email in critical_accounts:
        alert_message = f"ALERT: Critical account {user_email} had a failed login attempt from IP {ip_address} at {timestamp}"
        security_alerts.append(alert_message)
        print(alert_message)
        