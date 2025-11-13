/*code for complex numbers*/
#include <iostream>
using namespace std;

class Complex {
    float real, imag;   // data members

public:
    // Default constructor
    Complex() {
        real = 0;
        imag = 0;
    }

    // Parameterized constructor
    Complex(float r, float i) {
        real = r;
        imag = i;
    }

    // Operator overloading for addition
    Complex operator + (Complex obj) {
        Complex temp;
        temp.real = real + obj.real;
        temp.imag = imag + obj.imag;
        return temp;
    }

    // Operator overloading for subtraction
    Complex operator - (Complex obj) {
        Complex temp;
        temp.real = real - obj.real;
        temp.imag = imag - obj.imag;
        return temp;
    }

    // Operator overloading for multiplication
    Complex operator * (Complex obj) {
        Complex temp;
        temp.real = (real * obj.real) - (imag * obj.imag);
        temp.imag = (real * obj.imag) + (imag * obj.real);
        return temp;
    }

    // Display function
    void display() {
        cout << real << " + " << imag << "i" << endl;
    }
};

// Main function
int main() {
    Complex c1(3, 2), c2(1, 7), result;

    cout << "First Complex Number: ";
    c1.display();
    cout << "Second Complex Number: ";
    c2.display();

    result = c1 + c2;
    cout << "\nAddition: ";
    result.display();

    result = c1 - c2;
    cout << "Subtraction: ";
    result.display();

    result = c1 * c2;
    cout << "Multiplication: ";
    result.display();

    return 0;
}
