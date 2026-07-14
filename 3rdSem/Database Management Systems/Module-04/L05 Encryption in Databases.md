# Encryption in Databases

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 5  
**Date:** 15-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Encryption?

Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) using an algorithm and a key. Only someone with the correct decryption key can convert the ciphertext back to plaintext. Encryption protects data confidentiality even if an attacker gains access to the storage medium.

```
Plaintext:  Hello World
               |
               v  [Encryption Algorithm + Key]
               |
Ciphertext:  aB3#kL9$pQ2...
               |
               v  [Decryption Algorithm + Key]
               |
Plaintext:  Hello World
```

## Symmetric Encryption

In symmetric encryption, the same key is used for both encryption and decryption.

**Algorithm:** AES (Advanced Encryption Standard) -- the most widely used symmetric algorithm. Key sizes: 128, 192, or 256 bits.

**How it works:**

```
Sender                               Receiver
  |                                     |
  |  Plaintext                          |
  |    |                                |
  |    v                                |
  |  Encrypt (AES + Key K)             |
  |    |                                |
  |    v                                |
  |  Ciphertext  ----Network--->   Ciphertext
  |                                |
  |                                v
  |                              Decrypt (AES + Key K)
  |                                |
  |                                v
  |                              Plaintext
```

**Advantages:** Fast, efficient for large data volumes.
**Disadvantage:** Key distribution problem -- both parties must securely share the key.

## Asymmetric Encryption

In asymmetric encryption, two mathematically related keys are used: a public key (for encryption) and a private key (for decryption).

**Algorithm:** RSA (Rivest-Shamir-Adleman), ECC (Elliptic Curve Cryptography).

**How it works:**

```
Sender                               Receiver
  |                                     |
  |  Plaintext                          |
  |    |                                |
  |    v                                |
  |  Encrypt (RSA + Receiver's         |
  |    Public Key)                      |
  |    |                                |
  |    v                                |
  |  Ciphertext  ----Network--->   Ciphertext
  |                                |
  |                                v
  |                              Decrypt (RSA + Receiver's
  |                                Private Key)
  |                                |
  |                                v
  |                              Plaintext
```

**Advantages:** No key distribution problem -- public keys can be shared openly.
**Disadvantage:** Much slower than symmetric encryption (100-1000x slower).

### Hybrid Approach

In practice, systems use hybrid encryption: asymmetric encryption to exchange a symmetric session key, then symmetric encryption for the actual data.

## Comparison: Symmetric vs Asymmetric

| Property              | Symmetric (AES)              | Asymmetric (RSA)           |
|-----------------------|------------------------------|----------------------------|
| Keys                  | Single shared key            | Public/private key pair    |
| Speed                 | Fast                         | Slow                       |
| Key distribution      | Problematic (must share key) | Easy (public key is open)  |
| Key length            | 128-256 bits                 | 2048-4096 bits             |
| Use case              | Bulk data encryption         | Key exchange, digital      |
|                       |                              | signatures                 |
| Security              | Very strong                  | Strong (with large keys)   |

## Data at Rest Encryption

Data at rest refers to data stored on disk (database files, backups, logs). If an attacker steals the hard drive, encryption ensures the data remains unreadable.

### Transparent Data Encryption (TDE)

TDE encrypts database files automatically at the file level. The DBMS handles encryption/decryption transparently -- applications see plaintext, but the data on disk is encrypted.

**How TDE works:**

```
Application
    |
    v
DBMS (decrypts on read, encrypts on write)
    |
    v
Disk (encrypted database files .mdf, .ndf, .ldf)
```

**Benefits:**
- No application changes required.
- Protects backup files and database files.
- Built into major DBMS (SQL Server, Oracle, MySQL).

**Enabling TDE in SQL Server:**

```sql
-- Create a master key
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'StrongMasterKey123';

-- Create a certificate
CREATE CERTIFICATE TDECert WITH SUBJECT = 'TDE Certificate';

-- Create a database encryption key
CREATE DATABASE ENCRYPTION KEY
WITH ALGORITHM = AES_256
ENCRYPTION BY SERVER CERTIFICATE TDECert;

-- Enable encryption
ALTER DATABASE SalesDB SET ENCRYPTION ON;
```

### File-Level Encryption

Encrypting the file system (e.g., BitLocker on Windows, LUKS on Linux). The OS encrypts entire volumes. The DBMS is unaware of the encryption.

## Data in Transit Encryption

Data in transit moves across the network between client and server. Without encryption, an attacker can sniff the network and capture data or credentials.

### SSL/TLS

SSL (Secure Sockets Layer) and its successor TLS (Transport Layer Security) encrypt the connection between the database client and server.

**How it works:**
1. Client connects to server; server presents its SSL certificate.
2. Client verifies the certificate against a trusted Certificate Authority (CA).
3. A symmetric session key is exchanged (using asymmetric encryption).
4. All subsequent communication is encrypted with the session key.

**Enforcing SSL in MySQL:**

```sql
-- Require SSL for a specific user account
ALTER USER 'alice'@'%' REQUIRE SSL;

-- Require SSL and a valid X.509 certificate
ALTER USER 'alice'@'%' REQUIRE X509;
```

**Enforcing Encryption in SQL Server (in connection string):**

```
Server=myServer;Database=myDB;Encrypt=yes;TrustServerCertificate=false;
```

## Column-Level Encryption

Column-level encryption encrypts specific columns within a table. Sensitive data (credit card numbers, social security numbers, medical records) can be encrypted while leaving non-sensitive columns in plaintext.

**Advantages:**
- Granular control: only sensitive data is encrypted.
- Different columns can use different keys.
- Even DBAs with full table access cannot read encrypted columns without the key.

