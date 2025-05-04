#include <bits/stdc++.h>
using namespace std;

class Person{
public:
    string name;
    Person(string name){
        this->name = name;
    }
    void say_hello(){
        cout << "Hello, I am " << name << endl;
    }
};

int main(){
    Person p("Bryan");
    p.say_hello();
}