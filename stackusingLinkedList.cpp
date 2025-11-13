/*stack using linked list*/
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class Stack {
    Node* top;
public:
    Stack() { top = NULL; }

    void push(int val) {
        Node* newNode = new Node();
        newNode->data = val;
        newNode->next = top;
        top = newNode;
    }

    void pop() {
        if (top == NULL)
            cout << "Stack Underflow!" << endl;
        else {
            cout << top->data << " popped from stack." << endl;
            Node* temp = top;
            top = top->next;
            delete temp;
        }
    }

    void display() {
        if (top == NULL)
            cout << "Stack is empty." << endl;
        else {
            Node* temp = top;
            cout << "Stack elements: ";
            while (temp != NULL) {
                cout << temp->data << " ";
                temp = temp->next;
            }
            cout << endl;
        }
    }
};

int main() {
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.display();
    s.pop();
    s.display();
    return 0;
}
