library_data = {
	"M001" : ["book B","book B"],
	"M002" : ["book A"],
	"M003" : [],
	"M004" : ["book B","Book C"],
	"M005" : ["book D"],
	"M006" : ["book D"]
}

# average number of book borrowed 
total_member = len(library_data)
total_borrowed_books = sum(len(books) for books in library_data.values())
average = total_borrowed_books / total_member 
print("total member: ",total_member)
print("total borrowed books: ",total_borrowed_books)
print("average number of books borrowed: ",average)

#most and least borrowed books
all_books = []
for books in library_data.values():
	all_books.extend(books)
	
book_counts ={}
for book in all_books:
	if book in book_counts:
		book_counts[book] += 1
	else:
		book_counts[book] = 1
		
#most borrowed books
most_borrowed = max(book_counts,key=book_counts.get)
print("most borrowed books: ",most_borrowed)

#least borrowed books
least_borrowed = min(book_counts,key=book_counts.get)
print("least borrowed books: ",least_borrowed)

# count member who borrowed zero books
zero_borrowers = sum(1 for books in library_data.values() if len(books) == 0)
print("members with 0 borrowing: ",zero_borrowers)

# most frequent borrowed books: 
print("most frequent borrowed book (mode): ",most_borrowed)



