# 📧 Email Automation for Clio Website using Python & Selenium

This project automates email-based tasks on the Clio website using Python and Selenium. It reads a list of emails from a file, performs actions for each email, and tracks used ones.

---

## 📝 Instructions

### ✅ 1. Paste All Emails
- Open the file `E1.txt`
- Paste all your target **email addresses** (one per line)

### ✅ 2. Keep `S1.txt` Empty Initially
- The file `S1.txt` should remain **empty** initially.
- It will automatically store **used/processed email addresses** as the script runs.

### ✅ 3. Enter Your Clio Credentials
- Open `main.py`
- Find and enter your:
  ```python
  username = "your_clio_email"
  password = "your_clio_password"
