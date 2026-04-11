# 🔐 Password Manager (Python - Tkinter)

A modern Password Manager built using Python Tkinter.
Generate secure passwords, store them safely in JSON format, and quickly search saved credentials.

---

## 🎯 Features

* 🔑 Strong random password generator
* 📋 Auto copy to clipboard
* 💾 Save passwords in **JSON format**
* 🔍 Search saved credentials instantly
* ⚠️ Input validation with popups
* 🖥️ Clean and simple GUI

---

## 📁 Project Structure

```id="u92kls"
.
├── main.py
├── password.png
├── Screenshot.png
├── password_data.json
```

### Files Overview

* **main.py** → Main logic, UI, password generation, saving & search 
* **password.png** → UI logo
* **Screenshot.png** → App preview
* **password_data.json** → Stores credentials securely

---

## 🎮 How It Works

* Enter:

  * Website
  * Email/Username
* Click **Generate** → Creates a strong password
* Password is automatically copied 📋
* Click **Add** → Saves data into JSON file
* Use **Search** → Retrieve saved credentials instantly

---

## 🔒 Security Note

* Data is stored locally in a `.json` file
* No encryption implemented (for learning/demo purposes)

---

## 🧠 Concepts Used

* Tkinter GUI
* JSON data handling
* Random password generation
* File handling (read/write/update)
* Clipboard handling (pyperclip)
* Exception handling

