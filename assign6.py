class StudentNode:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks= marks
        self.next = None

class studentLinkedList:
    def __init__(self):
        self.head = None

    def AddStudent(self,roll_no,name,marks):
        new_node = StudentNode(roll_no,name,marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Student Record Added.")

    def DeleteStudent(self, roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no == roll_no:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("Student Record Deleted.")
                return
            prev = current
            current = current.next
        print("Student not Found.")

    def UpdateStudent(self, roll_no, new_name, new_marks):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.name = new_name
                current.marks = new_marks
                print("Student Record Updated.")
                return
            current = current.next
        print("Student Not found.")

    def SearchStudent(self,roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"Found:- \nRoll No:",current.roll_no,"  Name:",current.name,"  Marks:",current.marks)
                return
            current = current.next
        print("Student not Found.")

    def DisplayStudent(self, sort_by="roll_no", ascending=True):
        students = []
        current = self.head
        while current:
            students.append((current.roll_no, current.name, current.marks))
            current = current.next
        if sort_by == "roll_no":
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
            students.sort(key=lambda x: x[2], reverse=not ascending)
        if not students:
            print("No Record to Dispaly.")
            return
        print("Student Record: ")
        for s in students:
            print(f"Roll no.: ",s[0],"  Name: ",s[1],"  Marks: ",s[2])            

def menu():
    System = studentLinkedList()
    print("--- Student Record Management Menu---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")

    while True:
        choice = int(input("\nEnter your choice (1-6) : "))
        if choice == 1:
            roll = int(input("Enter Roll no : "))
            name = input("Enter Name : ")
            marks= int(input("Enter Marks : "))
            System.AddStudent(roll,name,marks)
        elif choice == 2:
            roll = int(input("Enter Roll no to delete : "))
            System.DeleteStudent(roll)
        elif choice == 3:
            roll = int(input("Enter Roll no to update: "))
            name = input("Enter new Name : ")
            marks= int(input("Enter updated Marks : "))
            System.UpdateStudent(roll,name,marks)
        elif choice == 4:
            roll = int(input("Enter Roll no to Search : "))
            System.SearchStudent(roll)
        elif choice == 5:
            sort_key = input("Sort by 'roll_no' or 'marks' : ").strip()
            order = input("Order 'asc' or 'desc' : ").strip()
            ascending = True if order == 'asc' else False
            System.DisplayStudent(sort_by=sort_key, ascending=ascending)
        elif choice == 6:
            print("Exiting Student Record Management System.")
            break
        else:
            print("Invalid choice, try again!")

menu()
            