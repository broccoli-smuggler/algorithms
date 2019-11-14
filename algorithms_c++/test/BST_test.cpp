//
// Created by joshua on 15/11/19.
//

#include <string>
#include <vector>
#include <gtest/gtest.h>
#include "BST.h"
#include "BST.tcc"

using std::string;
using std::vector;

class BST_int_test : public ::testing::Test {
 protected:
  tree::BST<int, string> bst_;
  BST_int_test() = default;

};

TEST_F(BST_int_test, test_init) {
    EXPECT_FALSE(bst_.get(1));
}

TEST_F(BST_int_test, test_put_get) {
    bst_.put(1, "a");
    EXPECT_EQ(bst_.get(1), "a");
};

TEST_F(BST_int_test, test_sorted) {
    bst_.put(1, "a");
    bst_.put(2, "b");
    bst_.put(4, "d");
    std::vector<string> r = {"a", "b", "d"};
    EXPECT_EQ(r, bst_.sorted());
}

TEST_F(BST_int_test, test_delete_right_sub) {
    bst_.put(1, "a");
    bst_.put(2, "b");
    bst_.put(4, "d");
    bst_.put(3, "c");
    bst_.delete_value(4);
    EXPECT_FALSE(bst_.get(4));
    std::vector<string> r = {"a", "b", "c"};
    EXPECT_EQ(r, bst_.sorted());
}

TEST_F(BST_int_test, test_delete_left_sub) {
    bst_.put(1, "a");
    bst_.put(2, "b");
    bst_.put(4, "d");
    bst_.put(5, "e");
    bst_.delete_value(4);
    EXPECT_FALSE(bst_.get(4));
    std::vector<string> r = {"a", "b", "e"};
    EXPECT_EQ(r, bst_.sorted());
}

TEST_F(BST_int_test, test_delete_2_sub) {
    bst_.put(1, "a");
    bst_.put(2, "b");
    bst_.put(4, "d");
    bst_.put(3, "c");
    bst_.put(5, "e");
    bst_.delete_value(4);
    EXPECT_FALSE(bst_.get(4));
    std::vector<string> r = {"a", "b", "c", "e"};
    EXPECT_EQ(r, bst_.sorted());
}

TEST_F(BST_int_test, test_delete_null_sub) {
    bst_.put(1, "a");
    bst_.put(2, "b");
    bst_.put(4, "d");
    bst_.delete_value(4);
    EXPECT_FALSE(bst_.get(4));
    std::vector<string> r = {"a", "b"};
    EXPECT_EQ(r, bst_.sorted());
}
