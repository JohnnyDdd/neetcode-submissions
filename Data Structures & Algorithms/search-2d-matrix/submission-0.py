class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mtx_l = 0
        m = len(matrix)
        lm = 0
        rm = m-1
        mid_m = -1
        while rm >= lm:
            mid_m = (rm+lm) // 2
            if matrix[mid_m][-1] >= target and matrix[mid_m][0] <= target: break
            else:
                if target < matrix[mid_m][0]: rm = mid_m - 1
                else: lm = mid_m + 1

        if mid_m == -1: return False
        n = len(matrix[0])
        row = matrix[mid_m]

        ln = 0
        rn = n - 1
        while rn >= ln:
            mid_n = (rn+ln) // 2
            if row[mid_n] == target: return True
            else:
                if target < row[mid_n]: rn = mid_n - 1
                else: ln = mid_n + 1
                
        return False