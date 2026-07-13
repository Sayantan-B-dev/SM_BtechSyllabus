# Case Study on Database Breaches

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 6  
**Date:** 15-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction

Real-world database breaches provide critical lessons for understanding security failures and designing robust defenses. This lecture examines four major breaches, their root causes, and the preventive measures that could have stopped them.

---

## 1. Sony PlayStation Network Breach (2011)

### Overview
- **Date:** April 2011
- **Impact:** 77 million user accounts compromised.
- **Data exposed:** Names, addresses, email addresses, birth dates, login credentials, and (potentially) credit card numbers.
- **Cost:** Estimated $171 million in remediation and lost revenue.

### How It Happened
- Attackers exploited a vulnerability in the Apache web server software running on Sony's network.
- They used SQL injection to bypass authentication on the Sony PSN website.
- Once inside, they escalated privileges and gained access to the application server.
- From the application server, they accessed the backend database containing user credentials.
- Passwords were stored using MD5 hashing (a weak, broken algorithm) without salting, making them easy to crack.
- The database was not segmented -- all user data (personal + financial) was in one database.

### Root Causes
- SQL injection vulnerability in the web application.
- Outdated and unpatched Apache server.
- Weak password hashing (MD5 without salt).
- No network segmentation -- application and database servers were on the same flat network.
- Lack of encryption for sensitive data at rest.

### Lessons Learned
- Use parameterized queries (prepared statements) to prevent SQL injection.
- Keep all software patched and up to date.
- Use strong, salted hashing algorithms (bcrypt, Argon2) for passwords.
- Segment networks: application server and database server should be in separate zones.
- Encrypt sensitive data at rest.
- Implement monitoring to detect unusual access patterns.

---

## 2. Equifax Data Breach (2017)

### Overview
- **Date:** July 2017 (disclosed September 2017)
- **Impact:** 147.9 million people affected.
- **Data exposed:** Social Security numbers, birth dates, addresses, driver's license numbers, credit card numbers.
- **Cost:** Over $1.4 billion in settlements and fines.

### How It Happened
- Equifax ran an Apache Struts web framework (CVE-2017-5638) that had a critical remote code execution vulnerability.
- A patch was available in March 2017. Equifax failed to apply it.
- Attackers scanned the internet, found the unpatched server, and exploited the vulnerability.
- They gained access to the dispute portal web application.
- From the web application, they moved laterally across the network to reach a database containing massive amounts of sensitive personal data.
- Data was exfiltrated over 76 days without detection.
- Communication between the database server and internal systems was unencrypted.

### Root Causes
- Failure to patch a known vulnerability (patch was available two months before the attack).
- Poor network segmentation -- attackers moved from the web tier to the data tier.
- Lack of encryption for data in transit.
- Inadequate monitoring -- the breach went undetected for 76 days.
- Excessive data retention -- holding data that was no longer needed.

### Lessons Learned
- A patch management policy is critical. Critical patches must be applied within days, not months.
- Implement network segmentation and strict firewall rules between tiers.
- Encrypt all sensitive data in transit (TLS) and at rest.
- Deploy intrusion detection and SIEM systems with real-time alerting.
- Practice data minimization: only retain data needed for business purposes.
- Use database activity monitoring (DAM) to detect anomalous queries.

---

## 3. Facebook / Cambridge Analytica (2018)

### Overview
- **Date:** March 2018 (revealed)
- **Impact:** 87 million Facebook user profiles harvested.
- **Data exposed:** Profile data, likes, friend networks, private messages of some users.
- **Cost:** $5 billion FTC fine, massive reputational damage, and stock price drop.

### How It Happened
- A Cambridge University researcher, Aleksandr Kogan, created a personality quiz app on Facebook.
- Facebook's API allowed the app to collect data not only on the user who installed it but also on the user's entire friend network (approximately 300,000 users installed the app, yielding data on 87 million people).
- This data was sold to Cambridge Analytica, a political consulting firm.
- The data was used to build psychological profiles for targeted political advertising in the 2016 US election and Brexit referendum.
- The breach was not a technical hack but an abuse of authorized API access -- an insider threat facilitated by weak access control policies.