**Disadvantages:**
- Cannot easily search or index encrypted columns.
- Application must manage keys.
- Performance overhead for encrypting/decrypting.

### Column Encryption in MySQL:

```sql
-- Encrypt data using AES
INSERT INTO customers (name, ssn)
VALUES ('Alice', AES_ENCRYPT('123-45-6789', 'encryption_key'));

-- Decrypt data
SELECT name, AES_DECRYPT(ssn, 'encryption_key') AS ssn
FROM customers;
```

### Column Encryption in SQL Server (Always Encrypted):

```sql
-- Create a column master key (CMK)
CREATE COLUMN MASTER KEY MyCMK
WITH (
    KEY_STORE_PROVIDER_NAME = 'MSSQL_CERTIFICATE_STORE',
    KEY_PATH = 'CurrentUser/My/...'
);

-- Create a column encryption key (CEK)
CREATE COLUMN ENCRYPTION KEY MyCEK
WITH VALUES (
    COLUMN_MASTER_KEY = MyCMK,
    ALGORITHM = 'RSA_OAEP',
    ENCRYPTED_VALUE = 0x01...
);

-- Create a table with an encrypted column
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100),
    ssn VARCHAR(11) ENCRYPTED WITH (
        ENCRYPTION_TYPE = DETERMINISTIC,
        ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256',
        COLUMN_ENCRYPTION_KEY = MyCEK
    )
);
```

## Hashing vs Encryption

Hashing is often confused with encryption, but they serve different purposes.

| Property          | Encryption                         | Hashing                              |
|-------------------|------------------------------------|--------------------------------------|
| Reversible?       | Yes (decrypt with key)             | No (one-way function)                |
| Output length     | Same as input (or slightly larger) | Fixed length (e.g., SHA-256 = 256b)  |
| Key required?     | Yes                                | No                                   |
| Purpose           | Confidentiality                    | Integrity verification, password     |
|                   |                                    | storage                              |
| Examples          | AES, RSA                           | SHA-256, MD5 (broken)                |
| Collision risk    | N/A                                | Possible (but negligible for good    |
|                   |                                    | hash functions)                      |

### Hashing Passwords

Passwords should never be stored in plaintext. Instead, store the hash. When a user logs in, hash the input and compare with the stored hash.

```sql
-- Store a hashed password
INSERT INTO users (username, password_hash)
VALUES ('alice', SHA2('mypassword', 256));

-- Verify login
SELECT * FROM users
WHERE username = 'alice'
  AND password_hash = SHA2('mypassword', 256);
```

**Important:** Use a salt (random value) with each password to prevent rainbow table attacks. Use algorithms like bcrypt, PBKDF2, or Argon2.

## Key Management

Encryption is only as secure as the key management.

**Best practices:**
- Store keys separately from the encrypted data (never on the same disk).
- Use a Hardware Security Module (HSM) or a key vault.
- Rotate keys periodically.
- Back up keys securely; losing the key means losing the data.
- Use different keys for different purposes (e.g., one key for TDE, another for column encryption).

---

## Practice Problems

1. Explain the difference between symmetric and asymmetric encryption. Give one advantage of each.
   <details>
   <summary>Show Answer</summary>
   **Symmetric encryption** uses the same key for encryption and decryption (e.g., AES). *Advantage:* Fast and efficient for large data. **Asymmetric encryption** uses a public-private key pair (e.g., RSA). *Advantage:* No need to share a secret key; the public key can be openly distributed.
   </details>
2. What is Transparent Data Encryption (TDE)? How does it differ from column-level encryption?
   <details>
   <summary>Show Answer</summary>
   TDE encrypts the entire database at the file level automatically; the database engine encrypts/decrypts data as it is written/read from disk, requiring no application changes. Column-level encryption encrypts only specific columns, giving finer control but requiring application-level key management and SQL functions (e.g., `AES_ENCRYPT()`/`AES_DECRYPT()`). TDE protects against physical theft of storage; column-level protects against unauthorized queries.
   </details>
3. Write SQL statements to encrypt a column `credit_card` in a `payments` table using AES in MySQL.
   <details>
   <summary>Show Answer</summary>
   ```sql
   CREATE TABLE payments (
       id INT PRIMARY KEY,
       customer_name VARCHAR(100),
       credit_card VARBINARY(256)
   );

   -- Insert encrypted data
   INSERT INTO payments (id, customer_name, credit_card)
   VALUES (1, 'John Doe', AES_ENCRYPT('4111-1111-1111-1111', 'encryption_key'));

   -- Read decrypted data
   SELECT id, customer_name, AES_DECRYPT(credit_card, 'encryption_key')
   FROM payments;
   ```
   </details>
4. Why is hashing preferred over encryption for password storage? What is a salt and why is it important?
   <details>
   <summary>Show Answer</summary>
   Hashing is one-way (cannot be reversed), so even if the password file is stolen, the original passwords cannot be recovered. Encryption is two-way — if the encryption key is compromised, all passwords are exposed. A **salt** is a random value appended to each password before hashing. It prevents attackers from using precomputed rainbow tables and ensures that identical passwords produce different hashes.
   </details>
5. Describe the SSL/TLS handshake process for securing a database connection.
   <details>
   <summary>Show Answer</summary>
   (1) Client sends a "ClientHello" with supported TLS versions and cipher suites. (2) Server responds with "ServerHello" selecting a cipher suite and sends its digital certificate. (3) Client verifies the certificate against a trusted CA. (4) Client generates a pre-master secret, encrypts it with the server's public key, and sends it to the server. (5) Both derive the symmetric session key from the pre-master secret. (6) They exchange "Finished" messages to confirm the secure connection is established. All subsequent data is encrypted with the session key.
   </details>
