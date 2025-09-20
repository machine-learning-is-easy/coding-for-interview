
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global front
        front = head

        def helper(back) -> bool:
            global front
            if not back:
                return True

            # let back pointer travel to the back of the list through recursion
            equal_so_far = helper(back.next)

            # check if front and back have the same value
            value_equal = (front.val == back.val)

            # when the function return, back is gradually moved toward head of the list
            # move front accordingly to compare their value
            front = front.next
            return equal_so_far and value_equal

        return helper(head)