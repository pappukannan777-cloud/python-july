books=["Harry Potter","The Hobbit","Wings of Fire","Diary of a Wimpy Kid"]
copies=[3,0,2,5]

library={book:copy for book,copy in zip(books,copies)}

available=[book for book in books if library[book]>0]
print("Available books:",available)

choice=input("Enter the book you want to borrow: ")

if choice not in library or library[choice]==0:
    print("Book is not available")
    exit()

fees=[10,20,30,40]
extra=int(input("Enter extra fee: "))

fees=list(map(lambda x:x+extra,fees))

index=books.index(choice)
library[choice]=library[choice]-1

print("Borrowed book:",choice)
print("Updated fee:",fees[index])
print("Library:",library)