
# 🔍 File Search Cheat Sheet: `find` (Linux) vs `Get-ChildItem` (PowerShell)

---

## 🐧 Linux: `find`

| Task                        | Command Example                                         |
|-----------------------------|---------------------------------------------------------|
| Find all `.txt` files       | `find / -name "*.txt" 2>/dev/null`                      |
| Case-insensitive search     | `find / -iname "*.txt"`                                 |
| Find files in current dir   | `find . -type f -name "*.txt"`                          |
| Find files > 100MB          | `find / -size +100M`                                    |
| Find recently modified      | `find . -mtime -1`                                      |
| Find and delete             | `find /tmp -type f -name "*.log" -delete`               |
| Execute command on result   | `find . -name "*.log" -exec rm {} \;`                  |

---

## 🪟 Windows PowerShell: `Get-ChildItem`

| Task                        | Command Example                                         |
|-----------------------------|---------------------------------------------------------|
| Find all `.txt` files       | `Get-ChildItem -Filter *.txt`                           |
| Recursively search          | `Get-ChildItem -Recurse -Filter *.txt`                 |
| Shorthand                   | `gci -Recurse -Filter *.txt`                            |
| Show full paths             | `gci -Recurse -Filter *.txt | Select-Object FullName`   |
| Search specific path        | `gci -Path C:\Users\mike\Desktop -Filter *.txt`      |
| Find by extension           | `gci -Recurse -Include *.ps1`                           |
| Combine with Where-Object   | `gci -Recurse | Where-Object { $_.Name -like "*.txt" }` |

---

### 🖥 CMD (Windows Command Prompt)

| Task                        | Command Example                                          |
|-----------------------------|----------------------------------------------------------|
| Find all `.txt` files       | `dir /s /b *.txt`                                        |
| Search specific folder      | `dir C:\\Users\\mike\\Desktop\\*.txt /s /b`              |
| Search by part of name      | `dir /s /b | findstr flag`                               |
| Search whole drive          | `dir C:\\ /s /b | findstr flag.txt`                      |
| Redirect errors             | `dir /s /b *.txt 2>nul`          
---

### 📝 Notes
- PowerShell `find` is **not** like Linux `find`; it searches **text inside files**.
- Use `gci` (`Get-ChildItem`) for file discovery in PowerShell.
- Redirect `2>/dev/null` in Linux to suppress permission errors.

---

✅ Use the right command depending on your shell: **Bash** (Linux) vs **PowerShell** (Windows).
