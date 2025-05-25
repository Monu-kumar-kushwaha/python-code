import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('books.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create the books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert initial data into the books table
    books = [
        ('The Catcher in the Rye', 'J.D. Salinger', 10.99),
        ('To Kill a Mockingbird', 'Harper Lee', 7.99),
        ('1984', 'George Orwell', 8.99),
        ('Pride and Prejudice', 'Jane Austen', 6.99),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 10.99)
    ]

    cursor.executemany('''
        INSERT INTO books (title, author, price)
        VALUES (?, ?, ?)
    ''', books)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database created and initial data inserted successfully.")

# Run the function to create the database and insert data
create_database()

import sqlite3

def connect_to_db():
    return sqlite3.connect('books.db')

def fetch_book_price(title):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT price FROM books WHERE title = ?', (title,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def add_book(title, author, price):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))
    conn.commit()
    conn.close()

def calculate_total_amount(title, quantity):
    price = fetch_book_price(title)
    if price is not None:
        total_amount = price * quantity
        return total_amount
    else:
        return None

# Main function demonstrating the usage of above functions
def main():
    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Calculate total amount for purchase")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            add_book(title, author, price)
            print(f"Book '{title}' by {author} added successfully.")
        
        elif choice == '2':
            title = input("Enter the book title: ")
            quantity = int(input("Enter the quantity purchased: "))
            total_amount = calculate_total_amount(title, quantity)
            if total_amount is not None:
                print(f"Total amount for {quantity} copies of '{title}' is ${total_amount:.2f}")
            else:
                print(f"Book '{title}' not found in the database.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
