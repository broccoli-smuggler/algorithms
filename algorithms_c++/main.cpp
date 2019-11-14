#include <iostream>
#include "BST.h"
#include "BST.tcc"

using std::pair;
using std::cout;
using std::endl;

int main() {
    using namespace tree;

    BST<int, int> bst;
    bst.put(2,2);
    cout << bst.get(2);

    bst.put(3, 99);
    cout << bst.get(3);

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
