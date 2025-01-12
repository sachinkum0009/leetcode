#include <vector>
#include <iostream>
#include <stdio.h>

/**
 * Definition for singly-linked list.
*/
 struct ListNode {
     int val;
     ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL || list2 == NULL)
        {
            return list1 == NULL ? list2 : list1;
        }
        ListNode* dummy = new ListNode(-1);
        ListNode* list3 = dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                list3->next = new ListNode(list1->val);
                list1 = list1->next;
            } else {
                list3->next = new ListNode(list2->val);
                list2 = list2->next;
            }
            list3 = list3->next;
        }

        while (list1) {
            list3->next = new ListNode(list1->val);
            list1 = list1->next;
            list3 = list3->next;
        }

        while (list2) {
            list3->next = new ListNode(list2->val);
            list2 = list2->next;
            list3 = list3->next;
        }

        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};

ListNode* createList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    for (size_t i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    return head;
}


int main() {
    Solution solution;
    std::vector<int> values1 = {1, 2, 4};
    std::vector<int> values2 = {1, 3, 4};
    ListNode* list1 = createList(values1);
    ListNode* list2 = createList(values2);
    ListNode* mergedList = solution.mergeTwoLists(list1, list2);
    printList(mergedList);
    return 0;
}
