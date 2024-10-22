from datetime import datetime

def calculate_fine(due_date, return_date):
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d")
        returned = datetime.strptime(return_date, "%Y-%m-%d")
        days_overdue = (returned - due).days

        if days_overdue > 0:
            fine = days_overdue * 5  # $5 per day overdue
            print(f"Item is {days_overdue} days overdue. Fine: ${fine}")
        else:
            print("No fine. Item returned on time.")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")