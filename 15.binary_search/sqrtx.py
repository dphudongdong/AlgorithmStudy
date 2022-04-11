"""
    
    给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
    由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
    要求保留5位有效数字
    https://leetcode-cn.com/problems/sqrtx/solution/by-flix-cxg6/

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, ans = 0,x, -1
        while low <=high:
            mid = low+((high-low)>>1)
            if mid*mid <=x:
                low = mid+1
                ans = mid
            else:
                high = mid -1
        return ans

    def mySqrt1(self, x: int) -> float:
        EPS = 1e-12      # 控制精度
        low, high, ans = 0, x, -1
        while low+EPS <=high:
            mid = low+((high-low)/2)
            if mid*mid <=x:
                low = mid
                ans = mid
            else:
                high = mid
        return round(ans,6)

if __name__ =='__main__':
    a=Solution()
    print(a.mySqrt(5))
    print(a.mySqrt1(2))