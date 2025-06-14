
# PostgreSQL Access Reference for BloodHound Community Edition

This guide provides commonly used PostgreSQL commands to access and inspect the `bloodhound` database, especially useful when working with BloodHound CE (v7+).

---

## ✅ Access Methods

### 1. Recommended (Peer Auth via Unix Socket)
No password required (uses local Unix user identity):

```bash
sudo -u _bloodhound psql -d bloodhound
```

### 2. Alternate (TCP Connection, SSL Disabled)
Useful when `psql` crashes with SSL errors or you're scripting access:

```bash
psql "host=localhost dbname=bloodhound user=_bloodhound sslmode=disable"
```

> 💡 This bypasses SSL and avoids potential memory corruption issues on Kali Linux.

---

## 🛠 Common `psql` Commands

### View all databases:
```sql
\l
```

### Connect to a database:
```bash
\c bloodhound
```

### List all tables:
```sql
\dt
```

### Show table structure:
```sql
\d users
\d auth_secrets
\d users_roles
```


### Exit `psql`:
```sql
\q
```

---

## 🧩 Notes

- Default database: `bloodhound`
- Default user: `_bloodhound`
- Data includes users, auth secrets, roles, and session tokens
- Located on port `5432` (default PostgreSQL port)

---

## 🔐 Troubleshooting

### If `psql` crashes with `SSL SYSCALL`:
Use:

```bash
psql "host=localhost dbname=bloodhound user=_bloodhound sslmode=disable"
```

Or force non-SSL in `.psqlrc` or with environment variables.

---

## 📁 File Location Reference

- Config: `/etc/bhapi/bhapi.json`
- Database files: `/var/lib/postgresql/`
