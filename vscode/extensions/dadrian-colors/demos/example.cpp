#include <iostream>

using namespace std;

template<typename T>
class MyTemplateClass {
    private T* Object;

    public void print();
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
