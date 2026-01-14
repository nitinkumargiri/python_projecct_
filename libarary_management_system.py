class library:
    def __init__(self):
        self.book = []
        
    def add_book(self,book):
        self.book.append(book)
        print(f"{book} add successfully ✅")
        
    def display_book(self):
        if not self.book:
            print("No booik available in the library")
        else:
            print("Availabe book: ")
            for book in self.book:
                print("-",book)
                
    def issue_book(self,book):
        if book in self.book:
            self.book.remove(book)
            print(f"{book} issued sucessfully.")
        else:
            print("book arae not available.")
            
    def return_book(self,book):
        self.book.append(book)
        print(f"{book} returened sucessfully.")
        
library = library()
while True:
    print("WELCOME TO LIBARARY")
    print("1. Add book")
    print("display book")
    print("3. Issued book")
    print("Return book ")
    print("5.exit")
    
    choice = int (input("enter your choice: "))
    if choice == 1: 
        book = input("Add book: ")
        library.add_book(book)
    