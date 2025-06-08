
# 🛡️ Common Ports Cheat Sheet (Linux & Windows)

This cheat sheet lists commonly used TCP/UDP ports for Linux and Windows environments, ordered by OS.

---

## 🐧 Linux Ports

| Port | Protocol | Service         | Description                     |
|------|----------|------------------|---------------------------------|
| 22   | TCP      | SSH              | Secure Shell                    |
| 21   | TCP      | FTP              | File Transfer Protocol          |
| 20   | TCP      | FTP Data         | Data channel for FTP            |
| 23   | TCP      | Telnet           | Unencrypted remote shell        |
| 25   | TCP      | SMTP             | Mail transfer                   |
| 53   | TCP/UDP  | DNS              | Domain Name System              |
| 67   | UDP      | DHCP Server      | Dynamic Host Config Protocol    |
| 68   | UDP      | DHCP Client      | Client-side DHCP                |
| 69   | UDP      | TFTP             | Trivial File Transfer Protocol  |
| 80   | TCP      | HTTP             | Web traffic                     |
| 110  | TCP      | POP3             | Email retrieval                 |
| 123  | UDP      | NTP              | Network Time Protocol           |
| 137  | UDP      | NetBIOS Name     | Name service                    |
| 138  | UDP      | NetBIOS Datagram | Datagram service                |
| 139  | TCP      | NetBIOS Session  | Session service                 |
| 143  | TCP      | IMAP             | Internet Message Access         |
| 161  | UDP      | SNMP             | Simple Network Management       |
| 443  | TCP      | HTTPS            | Secure Web Traffic              |
| 445  | TCP      | SMB              | File sharing and AD             |
| 514  | UDP      | Syslog           | Log message forwarding          |
| 631  | TCP      | CUPS             | Print services                  |
| 3306 | TCP      | MySQL            | MySQL Database Server           |
| 5432 | TCP      | PostgreSQL       | PostgreSQL Database Server      |
| 8080 | TCP      | HTTP-Alt         | Alternate web server port       |

---

## 🪟 Windows Ports

| Port  | Protocol | Service        | Description                                  |
|-------|----------|----------------|----------------------------------------------|
| 135   | TCP      | RPC            | Remote Procedure Call                        |
| 137   | UDP      | NetBIOS Name   | Name resolution                              |
| 138   | UDP      | NetBIOS Datagram| Datagram distribution                        |
| 139   | TCP      | NetBIOS Session| File/printer sharing over NetBIOS            |
| 445   | TCP      | SMB            | Direct file/printer sharing                  |
| 3389  | TCP      | RDP            | Remote Desktop Protocol                      |
| 5985  | TCP      | WinRM (HTTP)   | Windows Remote Management  (evil winRM)      |
| 5986  | TCP      | WinRM (HTTPS)  | Secure Windows Remote Management             |
| 47001 | TCP      | WinRM Listener | Windows Remote Management Admin Service      |
| 49152–65535 | TCP | Dynamic Ports | Ephemeral ports for RPC and WMI             |

---

## 📌 Notes
- Ports can vary slightly based on service configuration.
- Ensure firewall and security policies align with usage.
- Use tools like `nmap`, `netstat`, or `ss` to verify open ports.

---

✅ **Tip**: Always audit which services are bound to open ports and restrict them by IP/firewall when possible.

## Common Windows Ports and Vulnerbilities 

### <span style="color:deepskyblue">FTP</span> <span style="color:orange">(Port 21)</span>
<span style="color:white">Microsoft FTP Server</span> — <span style="color:red">could allow file access!</span>

### <span style="color:mediumpurple">DNS</span> <span style="color:orange">(Port 53)</span>
<span style="color:white">Simple DNS Plus</span> — <span style="color:red">could leak internal info</span>

### <span style="color:darkorange">Kerberos</span> <span style="color:orange">(Port 88)</span>
<span style="color:white">Important for Windows authentication</span> — <span style="color:red">target for attacks like Kerberoasting</span>

### <span style="color:goldenrod">RPC</span> <span style="color:orange">(Port 135)</span>
<span style="color:white">Windows Remote Procedure Call</span> — <span style="color:yellow">can enumerate services</span>

### <span style="color:mediumseagreen">NetBIOS</span> <span style="color:orange">(Port 139)</span>
<span style="color:white">Used for file/printer sharing</span> — <span style="color:red">could lead to info leaks</span>

### <span style="color:crimson">LDAP</span> <span style="color:orange">(Port 389, 3268)</span>
<span style="color:white">Active Directory</span> — <span style="color:red">critical for domain attacks!</span>

### <span style="color:sienna">SMB</span> <span style="color:orange">(Port 445)</span>
<span style="color:white">File sharing</span> — <span style="color:red">commonly exploited</span>

### <span style="color:steelblue">HTTP</span> <span style="color:orange">(Ports 5985, 47001)</span>
<span style="color:white">Windows Remote Management over HTTP</span>

### <span style="color:orchid">.NET Message</span> <span style="color:orange">(Port 9389)</span>
<span style="color:white">Might be related to WCF services</span> — <span style="color:red">could be abused</span>

### <span style="color:gray">Other Ports</span> <span style="color:orange">(464, 593, 636, 3269)</span>
<span style="color:white">Various Windows services tied to Active Directory and secure communication</span>
