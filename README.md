# PEN-200
# Commonly Used Commands

## 📌 **Connecting to OffSec VPN**
```bash
sudo openvpn universal.ovpn
```

---

## 🔍 **Scanning and Web Enumeration**
```
### **Start a Web Server**
```bash
python3 -m http.server 80
```

---

## 💻 **Upgrading to a Fully Interactive Shell**
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
1. Press `CTRL+Z`
2. Run:
```bash
stty raw -echo; fg
```
3. Set terminal type:
```bash
export TERM=xterm
```

---

## 🖥 **Remote Desktop (XRDP) - Windows**
```bash
xfreerdp /u:damian /p:ICannotThinkOfAPassword1! /v:192.168.172.221 /size:80% /tls-seclevel:0 /timeout:80000 /drive:kali,.
```

---

## 🏴 **Metasploit & Payloads**
```bash
msfvenom -
```

---

## 🔍 **Windows Enumeration**
### **Find All Text Files in `C:\Users`**
```cmd
dir /s c:\users\*.txt
```

### **Find Windows System Information**
```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

### **Check Last Patch Date**
```cmd
wmic qfe
```

### **Check Logical Drives**
```cmd
wmic logicaldisk get caption,description, providername
```

### **Extract Saved Wi-Fi Passwords (Windows)**
```cmd
netsh wlan show profile <SSID> key=clear
```

#### **Extract All Saved WiFi Passwords in One Command**
```cmd
cls & echo. & for /f "tokens=4 delims=: " %a in ('netsh wlan show profiles ^| find "Profile "') do @echo 
off > nul & (netsh wlan show profile "%a" key=clear | findstr "SSID Key")
```

---

## 🛡 **Check if Antivirus is Running (Windows)**
```cmd
sc query windefend
netsh advfirewall firewall dump
netsh firewall show state
```

---

## 🎧 **Start a Reverse Shell Listener**
```bash
nc -lvp 443
```

---

## 🏴 **Searching for Flag Files**
### **Linux**
```bash
find / -name 'flag*' 2>/dev/null
```
### **Windows (PowerShell)**
```powershell
Get-ChildItem -Path C:\ -Filter "flag*" -Recurse -ErrorAction SilentlyContinue
```
### **Windows (CMD)**
```cmd
dir C:\ /s /b | findstr /i "^flag"
```

---

## 🐳 **Docker Commands**
### **Install Docker**
```bash
sudo apt install docker.io
```
### **Install Docker Compose**
```bash
sudo apt install docker-compose
```
### **Start Docker Compose**
```bash
sudo docker-compose up
```
### **Run Docker Compose in Background**
```bash
sudo docker-compose up -d
```
### **Check Running Containers**
```bash
sudo docker ps -a
```
### **Stop Docker Containers**
```bash
sudo docker-compose stop
```
### **Remove a Docker Container**
```bash
sudo docker rm <container_id>
```
### **Remove All Containers**
```bash
sudo docker rm $(sudo docker ps -aq)
```
