/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  bool isPalindrome(ListNode? head) {
    List<int> values = [];
    while (head != null) {
      values.add(head.val);
      head = head.next;
    }
    int i = 0;
    int j = values.length - 1;
    while (i < j) {
      if (values[i] != values[j]) return false;
      i++;
      j--;
    }
    return true;
  }
}