
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.n_path = 0

        def recurPathSum(root, sum_upto_now):
            if not root:
                return
            sum_local = sum_upto_now + root.val

            if sum_local - targetSum in sum_freq:
                self.n_path += sum_freq[sum_local - targetSum]
            if sum_local not in sum_freq:
                sum_freq[sum_local] = 1
            else:
                sum_freq[sum_local] += 1

            recurPathSum(root.left, sum_local)
            recurPathSum(root.right, sum_local)

            sum_freq[sum_local] -= 1
            if sum_freq[sum_local] == 0:
                del sum_freq[sum_local]

        sum_freq = {0: 1}
        recurPathSum(root, 0)

        return self.n_path