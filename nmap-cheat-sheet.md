# Nmap Cheat Sheet: Reconnaissance & Vulnerability Scanning

## Basic Scanning Techniques

| Command | Description |
|---------|-------------|
| `nmap <target>` | Default scan (TCP SYN scan of top 1000 ports) |
| `nmap -sS <target>` | TCP SYN scan (requires root/sudo) |
| `nmap -sT <target>` | TCP connect scan |
| `nmap -sU <target>` | UDP scan (requires root/sudo) |
| `nmap -sV <target>` | Version detection scan |
| `nmap -O <target>` | OS detection (requires root/sudo) |
| `nmap -A <target>` | Aggressive scan (OS detection, version detection, script scanning, traceroute) |

## Host Discovery

| Command | Description |
|---------|-------------|
| `nmap -sn <target>` | Ping scan (no port scan) |
| `nmap -Pn <target>` | Skip host discovery (treat all hosts as online) |
| `nmap -PS <port list> <target>` | TCP SYN discovery on specified ports |
| `nmap -PA <port list> <target>` | TCP ACK discovery on specified ports |
| `nmap -PU <port list> <target>` | UDP discovery on specified ports |
| `nmap -PE <target>` | ICMP echo discovery |

## Port Specification

| Command | Description |
|---------|-------------|
| `nmap -p 22 <target>` | Scan specific port |
| `nmap -p 1-100 <target>` | Scan port range |
| `nmap -p- <target>` | Scan all ports (1-65535) |
| `nmap -p http,https <target>` | Scan ports by service name |
| `nmap --top-ports 1000 <target>` | Scan top N ports |
| `nmap -F <target>` | Fast scan (top 100 ports) |

## Timing and Performance

| Command | Description |
|---------|-------------|
| `nmap -T0 <target>` | Paranoid timing (slowest) |
| `nmap -T1 <target>` | Sneaky timing |
| `nmap -T2 <target>` | Polite timing |
| `nmap -T3 <target>` | Normal timing (default) |
| `nmap -T4 <target>` | Aggressive timing |
| `nmap -T5 <target>` | Insane timing (fastest) |
| `nmap --min-rate=1000 <target>` | Send packets no slower than 1000 per second |
| `nmap --max-retries=2 <target>` | Limit retry attempts |

## Output Options

| Command | Description |
|---------|-------------|
| `nmap -oN output.txt <target>` | Normal output to file |
| `nmap -oX output.xml <target>` | XML output to file |
| `nmap -oG output.grep <target>` | Grepable output to file |
| `nmap -oA output <target>` | Output in all formats |
| `nmap -v <target>` | Verbose output |
| `nmap -vv <target>` | Very verbose output |

## Advanced Options

| Command | Description |
|---------|-------------|
| `nmap -f <target>` | Fragment packets |
| `nmap --mtu <size> <target>` | Set specific MTU size |
| `nmap -D RND:5 <target>` | Cloak scan with 5 random decoys |
| `nmap --source-port <port> <target>` | Spoof source port |
| `nmap --data-length <size> <target>` | Append random data to packets |
| `nmap --reason <target>` | Display reason nmap classified ports as open/closed |

## Vulnerability Scanning with NSE

### Basic NSE Script Usage

| Command | Description |
|---------|-------------|
| `nmap --script vuln <target>` | Run all vulnerability detection scripts |
| `nmap --script "vuln and safe" <target>` | Run safe vulnerability scripts |
| `nmap --script "vuln,exploit" <target>` | Run vulnerability and exploit scripts |
| `nmap --script-updatedb` | Update the script database |

### Common Vulnerability Scanning Commands

| Command | Description |
|---------|-------------|
| `nmap -sV --script vuln <target>` | Service version detection with vulnerability scan |
| `nmap -sV --script "vuln" -p 443 <target>` | Scan for vulnerabilities on specific port |
| `nmap -sV --script "ssl-*" <target>` | Scan for SSL/TLS vulnerabilities |
| `nmap --script "http-*" <target>` | Scan for HTTP vulnerabilities |
| `nmap --script "smb-vuln*" -p 445 <target>` | Scan for SMB vulnerabilities |

### Specific Vulnerability Scanning Examples

| Command | Description |
|---------|-------------|
| `nmap --script ssl-heartbleed <target>` | Check for Heartbleed vulnerability |
| `nmap --script smb-vuln-ms17-010 <target>` | Check for EternalBlue vulnerability |
| `nmap --script http-shellshock <target>` | Check for Shellshock vulnerability |
| `nmap --script ftp-vsftpd-backdoor <target>` | Check for vsFTPd backdoor |
| `nmap --script "vuln and safe" -p 22,80,443 <target>` | Safe vulnerability scanning of selected ports |

### Detailed Vulnerability Scan Command Examples

```bash
# Comprehensive vulnerability scan with service version detection
sudo nmap -sS -sV --script vuln <target>

# Scan all ports for vulnerabilities
sudo nmap -sS -p- --script vuln <target>

# Scan for vulnerabilities with verbose output and save to file
sudo nmap -sS -sV -v --script vuln -oN vuln-scan.txt <target>

# Scan network range for MS17-010 (EternalBlue) vulnerability
sudo nmap -sS -p 445 --script smb-vuln-ms17-010 192.168.1.0/24

# Scan web server for vulnerabilities
sudo nmap -sS -sV -p 80,443 --script "http-vuln*" <target>
```

## Practical Reconnaissance Examples

```bash
# Quick initial recon scan
sudo nmap -sS -T4 --min-rate=1000 -p- <target>

# Detailed scan of discovered ports
sudo nmap -sS -sV -sC -p80,443,8080 <target>

# Network sweep with version detection on common ports
sudo nmap -sS -sV -F 192.168.1.0/24

# Stealthy reconnaissance scan
sudo nmap -sS -T2 --top-ports 100 <target>

# Comprehensive scan for penetration testing
sudo nmap -sS -sV -O -A --script "default,vuln" -oA full-scan <target>
```

## Important Notes

1. **Authorization**: Only scan systems you own or have explicit permission to test.
2. **Detection**: More aggressive scans are more likely to be detected by security systems.
3. **Legal Implications**: Unauthorized scanning may violate laws or regulations.
4. **Performance Impact**: Intensive scanning can impact target system performance.
5. **False Positives**: Vulnerability scans may report false positives that require manual verification.
