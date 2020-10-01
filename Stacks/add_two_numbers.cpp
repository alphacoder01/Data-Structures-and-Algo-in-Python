/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        struct ListNode* result = new ListNode(0);
        struct ListNode* resultPtr = result;
        
        int sum, carry=0, currNode;
        while(l1!=NULL || l2!=NULL){

            if(l1!=NULL && l2!=NULL){
                sum = l1->val + l2->val + carry;
                l2 = l2->next;
                l1 = l1->next;
            }
                
            else if(l1!=NULL){
                sum = l1->val + carry;
                l1 = l1->next;
            }
            
            else if(l2!=NULL){
                sum = l2->val + carry;
                l2 = l2->next;
            }
            
            currNode = sum % 10;
            carry = (int)(sum / 10);
            
            resultPtr->next = new ListNode(currNode);            
            resultPtr = resultPtr->next;
        }
        
        if(carry){
            resultPtr->next = new ListNode(carry);
            resultPtr = resultPtr->next;
        }
        return result->next;
    }
};