### Root Causes
- Overly permissive API: apps could access friends' data without their consent.
- Weak access control policies at Facebook.
- Lack of enforcement of data usage policies.
- No technical controls to prevent data exfiltration via API.
- Insider threat: a trusted researcher abused authorized access.

### Lessons Learned
- Apply the principle of least privilege to API access: apps should only access data they absolutely need.
- Implement data access governance: know who has access to what data and why.
- Use API rate limiting and anomaly detection to identify data scraping.
- Enforce data usage policies with technical controls (not just terms of service).
- Audit third-party access regularly.
- Users must give explicit consent for their data to be shared with third parties (GDPR principles).

---

## 4. Marriott International / Starwood (2018)

### Overview
- **Date:** November 2018 (disclosed)
- **Impact:** Up to 500 million guest records compromised.
- **Data exposed:** Names, addresses, phone numbers, email addresses, passport numbers, credit card details, travel history.
- **Cost:** $123 million GDPR fine, $52 million FTC settlement, class-action lawsuits.

### How It Happened
- Marriott acquired Starwood Hotels in 2016. Starwood's reservation database was already compromised before the acquisition.
- Attackers had been present in the Starwood network since 2014.
- They gained access to the Starwood reservation database using administrative credentials stolen via phishing or malware.
- Database contained records of guests at Starwood properties worldwide.
- The breach was discovered in 2018 when Marriott's security tools detected an attempted access through Starwood's systems.
- Because the systems were not integrated post-acquisition, the compromised legacy system remained unsecured.

### Root Causes
- Insufficient due diligence during acquisition: Starwood's security weaknesses were not discovered.
- Use of legacy, unsecured systems post-acquisition.
- Stolen administrative credentials (phishing/social engineering).
- Lack of encryption for passport numbers and other sensitive fields.
- Inadequate monitoring of internal database access.

### Lessons Learned
- Security due diligence is mandatory during mergers and acquisitions.
- Legacy systems must be remediated or isolated as part of integration.
- Use multi-factor authentication for all administrative accounts.
- Encrypt all personally identifiable information (PII), especially passport numbers.
- Implement continuous monitoring and behavioral analytics.
- Prepare an incident response plan in advance.

---

## Summary Table

| Breach              | Year | Records Affected | Root Cause(s)                               | Primary Lesson                               |
|---------------------|------|------------------|---------------------------------------------|----------------------------------------------|
| Sony PSN            | 2011 | 77 million       | SQL injection, weak hashing, flat network   | Parameterized queries, encryption, patching  |
| Equifax             | 2017 | 148 million      | Unpatched Apache Struts, no segmentation    | Patch management, network segmentation       |
| Cambridge Analytica | 2018 | 87 million       | Overly permissive API, insider abuse        | Least privilege on APIs, data governance     |
| Marriott/Starwood   | 2018 | 500 million      | Legacy system, stolen admin creds           | Security due diligence in M&A, MFA           |

## Common Themes Across All Breaches

1. **SQL Injection and unpatched software** remain the most common entry points.
2. **Weak access controls** (overly permissive accounts or APIs) enable lateral movement and escalation.
3. **Lack of encryption** leaves exposed data readable.
4. **Inadequate monitoring** allows attackers to remain undetected for months or years.
5. **Poor credential management** (weak passwords, no MFA) facilitates unauthorized access.

## Prevention Measures Summary

- SQL Injection: use parameterized queries, input validation, stored procedures.
- Patching: implement a formal patch management process with SLAs for critical patches.
- Encryption: encrypt data at rest (TDE, column-level) and in transit (TLS).
- Access control: enforce least privilege, use RBAC, implement MFA.
- Monitoring: deploy database activity monitoring (DAM), SIEM, and user behavior analytics (UBA).
- Network: segment networks, use firewalls, never expose databases directly.
- Backup and recovery: regular backups, test restoration procedures.
- Incident response: have a documented, tested incident response plan.

---

## Practice Problems

1. Describe the Sony PSN breach. What was the entry point and what three security failures allowed it to succeed?
2. The Equifax breach cost over $1.4 billion. What single action could have prevented the entire incident? Justify your answer.
3. Was the Cambridge Analytica incident a "hack" in the traditional sense? Why or why not? What access control concept was violated?
4. List three common root causes shared by at least three of the four breaches discussed.
5. Prepare a list of 5 specific database security controls that would have mitigated the Marriott breach.
