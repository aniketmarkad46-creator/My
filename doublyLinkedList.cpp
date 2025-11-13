/*doubly linked list*/
#include <iostream>
using namespace std;

struct Node {
    int data;           // data part of node
    Node *prev, *next;  // pointers to previous and next node
};

Node* head = NULL;  // initially the list is empty

// Insert node at the end of the list
void insertEnd(int value) {
    Node* newNode = new Node;     // create new node
    newNode->data = value;        // assign data
    newNode->next = NULL;         // next is null for new end node
    newNode->prev = NULL;         // prev initially null

    if (head == NULL) {           // if list is empty
        head = newNode;           // new node becomes head
    } else {
        Node* temp = head;
        while (temp->next != NULL)  // go to last node
            temp = temp->next;
        temp->next = newNode;       // link new node at end
        newNode->prev = temp;       // set previous pointer
    }
}

// Display all nodes in the list
void display() {
    if (head == NULL) {
        cout << "List is empty\n";
        return;
    }
    Node* temp = head;
    cout << "List: ";
    while (temp != NULL) {          // traverse from head to end
        cout << temp->data << " ";  // print each data
        temp = temp->next;
    }
    cout << endl;
}

// Delete the first node containing the given value
void deleteNode(int value) {
    Node* temp = head;

    // search for node with given value
    while (temp != NULL && temp->data != value)
        temp = temp->next;

    if (temp == NULL) {  // value not found
        cout << "Value not found\n";
        return;
    }

    // if node to delete is the head
    if (temp == head) {
        head = temp->next;
    }

    // adjust previous/next links
    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    if (temp->prev != NULL)
        temp->prev->next = temp->next;

    delete temp;  // free memory
    cout << "Deleted " << value << endl;
}

int main() {
    int choice, val;

    do {
        cout << "\n1. Insert at end\n2. Display list\n3. Delete by value\n4. Exit\nEnter choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter value to insert: ";
            cin >> val;
            insertEnd(val);
            break;
        case 2:
            display();
            break;
        case 3:
            cout << "Enter value to delete: ";
            cin >> val;
            deleteNode(val);
            break;
        case 4:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice\n";
        }
    } while (choice != 4);

    return 0;
}
