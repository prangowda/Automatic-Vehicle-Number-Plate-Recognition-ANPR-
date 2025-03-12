import csv
import sqlite3

# Initialize database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number_plate TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

def save_to_csv(plate_number):
    with open("vehicle_records.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([plate_number])
    print(f"Saved {plate_number} to CSV.")

def save_to_database(plate_number):
    cursor.execute("INSERT INTO vehicles (number_plate) VALUES (?)", (plate_number,))
    conn.commit()
    print(f"Saved {plate_number} to database.")

if __name__ == "__main__":
    sample_plate = "KA 01 AB 1234"
    save_to_csv(sample_plate)
    save_to_database(sample_plate)
