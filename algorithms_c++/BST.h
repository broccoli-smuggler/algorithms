//
// Created by joshua on 14/11/19.
//

#ifndef THINK_CELL__BST_H_
#define THINK_CELL__BST_H_

#include <memory>
#include <optional>
#include "interfaces/ITree.h"

namespace tree {
using std::shared_ptr;
using std::optional;

template <class K, class V>
class BST: public ITree<K, V> {
 public:
  BST() = default;
  ~BST();

  void put(K key, V value) override;
  void delete_value(K key) override;
  optional<V> get(K key) override;
  void delete_tree() override;
  vector<V> sorted() override;

 private:
  class Node {
   public:
    Node(K key, V value) : key(key), value(value)  {}

    shared_ptr<Node> left;
    shared_ptr<Node> right;
    K key;
    V value;
  };

  shared_ptr<Node> put(K key, V value, shared_ptr<Node>& current);
  optional<shared_ptr<Node>> find(K key);
  void morris_travel_inorder(shared_ptr<Node>& root, vector<V>& result);
  shared_ptr<Node> root_node;
};
}

#endif //THINK_CELL__BST_H_
