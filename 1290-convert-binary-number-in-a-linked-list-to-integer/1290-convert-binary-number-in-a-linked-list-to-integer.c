/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    while(head->next != NULL)
    {
        head->next->val += 2 * head->val;
        head = head->next;
    }
    return head->val;
}