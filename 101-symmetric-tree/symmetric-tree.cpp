/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) 
    {
        if ( root == nullptr )
            return false;
        
        return isSymmetricHelper(root->left, root->right);
    }

    bool isSymmetricHelper(TreeNode* node_left, TreeNode* node_right)
    {
        if ( node_left == nullptr && node_right == nullptr)
            return true;
        if ( node_left == nullptr || node_right == nullptr)
            return false;
        return ( node_left->val == node_right->val ) &&
                isSymmetricHelper(node_left->left, node_right->right) &&
                isSymmetricHelper(node_left->right, node_right->left); 
    }
};