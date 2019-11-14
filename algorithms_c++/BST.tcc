//
// Created by joshua on 14/11/19.
//

#include "BST.h"

namespace tree {

using std::make_shared;

template<class K, class V>
BST<K, V>::~BST() {
    if (root_node != NULL) this->delete_tree();
}

template<class K, class V>
void BST<K, V>::put(K key, V value) {
    this->put(key, value, this->root_node);
}

template<class K, class V>
shared_ptr<typename  BST<K, V>::Node> BST<K, V>::put(K key, V value, shared_ptr<Node>& current) {
    // NULL exit
    if (current == nullptr) current = make_shared<Node>(key, value);
    else if (key < current->key) current->left = this->put(key, value, current->left);
    else if (key > current->key) current->right = this->put(key, value, current->right);
    else current->value = value;
    return current;
}

template <class K, class V>
optional<shared_ptr<typename BST<K, V>::Node>> BST<K, V>::find(K key) {
    shared_ptr<Node> current_node = this->root_node;
    while (current_node != NULL) {
        if (key < current_node->key) current_node = current_node->left;
        else if (key > current_node->key) current_node = current_node->right;
        else return current_node;
    }
    return {};
}

template<class K, class V>
void BST<K, V>::delete_value(K key) {
    shared_ptr<Node> current = this->root_node;
    shared_ptr<Node> root;
    bool is_left = true;

    while (current != NULL) {
        if (current->key > key) {
            // iterate down to the left
            root = current;
            current = current->left;
            is_left = true;
        } else if (current->key < key) {
            // iterate down to the right
            root = current;
            current = current->right;
            is_left = false;
        } else {
            // Found the node to delete
            if (current->left == NULL && current->right == NULL) {
                // No sub trees, so just delete and make the root point to NULL
                current = NULL;
                (is_left ? root->left = NULL : root->right = NULL);
            } else if (current->left != NULL && current->right != NULL) {
                // two sub trees, make the right the new root and put the left on it
                (is_left ? root->left = current->right : root->right = current->right);
                shared_ptr<Node> far_left = current->right;
                while(far_left->left != NULL) {
                    far_left = far_left->left;
                }
                far_left->left = current->left;
                current = NULL;
            } else {
                if (current->left != NULL) {
                    (is_left ? root->left = current->left : root->right = current->left);
                } else if (current->right != NULL){
                    (is_left ? root->left = current->right : root->right = current->right);
                }
                current = NULL;
            }
        }
    }
}

template<class K, class V>
optional<V> BST<K, V>::get(K key) {
    auto option = this->find(key);
    if (option) {
        return (*option)->value;
    }
    return {};
}

template<class K, class V>
void BST<K, V>::delete_tree() {

}

template <class K, class V>
void BST<K, V>::morris_travel_inorder(shared_ptr<Node>& root, vector<V>& result) {
    shared_ptr<Node> current = root;
    shared_ptr<Node> righter;

    while (current != NULL) {
        // check to see if current has a left branch
        if (current->left != NULL) {
            // go through to the right most banch on this subtree
            righter = current->left;
            while (righter->right != NULL) {
                righter = righter->right;
            }

            // append the current to the right of the righter sub tree
            righter->right = current;
            shared_ptr<Node> t = current;
            current = current->left;
            t->left = NULL;
        }
        else {
            result.push_back(current->value);
            current = current->right;
        }
    }
}

template<class K, class V>
vector<V> BST<K, V>::sorted() {
    vector<V> result;
    this->morris_travel_inorder(this->root_node, result);
    return result;
}

}
