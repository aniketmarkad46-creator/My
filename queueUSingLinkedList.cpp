/*queue using Linked list*/
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class Queue {
    Node* front;
    Node* rear;
public:
    Queue() { front = rear = NULL; }

    void enqueue(int val) {
        Node* newNode = new Node();
        newNode->data = val;
        newNode->next = NULL;
        if (rear == NULL)
            front = rear = newNode;
        else {
            rear->next = newNode;
            rear = newNode;
        }
    }

    void dequeue() {
        if (front == NULL) {
            cout << "Queue Underflow!" << endl;
            return;
        }
        Node* temp = front;
        cout << front->data << " dequeued from queue." << endl;
        front = front->next;
        if (front == NULL) rear = NULL;
        delete temp;
    }

    void display() {
        if (front == NULL)
            cout << "Queue is empty." << endl;
        else {
            Node* temp = front;
            cout << "Queue elements: ";
            while (temp != NULL) {
                cout << temp->data << " ";
                temp = temp->next;
            }
            cout << endl;
        }
    }
};

int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();
    q.dequeue();
    q.display();
    return 0;
}
