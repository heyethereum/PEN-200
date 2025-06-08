# 🛡️ Common Ports Cheat Sheet (Linux & Windows)

This cheat sheet lists commonly used TCP/UDP ports for Linux and Windows environments, ordered by OS.

---

## 🐧 Linux Ports

| Port | Protocol | Service         | Description                     | Vulnerabilities / Notes                  |
|------|----------|------------------|---------------------------------|-------------------------------------------|
| 20   | TCP      | FTP Data         | Data channel for FTP            | Insecure, susceptible to sniffing        |
| 21   | TCP      | FTP              | File Transfer Protocol          | Can allow file access if misconfigured   |
| 22   | TCP      | SSH              | Secure Shell                    | Brute force if weak creds                |
| 23   | TCP      | Telnet           | Unencrypted remote shell        | Outdated and insecure                    |
| 25   | TCP      | SMTP             | Mail transfer                   | May allow spam relaying                  |
| 53   | TCP/UDP  | DNS              | Domain Name System              | DNS spoofing, amplification              |
| 67   | UDP      | DHCP Server      | Dynamic Host Config Protocol    | Rogue DHCP attacks                       |
| 68   | UDP      | DHCP Client      | Client-side DHCP                |                                           |
| 69   | UDP      | TFTP             | Trivial File Transfer Protocol  | No authentication                        |
| 80   | TCP      | HTTP             | Web traffic                     | Cleartext; subject to MITM               |
| 110  | TCP      | POP3             | Email retrieval                 | Credentials in plain text                |
| 123  | UDP      | NTP              | Network Time Protocol           | NTP amplification DDoS                   |
| 137  | UDP      | NetBIOS Name     | Name service                    | Info leakage                             |
| 138  | UDP      | NetBIOS Datagram | Datagram service                |                                           |
| 139  | TCP      | NetBIOS Session  | Session service                 | File/printer sharing risks               |
| 143  | TCP      | IMAP             | Internet Message Access         |                                           |
| 161  | UDP      | SNMP             | Network Management              | Default community strings = insecure     |
| 443  | TCP      | HTTPS            | Secure Web Traffic              | TLS downgrade, weak ciphers              |
| 445  | TCP      | SMB              | File sharing and AD             | EternalBlue, SMB relay                   |
| 514  | UDP      | Syslog           | Log message forwarding          | Cleartext logs                           |
| 631  | TCP      | CUPS             | Print services                  | May expose printer info                  |
| 3306 | TCP      | MySQL            | MySQL Database Server           | Default creds, injection risks           |
| 5432 | TCP      | PostgreSQL       | PostgreSQL Database Server      |                                           |
| 8080 | TCP      | HTTP-Alt         | Alternate web server port       | Often used for admin panels              |

---

## 🪟 Windows Ports

| Port     | Protocol | Service         | Description                                | Vulnerabilities / Notes                              |
|----------|----------|------------------|--------------------------------------------|-------------------------------------------------------|
| 21       | TCP      | FTP              | Microsoft FTP Server                       | Could allow file access                              |
| 53       | UDP      | DNS              | Simple DNS Plus                            | Could leak internal info                             |
| 88       | TCP      | Kerberos         | Authentication for AD                      | Kerberoasting attacks                                |
| 135      | TCP      | RPC              | Remote Procedure Call                      | Can enumerate services                               |
| 137      | UDP      | NetBIOS Name     | Name resolution                            | Info leakage                                         |
| 138      | UDP      | NetBIOS Datagram | Datagram distribution                      |                                                     |
| 139      | TCP      | NetBIOS Session  | File/printer sharing                       | Info leaks                                           |
| 389,3268 | TCP      | LDAP             | Directory services                         | Critical for domain attacks                          |
| 445      | TCP      | SMB              | Direct file/printer sharing                | Commonly exploited (e.g. EternalBlue)               |
| 464      | TCP      | Kerberos Change  | Password change service                    | Sensitive to relay attacks                           |
| 593      | TCP      | RPC over HTTP    | Remote DCOM                                | May expose DCOM services                             |
| 636      | TCP      | LDAPS            | Secure LDAP                                | Weak TLS configs if outdated                         |
| 3269     | TCP      | GC-LDAPS         | Global Catalog over SSL                    | Used in AD forests; sensitive                        |
| 3389     | TCP      | RDP              | Remote Desktop Protocol                    | Brute-force, BlueKeep                                |
| 5985     | TCP      | WinRM (HTTP)     | Windows Remote Management                  | EvilWinRM, lateral movement                          |
| 5986     | TCP      | WinRM (HTTPS)    | Secure Windows Remote Management           | May still expose certs or auth weaknesses            |
| 47001    | TCP      | WinRM Listener   | Admin WinRM service                        | Elevated access vector                               |
| 9389     | TCP      | .NET Message     | WCF Services                               | Could be abused for internal communication attacks   |
| 49152–65535| TCP    | Dynamic Ports    | RPC and WMI                                | Hard to monitor; used in many lateral movement tools |

---

## 📌 Notes
- Ports can vary slightly based on service configuration.
- Ensure firewall and security policies align with usage.
- Use tools like `nmap`, `netstat`, or `ss` to verify open ports.

✅ **Tip**: Always audit which services are bound to open ports and restrict them by IP/firewall when possible.