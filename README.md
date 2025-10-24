# 📇 Contact Management System

## 📝 Project Overview
The **Contact Management System** is a simple **Python-based CLI application** that allows users to manage their contact list easily.  
It enables users to **add, edit, view, delete, and search** contacts stored in a **JSON file**.

---

## ⚙️ Features
- ➕ **Add a new contact** (name, phone, email)  
- ✏️ **Edit an existing contact** (update phone or email)  
- 👀 **View all saved contacts**  
- ❌ **Delete a contact** by name  
- 🔍 **Search for a contact** by name  
- 💾 **Persistent storage** — data is saved in a JSON file so it remains after the program closes

---

## 🧩 Project Structure
project-folder/
│
├── contacts.json ← Stores all contact data (auto-created)
├── contact_management.py ← Main program file
└── README.md ← Project documentation (this file)


---

## 🧠 How It Works
When you run the program, it displays a simple text-based menu with six options:

-Add Contact

-Edit Contact

-Show Contacts

-Delete Contact

-Search Contact

-Exit



You choose an option by entering its number, and the program performs the corresponding action.  
All data is saved to and loaded from the `contacts.json` file.

---

## 🧰 Requirements
Before running the project, make sure you have:
- **Python 3.6+** installed  
- The built-in **json** module (comes with Python)

---

## ▶️ How to Run
1. Open your **terminal** or **command prompt** inside the project folder.  
2. Run the following command:
   ```bash
   python contact_management.py
Follow the on-screen instructions.

🧪 Example Run
------Welcome to Contact Management System------
1. Add Contact
2. Edit Contact
3. Show Contacts
4. Delete Contact
5. Search Contact
6. Exit
Choose an option: 1
Enter the name: Ahmed
Enter the phone: 0123456789
Enter the email: ahmed@gmail.com
Contact added successfully.
💡 Notes
If contacts.json does not exist, it will be automatically created.

Email addresses must include @ and . to be valid.

Duplicate contact names are not allowed — each name must be unique.

🚀 Future Improvements
Here are some possible upgrades you could add:

Develop a Graphical User Interface (GUI) using Tkinter or PyQt.

Support multiple contact lists or categories.

Add CSV export/import functionality.

Implement advanced validation for phone numbers and emails.

Add sorting and filtering options for contacts.

