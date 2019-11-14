//
// Created by joshua on 14/11/19.
//

#ifndef THINK_CELL_INTERFACES_ITREE_H_
#define THINK_CELL_INTERFACES_ITREE_H_

#include <iterator>
#include <optional>
#include <vector>

namespace tree {

using std::optional;
using std::iterator;
using std::vector;

template <class K, class V>
class ITree {
 public:
  virtual void put(K key, V value) = 0;
  virtual void delete_value(K key) = 0;
  virtual optional<V> get(K key) = 0;
  virtual void delete_tree() = 0;
  virtual vector<V> sorted() = 0;
};

}

#endif //THINK_CELL_INTERFACES_ITREE_H_
