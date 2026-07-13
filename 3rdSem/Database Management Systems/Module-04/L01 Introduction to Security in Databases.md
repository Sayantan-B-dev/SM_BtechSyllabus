# Introduction to Security in Databases

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 1  
**Date:** 01-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Why Database Security?

Databases store the most valuable asset of an organization: its data. This includes customer records, financial transactions, intellectual property, employee details, and strategic plans. A breach can lead to financial loss, legal liability, reputational damage, and regulatory penalties. Database security is the practice of protecting the database from unauthorized access, misuse, corruption, or destruction.

## Security Threats

### 1. Unauthorized Access
An attacker gains access to data they are not permitted to see. This can happen through weak passwords, stolen credentials, or exploiting vulnerabilities in the application layer.

### 2. SQL Injection
A code injection technique where an attacker inserts malicious SQL statements into an input field. If the application does not properly sanitize inputs, the injected SQL is executed by the database.

Example: An attacker types `' OR '1'='1` into a login form. The resulting query becomes:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '';
```

This bypasses authentication because `'1'='1'` is always true.

### 3. Data Modification (Tampering)
Unauthorized changes to data. An attacker may alter financial records, grades, or transaction histories. Integrity is lost.

### 4. Denial of Service (DoS)
An attacker overwhelms the database server with requests, causing it to become unavailable to legitimate users. This can be done through resource exhaustion (CPU, memory, disk I/O) or by crashing the database process.

### 5. Privilege Escalation
A user with limited privileges exploits a bug or misconfiguration to gain higher-level access (e.g., a regular employee becomes an administrator). Once elevated, the attacker can read, modify, or delete any data.

## Security Goals: The CIA Triad

The three fundamental pillars of information security:

```
+---------------------+-----------------------------------------------+
| Confidentiality     | Data is accessible only to authorized users.  |
|                     | Ensured by authentication, authorization, and |
|                     | encryption.                                    |
+---------------------+-----------------------------------------------+
| Integrity           | Data is accurate and has not been tampered    |
|                     | with. Ensured by access controls, checksums,  |
|                     | and audit trails.                              |
+---------------------+-----------------------------------------------+
| Availability        | Data and the system are accessible when       |
|                     | needed. Ensured by redundancy, backups, and   |
|                     | DoS protection.                                |
+---------------------+-----------------------------------------------+
```

### Confidentiality
- Only authorized subjects (users, processes) can read data.
- Enforced through authentication (verifying identity) and authorization (checking permissions).
- Encryption protects data even if access controls are bypassed.

### Integrity
- Data is not modified by unauthorized parties.
- Mechanisms: access controls, constraints (PRIMARY KEY, FOREIGN KEY, CHECK), audit logs, checksums.
- Ensures that data remains correct and consistent.

### Availability
- The database system is operational and responsive when needed.
- Threats: DoS attacks, hardware failures, natural disasters, power outages.
- Mitigations: failover clusters, RAID, backups, load balancing.

## Security Layers

Database security operates at multiple layers. Each layer provides a line of defense:

```
+---------------------------+
|      Physical Layer       |  Locks on server room doors,
|                           |  biometric access, CCTV,
|                           |  fire suppression.
+---------------------------+
|      Network Layer        |  Firewalls, VPNs, network
|                           |  segmentation, intrusion
|                           |  detection systems (IDS).
+---------------------------+
|      OS Layer             |  Operating system hardening,
|                           |  file permissions, OS-level
|                           |  authentication, patching.
+---------------------------+
|      DBMS Layer           |  User accounts, privileges,
|                           |  encryption, audit logging,
|                           |  views, stored procedures.
+---------------------------+
```

### 1. Physical Security
Protects the hardware on which the database runs. If an attacker gains physical access to the server, they can steal hard drives, bypass software controls, or install keyloggers. Measures include locked server rooms, badge access, video surveillance, and environmental controls.

### 2. Network Security
Controls what traffic reaches the database server. The database should never be directly exposed to the internet. Firewalls allow only specific IP addresses and ports. A VPN encrypts traffic between the application and the database. An intrusion detection system (IDS) monitors for suspicious patterns.

### 3. Operating System Security
The OS must be hardened: unnecessary services disabled, file permissions set correctly, regular security patches applied. The database files on disk should be readable only by the database service account.

### 4. DBMS Security
The core focus of this module. Includes:
- **Authentication:** Verifying who the user is.
- **Authorization:** Determining what the user can do.
- **Auditing:** Recording what the user did.
- **Encryption:** Protecting data at rest and in transit.
- **Views:** Restricting access to specific columns or rows.
- **Stored Procedures:** Encapsulating logic and preventing direct table access.

## Defense in Depth

No single security measure is sufficient. Defense in depth means layering multiple controls so that if one fails, another still provides protection. For example:

1. A firewall blocks unauthorized network traffic (network layer).
2. The OS requires authentication (OS layer).
3. The DBMS requires a valid database account (DBMS layer).
4. The application validates input to prevent SQL injection (application layer).
5. Sensitive columns are encrypted (DBMS layer).
6. All queries are logged for auditing (DBMS layer).

## Summary

- Database security is essential because data is valuable.
- Major threats: unauthorized access, SQL injection, tampering, DoS, privilege escalation.
- CIA triad: Confidentiality, Integrity, Availability.
- Security operates at four layers: physical, network, OS, and DBMS.
- Defense in depth uses multiple overlapping controls.

---

## Practice Problems

1. Explain the CIA triad with a real-world example for each principle.
2. List five types of threats to database security and describe how each one can cause damage.
3. Draw a layered security diagram and explain the role of each layer.
4. What is defense in depth? Why is a single security measure insufficient?
5. Give an example of how a privilege escalation attack could occur in a poorly configured database system.
