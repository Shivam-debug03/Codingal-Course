from datetime import datetime

books = []
history = []

print("LIBRARY BOOK ORGANISER")

while True:
    print("\n1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. View library history")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        title = input("Enter the book title: ").strip()
        author = input("Enter the author's name: ").strip()
        genre = input("Enter the book genre: ").strip()

        if not title or not author or not genre:
            print("Please fill in all the book details.")
        else:
            time = datetime.now().strftime("%d %b %Y, %I:%M %p")
            book = {
                "title": title,
                "author": author,
                "genre": genre,
                "time": time,
            }
            books.append(book)
            history.append(f'{time} - Added "{title}" by {author}')
            print('"' + title + '" has been added to your library.')

    elif choice == "2":
        if not books:
            print("Your library is empty. Add a book to get started.")
        else:
            print("\nYOUR BOOKS")
            number = 1
            for book in books:
                print(f'{number}. {book["title"]} by {book["author"]}')
                print(f'   Genre: {book["genre"]} | Added: {book["time"]}')
                number = number + 1

    elif choice == "3":
        search_text = input("Search by title, author, or genre: ").strip().lower()
        found = False

        for book in books:
            if (search_text in book["title"].lower()
                    or search_text in book["author"].lower()
                    or search_text in book["genre"].lower()):
                print(f'{book["title"]} by {book["author"]}')
                print(f'Genre: {book["genre"]} | Added: {book["time"]}')
                found = True

        if not found:
            print("No matching books found.")

    elif choice == "4":
        if not books:
            print("There are no books to remove.")
        else:
            print("\nChoose a book to remove:")
            number = 1
            for book in books:
                print(f'{number}. {book["title"]} by {book["author"]}')
                number = number + 1

            try:
                book_number = int(input("Enter the book number: "))
                if book_number > 0 and book_number <= len(books):
                    removed_book = books.pop(book_number - 1)
                    time = datetime.now().strftime("%d %b %Y, %I:%M %p")
                    history.append(
                        f'{time} - Removed "{removed_book["title"]}"'
                    )
                    print('"' + removed_book["title"] + '" has been removed.')
                else:
                    print("That book number is not on the list.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "5":
        if not history:
            print("There is no library history yet.")
        else:
            print("\nLIBRARY HISTORY")
            for event in history:
                print(event)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Please choose a number from 1 to 6.")