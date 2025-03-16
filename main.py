import json

# File to store library data
LIBRARY_FILE = "book_data.json"

# Load library from file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    save_library(library)
    print("Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return
    print("Book not found!\n")

# Search for a book
def search_book(library):
    choice = input("Search by:\n1. Title\n2. Author\nEnter choice: ")
    query = input("Enter search term: ").lower()
    
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.\n")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty!\n")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

# Display statistics
def display_statistics(library):
    if not library:
        print("No books in the library.\n")
        return
    
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
   