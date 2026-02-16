# ISS-Overhead-Notifier
DAY - 33 - Project - Python X ISS Overhead Notifier

# 🛰️ ISS Overhead Notifier

## 📌 Project Overview

ISS Overhead Notifier is a Python automation project that tracks the real-time position of the International Space Station (ISS) and sends an email alert when the ISS is overhead during night-time at the user’s location.

The program combines live API data, location-based checks, UTC time comparison, and automated email notifications.

---

## 🔗 APIs Used

### 1️⃣ ISS Position API

Used to get real-time ISS coordinates.

```
http://api.open-notify.org/iss-now.json
```

### 2️⃣ Sunrise–Sunset API

Used to determine day/night based on location.

```
https://api.sunrise-sunset.org/json
```

---

## ⚙️ How the Code Works

* 🌍 Stores user latitude and longitude.
* 📡 Fetches live ISS position from API.
* 📍 Checks if ISS is within ±5° range of user location.
* 🌙 Retrieves sunrise and sunset times.
* ⏰ Compares UTC time to detect night.
* 🔁 Runs continuously in a loop for live monitoring.
* 📧 Sends email alert when both conditions are true.

---

## 📧 Gmail App Password Setup (Required)

Google blocks normal password login for scripts, so you must create an **App Password**.

### Steps:

1️⃣ Go to your Google Account
2️⃣ Open **Security**
3️⃣ Enable **2-Step Verification**
4️⃣ Search for **App Passwords**
5️⃣ Select:

* App → Mail
* Device → Other (Custom Name)
  6️⃣ Click **Generate**
  7️⃣ Copy the 16-character password
  8️⃣ Paste it in your Python code:

```python
user_password = "your_app_password"
```

⚠️ Do NOT use your normal Gmail password.

---

## ▶️ Run Project

Install dependency:

```bash
pip install requests
```

Run:

```bash
python iss_overhead_notifier.py
```

---

## 🧩 Technologies Used

* Python
* Requests (API handling)
* Datetime (UTC logic)
* SMTP (Email automation)
* JSON data parsing

---

## 👨‍💻 Author

**Robin Gupta**
