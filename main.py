USERNAME = "admin"
PASSWORD = "1234"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful!")
else:
    print("Invalid Credentials")

import sqlite3
import matplotlib.pyplot as plt   
import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    category TEXT,
    amount REAL,
    description TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")

DB_NAME = "finance.db"


# Add Transaction
def add_transaction(transaction_type):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions(type, category, amount, description, date)
    VALUES (?, ?, ?, ?, ?)
    """, (transaction_type, category, amount, description, date))

    conn.commit()
    conn.close()

    print(f"{transaction_type} added successfully!\n")


# View Transactions
def view_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    data = cursor.fetchall()

    print("\n--- Transactions ---")

    for row in data:
        print(row)

    conn.close()


# Balance Summary
def show_balance():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT type, SUM(amount)FROM transactions GROUP BY type""")

    data = cursor.fetchall()

    income = 0
    expense = 0

    for row in data:
        if row[0] == "Income":
            income = row[1]
        elif row[0] == "Expense":
            expense = row[1]

    balance = income - expense

    print("\n===== Balance Summary =====")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Current Balance: ₹{balance}")

    conn.close()


# Monthly Report
def monthly_report():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category""")

    data = cursor.fetchall()

    print("\n===== Expense Report =====")

    for row in data:
        print(f"{row[0]} : ₹{row[1]}")

    conn.close()

# Delete Transaction
def delete_transaction():
    view_transactions()

    transaction_id = input("\nEnter Transaction ID to delete: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE id = ?
    """, (transaction_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Transaction deleted successfully!")
    else:
        print("Transaction ID not found!")

    conn.close()


# Main Menu
def main():
    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Show Balance")
        print("5. Monthly Expense Report")
        print("6. Delete_transaction")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_transaction("Income")

        elif choice == '2':
            add_transaction("Expense")

        elif choice == '3':
            view_transactions()

        elif choice == '4':
            show_balance()

        elif choice == '5':
            monthly_report()

        elif choice == '6':
            delete_transaction()    

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()

# =========================================================
# ADVANCED FINANCIAL HABIT STREAK TRACKER
# Gamified Personal Finance Python Project
# =========================================================

# Starting Values
saving_streak = 0
budget_streak = 0
no_spending_streak = 0
coins = 0
level = 1

# Function for Design
def line():
    print("=" * 60)

# Welcome Screen
line()
print("FINANCIAL HABIT TRACKER")
line()

name = input("Enter Your Name: ")

days = int(input("Enter number of days to track: "))

# Daily Tracking Loop
for day in range(1, days + 1):

    line()
    print(f"📅 DAY {day} TRACKING")
    line()

   
    # Saving Habit
    save = input("💰 Did you save money today? (yes/no): ").lower()

    if save == "yes":
        saving_streak += 1
        coins += 10
        print(f"🔥 Saving Streak: {saving_streak}")
    else:
        saving_streak = 0
        print("❌ Saving streak broken!")

    # Budget Habit
    budget = input("📊 Did you follow your budget today? (yes/no): ").lower()

    if budget == "yes":
        budget_streak += 1
        coins += 15
        print(f"🔥 Budget Streak: {budget_streak}")
    else:
        budget_streak = 0
        print("❌ Budget streak broken!")

    # Unnecessary Spending Habit
    spending = input("🛒 Did you avoid unnecessary spending today? (yes/no): ").lower()

    if spending == "yes":
        no_spending_streak += 1
        coins += 20
        print(f"🔥 No-Spending Streak: {no_spending_streak}")
    else:
        no_spending_streak = 0
        print("❌ No-spending streak broken!")

    # Waterfall Loading Effect
    print("\n⏳ Calculating rewards", end="")

    for i in range(3):
        print(".", end="")
        time.sleep(1)

    print("\n")

    # Level System
    total_streak = saving_streak + budget_streak + no_spending_streak

    if total_streak >= 20:
        level = 5
    elif total_streak >= 15:
        level = 4
    elif total_streak >= 10:
        level = 3
    elif total_streak >= 5:
        level = 2
    else:
        level = 1

    # Rewards
    line()
    print("🏆 DAILY REWARDS & BADGES")
    line()

    if saving_streak >= 5:
        print("🎖️ Saving Master Badge Unlocked!")

    if budget_streak >= 7:
        print("🏅 Budget Champion Badge Unlocked!")

    if no_spending_streak >= 10:
        print("👑 Smart Spender Badge Unlocked!")

    # Coins and Level
    print(f"\n🪙 Total Coins Earned: {coins}")
    print(f"⭐ Current Level: {level}")

    # Motivation Messages
    if total_streak >= 15:
        print("🚀 Amazing financial discipline!")
    elif total_streak >= 8:
        print("👍 Good job! Keep saving money.")
    else:
        print("📈 Start building stronger habits.")

# Final Summary
line()
print("      FINAL FINANCIAL REPORT")
line()

print(f"👤 User Name                : {name}")
print(f"💰 Final Saving Streak      : {saving_streak}")
print(f"📊 Final Budget Streak      : {budget_streak}")
print(f"🔥 Final No-Spending Streak : {no_spending_streak}")

print(f"\n🪙 Total Coins Earned       : {coins}")
print(f"⭐ Final Level              : {level}")

# Performance Rating
score = saving_streak + budget_streak + no_spending_streak

print("\n📈 PERFORMANCE RESULT")

if score >= 25:
    print("🏆 Excellent Financial Habits!")
elif score >= 15:
    print("👍 Very Good Financial Discipline!")
elif score >= 8:
    print("🙂 Good Start! Keep Improving.")
else:
    print("📚 Need more consistency.")

# Ending Message
line()
print(" THANK YOU FOR USING FINANCE TRACKER 😊 ")
line()    



conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("SELECT category, SUM(amount)FROM transactions WHERE type='Expense'GROUP BY category")

data = cursor.fetchall()

categories = []
amounts = []

for row in data:
    categories.append(row[0])
    amounts.append(row[1])

plt.bar(categories, amounts)

plt.xlabel("Categories")
plt.ylabel("Amount")
plt.title("Expense Analysis")

plt.show()

