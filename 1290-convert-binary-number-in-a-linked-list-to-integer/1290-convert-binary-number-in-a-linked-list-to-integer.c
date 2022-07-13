/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    int sum = 0;
    do
    {
        sum = 2*sum + head->val;
        head = head->next;
    }while(head != NULL);
    return sum;
}