# 💰 Expense Tracker (CSV-Based, Python CLI)

A simple, user-friendly **command-line expense tracker** built with Python.  
This app allows you to log, store, and view expenses in a structured CSV file.

---

## ✨ Features

- Add new expenses with:
  - Date
  - Category (e.g., Food, Transport)
  - Description
  - Amount
- View all recorded expenses in a formatted table
- Automatically calculates and displays total spending
- Stores all data in `expenses.csv`
- Creates the file automatically if it doesn't exist

---

## 🚀 Getting Started

1. Save the Script
Save the file as `expense_tracker.py`.

2. Run the App
```bash
python expense_tracker.py
```
---

## 🖥️ Usage

On running the script, you'll see a menu like:

Expense Tracker Menu
1. Add Expense
2. View Expenses
3. Exit
---

## ➕ Add Expense

You will be prompted to enter:
Date (YYYY-MM-DD)
Category (e.g., Food, Transport)
Description
Amount

The input is then saved to expenses.csv.
---

## 📊 View Expenses

Prints all expenses in a neat table format and shows a running total.
Example output:

```
Date         Category        Description               Amount
-----------------------------------------------------------------
2024-07-22   Food            Lunch at cafe              85.00
2024-07-22   Transport       Bus fare                   20.00
-----------------------------------------------------------------
Total                                               105.00
```
---

## 📁 Project Structure

```
expense-tracker/
│
├── expense_tracker.py    # Main Python script
├── expenses.csv           # Auto-created CSV data file
└── README.md
```
---

## ✅ Requirements

```
Python 3.x
No third-party libraries required
```
---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋 Author

Created by Nomanguni Khumalo — Manage your money smarter!

