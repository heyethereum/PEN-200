# Command History Cheat Sheet

## Windows (PowerShell & Command Prompt)

### **1. View PowerShell Command History**

```powershell
Get-History
```

```powershell
(Get-PSReadlineOption).HistorySavePath
```

```powershell
notepad (Get-PSReadlineOption).HistorySavePath
```

```powershell
Get-History | Select-Object -Last 10
```

### **2. View Command Prompt (CMD) History**

```cmd
doskey /history
```

---

## Linux & macOS

### **1. View Bash History**

```bash
history
```

```bash
history | tail -10
```

```bash
cat ~/.bash_history
```

```bash
fc -l
```

```bash
fc -s
```

---

## Network Services Command Histories

### **1. View SNMP Command History**

```bash
cat ~/.snmp_history
```

```bash
grep snmp /var/log/syslog
```

```powershell
Get-EventLog -LogName System | Where-Object {$_.Source -like "SNMP*"}
```

---

### **2. View SSH Command History**

```bash
cat ~/.bash_history | grep ssh
```

```bash
tail -f /var/log/auth.log | grep sshd
```

---

### **3. View Web Server (Apache/Nginx) Command History**

```bash
tail -f /var/log/apache2/access.log
```

```bash
tail -f /var/log/nginx/access.log
```

---

## Summary

| Service | Command |
|---------|---------|
| PowerShell | `Get-History` |
| PowerShell | `(Get-PSReadlineOption).HistorySavePath` |
| CMD | `doskey /history` |
| Bash | `history` |
| Bash | `cat ~/.bash_history` |
| SNMP | `cat ~/.snmp_history` |
| SNMP | `grep snmp /var/log/syslog` |
| SSH | `cat ~/.bash_history | grep ssh` |
| Apache | `tail -f /var/log/apache2/access.log` |
| Nginx | `tail -f /var/log/nginx/access.log` | 
