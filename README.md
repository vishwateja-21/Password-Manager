# 🔐 Password Manager (CLI Tool in Python)

A secure command-line password manager built in Python.  
Features include master password protection, password encryption, and full CRUD support — all running from your terminal with zero bloat.

---

## ✨ Features

- 🔒 **Master Password Authentication** (first-time setup + login)
- 🛡️ **SHA-256 Hashing** for master password
- 🔐 **AES Encryption** of stored passwords using `cryptography`
- 🧾 Store, View, Search, Update, and Delete credentials
- 📂 Saves encrypted credentials to a local JSON file
- 🧠 Clean and beginner-friendly CLI interface

---

## 📦 Technologies Used

- **Python 3.12+**
- [`cryptography`](https://pypi.org/project/cryptography/) for AES encryption
- `hashlib` and `base64` for secure password handling
- JSON for lightweight storage

---

## 📸 Preview

```bash
==== Password Manager ====
1. Add Password
2. View All Passwords
3. Search Password by Website
4. Delete a Password
5. Update a Password
6. Exit
