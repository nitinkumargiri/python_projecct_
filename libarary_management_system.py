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
            print(f"{book} issued sucessfully.✅")
        else:
            print("book arae not available.")
            
    def return_book(self,book):
        self.book.append(book)
        print(f"{book} returened sucessfully.")
        
library = library()
while True:
    print("📚📙WELCOME TO LIBARARY📙📚")
    print("1. Add book")
    print("2. display book")
    print("3. Issued book")
    print("4. Return book ")
    print("5. exit")
    
    choice = int (input("enter your choice: "))
    if choice == 1: 
        book = input("Add book: ")
        library.add_book(book)
        
    elif choice == 2:
        library.display_book()
    
    elif choice == 3:
        book = input("eter your issued book: ")
        library.issue_book(book)
        
    elif choice == 4:
        book = input("enter those book do you want to return: ")
        library.return_book(book)
        
    elif choice == 5:
        print("GOOD BYE..👋👋")
        break
    
    else:
        print("Invailed choice ❌❌")
        
        
        
    