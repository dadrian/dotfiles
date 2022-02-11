#include <iostream>

using namespace std;

// MyTemplateClass is a templated class.
template<typename T>
class MyTemplateClass {
public:
    T* Object;

    void print();
};

template<typename T>
void MyTemplateClass<T>::print() {
    if (object == nullptr) {
        std::cout << "Object is unset\n" << std::endl;
    } else {
        std::cout << "Object is set\n." << std::endl;
    }
}

int main(int argc, const char *argv[]) {
    std::cout << "Hello, world!";
    MyTemplateClass<double> mtc;
    mtc.print();
    return 0;
}
