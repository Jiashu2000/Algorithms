# 回溯经典问题

from typing import Any, List


# 组合问题

'''
77. Combinations

all possible combinations of k numbers chosen from range [1, n]

'''
class Backtracking_combine:
    
    def __init__(self):
        self.res = []
        self.list = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.res
    
    def backtrack(self, n, k, idx):
        if len(self.list) == k:
            self.res.append(self.list[:])
            return
        for i in range(idx, n+1):
            self.list.append(i)
            self.backtrack(n, k, i+1)
            self.list = self.list[:-1]
    
    def optimized_backtrack(self, n, k, idx):
        if len(self.list) == k:
            self.res.append(self.list[:])
            return
        '''
        已经选择的元素个数: path.size();
        还需要的元素个数为: k - path.size();
        在集合n中至多要从该起始位置 : n - (k - path.size()) + 1, 开始遍历
        为什么有个+1呢, 因为包括起始位置, 我们要是一个左闭的集合。
        举个例子, n = 4, k = 3,  目前已经选取的元素为0(path.size为0), n - (k - 0) + 1 即 4 - ( 3 - 0) + 1 = 2。
        从2开始搜索都是合理的, 可以是组合[2, 3, 4]。
        '''
        for i in range(idx, n - (k - len(self.list))+2):
            self.list.append(i)
            self.backtrack(n, k, i+1)
            self.list = self.list[:-1]
          
    '''
    Time/Space complexity:

    First if in combine will be called exactly c(n, k) times, which is a binomial coefficient - 
    number of ways you can pick k elements from set of size n. 
    Then it has to perform k size job, of creating new result entry. 
    Time complexity - O(k * c(n, k)).

    For loop fragment, will be called exactly c(n, k - 1) times and 
    (in improved solution which only iterates on i <= n - k + 1)
    there will be n/k iterations on average. Time complexity - O(n/k * c(n, k - 1)) .

    Final time complexity = O(k * c(n, k)) + O(n/k * c(n, k - 1))) = O(k * c(n, k)).

    Space complexity - O(k * c(n, k)) - if we exclude the result collection it will be O(k).

    '''

'''
216. Combination Sum III

find valid combinations of k numbers that sum up to n such that
    - only numbers 1 through 9 are used
    - each number is used at most once
'''

class Backtracking_combinationSum3:

    def __init__(self):
        self.res = []
        self.tot = 0 
        self.list = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(k, n, 1)
        return self.res
    
    def backtrack(self, k, n, idx):
        if len(self.list) == k:
            if self.tot == n:
                self.res.append(self.list[:])
            return
        
        for i in range(idx,  9 - (k - len(self.list)) + 2):
            self.list.append(i)
            self.tot += i
            self.backtrack(k, n, i+1)
            self.list.pop()
            self.tot -= i
    
    '''
    Time complexity: O(k * C(9, k)) -> O(9^k)
    
    each recursive call iterates through at most all options (integers [1, 9] in this problem), 
    and we do so for each of the k positions in the combination we are currently trying to build.

    Space complexity: O(k)
    '''
            
'''

39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target. 

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

'''

class Backtracking_combinationSum:

    def __init__(self): 
        self.res = []
        self.list = []
        self.tot = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, 0)
        return self.res
    
    def backtrack(self, candidates, target, idx):
        if self.tot >= target:
            if self.tot == target:
                self.res.append(self.list[:])
            return
        
        for i in range(idx, len(candidates)):
            if self.tot + candidates[i] > target:
                break
            self.list.append(candidates[i])
            self.tot += candidates[i]
            self.backtrack(candidates, target, i)
            self.list.pop()
            self.tot -= candidates[i]
    
    '''
    Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
        For a each element, we can pick it multiple times (t), where t = target / element

    Space complexity: O(M/min_cand)
    '''

'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

'''

class Backtracking_combinationSum2:

    def __init__(self):
        self.res = []
        self.list = []
        self.tot = 0
        self.used = set()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, 0)
        return self.res
    
    def backtrack(self, candidates, target, idx):
        if self.tot >= target:
            if self.tot == target:
                self.res.append(self.list[:])
            return
        
        for i in range(idx, len(candidates)):
            if self.tot + candidates[i] > target:
                break
            '''
            “使用过”在这个树形结构上是有两个维度的, 一个维度是同一树枝上使用过, 一个维度是同一树层上使用过
            我们要去重的是同一树层上的“使用过”, 同一树枝上的都是一个组合里的元素, 不用去重。

            如果candidates[i] == candidates[i - 1] 并且 used[i - 1] == false, 
            就说明:前一个树枝, 使用了candidates[i - 1], 也就是说同一树层使用过candidates[i - 1]。
            '''
            if i > 0 and candidates[i] == candidates[i-1] and (i-1) not in self.used:
                continue
            self.tot += candidates[i]
            self.list.append(candidates[i])
            self.used.add(i)
            self.backtrack(candidates, target, i+1)
            self.tot -= candidates[i]
            self.list.pop()
            self.used.remove(i)

    '''
    Time complexity:
        O(2^n)
        for each element, we have two choices, pick it or not
    Space complexity:
        O(n)
    
    '''

'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

'''

class Backtracking_letterCombination:

    def __init__(self):
        self.list = []
        self.res = []
        self.map = {2: 'abc', 3: "def", 4: 'ghi',
                    5: 'jkl', 6: 'mno', 7: 'pqrs',
                    8: 'tuv', 9: 'wxyz'}
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return self.res
        self.backtrack(digits, 0)
        return self.res
    
    def backtrack(self, digits, d_idx):
        if d_idx == len(digits):
            self.res.append("".join(self.list))
            return
        num = int(digits[d_idx])
        s = self.map[num]
        for i in s:
            self.list.append(i)
            self.backtrack(digits, d_idx+1)
            self.list.pop()
    
    '''
    Time complexity:
        O(n * 4^n)
        where n is the length of digits
    
    Space complexity:
        O(n)
    '''

# 切割问题

'''
131. Palindrome Partitioning 

Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

'''


class Backtracking_palinromePartition:

    def __init__(self):
        self.list = []
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        self.backtrack(s, 0)
        return self.res
    

    def backtrack(self, s, idx):
        if idx == len(s):
            self.res.append(self.list[:])
            return
    
        for i in range(idx+1, len(s)+1):
            sub = s[idx: i]
            if self.isPalindrome(sub):
                self.list.append(sub)
                self.backtrack(s, i)
                self.list.pop()

    def isPalindrome(self, s):
        if not s:
            return False
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True           

    '''
    Time complexity:
        O(n * 2^n)
        In the worst case ('a' * n), we need to traverse all the 2^n possible answers 
        (call backtrack 2^n times). Each time, it costs o(n) to check palindrome
    
    Space complexity:
        O(n * 2^n)

    '''

# 子集问题

'''
78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets.

'''

class Backtracking_subsets:

    def __init__(self):
        self.res = []
        self.list = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):
        self.res.append(self.list[:])
        for i in range(idx, len(nums)):
            self.list.append(nums[i])
            self.backtrack(nums, i+1)
            self.list.pop()
    
    '''
    Time complexity: O(N * 2^N)
        there are n numbers and 2 decisions (whether to include it or not)

    Space complexity: O(N)

    子集和组合、分割问题的区别:
        子集是收集树形结构中树的所有节点的结果
        组合分割问题是收集树形结构中叶子节点的结果
    '''


'''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order

'''

class Backtracking_subsetsWithDup:

    def __init__(self):
        self.res = []
        self.list = []
        self.used = set()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, idx):
        self.res.append(self.list[:])
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in self.used:
                continue
            self.used.add(i)
            self.list.append(nums[i])
            self.backtrack(nums, i+1)
            self.list.pop()
            self.used.remove(i)
    
    '''
    Time complexity:
        O(N * 2^N)
    
    Space complexity:
        O(N)
    
    '''


'''
491. Non-decreasing Subsequences

Given an integer array nums, return all the different possible non-decreasing subsequences 
of the given array with at least two elements. You may return the answer in any order.

'''

class Backtracking_subsequence:

    def __init__(self):
        self.res = []
        self.list = []
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, idx):

        if len(self.list) >= 2:
            self.res.append(self.list[:])
        
        '''
        树层去重的逻辑: 同层出现过就不再用
        '''
        used = set()
        for i in range(idx, len(nums)):
            if self.list and nums[i] < self.list[-1]:
                continue
            if nums[i] in used:
                continue

            used.add(nums[i])
            self.list.append(nums[i])
            self.backtrack(nums, i+1)
            self.list.pop()

    '''
    Time complexity: 
        O(N * 2^N)
    
    Space complexity:
        O(N)

    '''

# 排列问题

'''
46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

'''

class Backtrack_permutation:

    def __init__(self):
        self.res = []
        self.list = []
        self.used = set()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums):
        if len(self.list) == len(nums):
            self.res.append(self.list[:])
            return

        for i in range(0, len(nums)):
            if i not in self.used:
                self.used.add(i)
                self.list.append(nums[i])
                self.backtrack(nums)
                self.list.pop()
                self.used.remove(i)
    
    '''
    Time complexity: o(N * N!)

    Space complexity: o(n)

    排列问题
        - 每层都是从0开始搜索而不是从startIdx
        - 需要used记录使用过的元素

    '''

'''
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

'''      

class Backtrack_permutationUnique:

    def __init__(self):
        self.res = []
        self.list = []
        self.used = set()
        


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums)
        return self.res


    def backtrack(self, nums):
        if len(self.list) == len(nums):
            self.res.append(self.list[:])
            return
        for i in range(0, len(nums)):
            if i in self.used:
                continue
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in self.used:
                continue

            self.list.append(nums[i])
            self.used.add(i)
            self.backtrack(nums)
            self.used.remove(i)
            self.list.pop()
    
    '''
    Time complexity:
        O(N * N!)
    
    Space complexity:
        O(N)

    '''

# 棋盘问题

'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens 
attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

'''

class Backtrack_NQueens:

    def __init__(self): 
        self.res = []
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, n, n, 0)
        return self.res
    
    def backtrack(self, board, n, queen, row):
        if queen == 0:
            tmp = []
            for arr in board:
                tmp.append(''.join(arr))
            self.res.append(tmp)
            return
        
        for i in range(n):
            if board[row][i] == '.' and self.isValid(board, row, i):
                board[row][i] = 'Q'
                self.backtrack(board, n, queen - 1, row+1)
                board[row][i] = '.'
        
    
    def isValid(self, board, row, col):
        # check the same column
        for i in range(len(board)):
            if i != row and board[i][col] == 'Q':
                return False
        
        # check diagonal, only need to check rows above the current row
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1

        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1 

        return True


    '''
    Time complexity:
        O(N!)
        The first row has n options, the second row has (n-1) options, so on...
    
    Space complexity:
        O(N^2)

    '''
    
'''
37. Sudoku Solver 

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

'''


class Backtrack_sudoku:

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board)
    
    def backtrack(self, board):
        '''
        一个for循环遍历棋盘的行,一个for循环遍历棋盘的列,一行一列确定下来之后,递归遍历这个位置放9个数字的可能性!
        '''
        for i in range(len(board)):
            for j in range(len(board[0])):   
                if board[i][j] != '.':
                    continue
                for num in range(1, 10):
                    if self.isValid(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if self.backtrack(board): 
                            return True
                        board[i][j] = '.'
                # 9个数都试完了,都不行,那么就返回false
                return False
        # 遍历完没有返回false,说明找到了合适棋盘位置了
        return True
    
    def isValid(self, board, row, col, num):
        for i in range(len(board)):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
        
        startx = (row//3) * 3
        starty = (col//3) * 3

        for i in range(startx, startx + 3):
            for j in range(starty, starty + 3):
                if i != row and j != col and board[i][j] == num:
                    return False
        return True

    '''
    time complexity: 
        o(9^m)
        where m is the number of '.' on the board
    
    space complexity:
        o(n^2)
    '''

'''
time and space complexity summary

子集问题分析:

    时间复杂度:
        O(2^n),因为每一个元素的状态无外乎取与不取,所以时间复杂度为O(2^n)
    空间复杂度:
        O(n),递归深度为n,所以系统栈所用空间为O(n),每一层递归所用的空间都是常数级别,
        注意代码里的result和path都是全局变量,就算是放在参数里,传的也是引用,并不会新申请内存空间,最终空间复杂度为O(n)


排列问题分析:

    时间复杂度:
        O(n!),这个可以从排列的树形图中很明显发现,每一层节点为n,第二层每一个分支都延伸了n-1个分支,
        再往下又是n-2个分支,所以一直到叶子节点一共就是 n * n-1 * n-2 * ..... 1 = n!。
    空间复杂度:
        O(n),和子集问题同理。

组合问题分析:

    时间复杂度:
        O(2^n),组合问题其实就是一种子集的问题,所以组合问题最坏的情况,也不会超过子集问题的时间复杂度。
    空间复杂度:
        O(n),和子集问题同理。  

N皇后问题分析:

    时间复杂度:
        O(n!) ,其实如果看树形图的话,直觉上是O(n^n),
        但皇后之间不能见面所以在搜索的过程中是有剪枝的,最差也就是O(n!),n!表示n * (n-1) * .... * 1。
    空间复杂度:
        O(n),和子集问题同理。

解数独问题分析:

    时间复杂度:
        O(9^m) , m是'.'的数目。
    空间复杂度:
        O(n^2),递归的深度是n^2

一般说道回溯算法的复杂度,都说是指数级别的时间复杂度,这也算是一个概括吧！

'''

'''
M-coloring Problem

Given an undirected graph and an integer M. 

The task is to determine if the graph can be colored with at most M colors such that 
no two adjacent vertices of the graph are colored with the same color. 

Here coloring of a graph means the assignment of colors to all vertices. 

Print 1 if it is possible to colour vertices and 0 otherwise.

the function graphColoring() which takes the 2d-array graph[], 
the number of colours and the number of nodes as inputs and returns true if answer exists otherwise false. 
1 is printed if the returned value is true, 0 otherwise.

'''

class backtrack_mColoring:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True
    
    def graphColorUtil(self, m, color, v):
        if v == self.V:
            return True
        
        for c in range(1, m+1):
            if self.isSafe(v, color, c):
                color[v] = c
                if self.graphColorUtil(m, color, v+1):
                    return True
                color[v] = 0
        return False
    
    def graphColoring(self, m):
        color = [0] * self.V
        if not self.graphColorUtil(m, color, 0):
            return False
        
        print("Solution exists: ")
        for c in color:
            print(c, " ")
        return True

# g = backtrack_mColoring(4)
# g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
# m = 3
# 
# g.graphColoring(m)

'''
time complexity: o(m^v). there is a total of o(m^v) combinations of colors.
where m is the number of colors and v is the number of vertices.

space complexity: o(v)

'''

'''
Rat in a Maze

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] 
and destination block is lower rightmost block i.e., maze[N-1][N-1]. 
A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down.

'''

class backtrack_ratMaze:

    def __init__(self, maze):
        self.maze = maze

    def isValid(self, n, x, y, res):
        if x >= 0 and y >= 0 and x < n and y < n and self.maze[x][y] == 1 and res[x][y] == 0:
            return True
        return False
    
    def ratMaze(self, n, move_x, move_y, x, y, res):
        if x == n-1 and y == n-1:
            return True
        for i in range(4):
            x_new = x + move_x[i]
            y_new = y + move_y[i]
            if self.isValid(n, x_new, y_new, res):
                res[x_new][y_new] = 1
                if self.ratMaze(n, move_x, move_y, x_new, y_new, res):
                    return True
                res[x_new][y_new] = 0
        return False
    
    def solveMaze(self):
        n = len(self.maze)
        res = [[0] * n for _ in range(n)]
        res[0][0] = 1
        move_x = [-1, 1, 0, 0]
        move_y = [0, 0, 1, -1]
        
        if self.ratMaze(n, move_x, move_y, 0, 0, res):
            for i in range(n):
                for j in range(n):
                    print(res[i][j], end = " ")
                print()
        else:
            print("solution does not exist")
        

# maze = [[1, 0, 0, 0],
#             [1, 1, 0, 1],
#             [0, 1, 0, 0],
#             [1, 1, 1, 1]]
# 
# m = backtrack_ratMaze(maze)
# m.solveMaze()

    '''
    time complexity:
        o(2^(n^2))
    
    space complexity:
        o(n^2)
    
    Why we cannot use dp to solve this problem?

    DP only works when you can decompose the problem into smaller problems. 
    For most grid problems that DP works on, there's a limitation that you can only move down and to the right.
    But in this case, you can move in all 4 directions, so the ability to carve out subproblems is no longer available. 
    '''


'''
The Knight's tour problem

'''

class backtrack_knightTour:

    def __init__(self, n):
        self.n = n
    
    def isSafe(self, x, y, board):
        if x >= 0 and y >= 0 and x < self.n and y < self.n and board[x][y] == -1: 
            return True
        return False
    
    def printSolution(self, board):
        for i in range(self.n):
            for j in range(self.n):
                print(board[i][j], end =" ")
            print(" ")
    
    def solveKT(self):
        board = [[-1] * self.n for _ in range(self.n)]
        move_x = [ -1 , 1 , 2 , 2 , 1 , -1 , -2 , -2 ]
        move_y = [2 , 2 , 1 , -1 , -2 , -2 , -1 , 1]

        board[0][0] = 0

        pos = 1

        if not self.solveKTUtil(board, 0, 0, move_x, move_y, pos):
            print("Solution does not exist")
        else: 
            self.printSolution(board)
    
    def solveKTUtil(self, board, cur_x, cur_y, move_x, move_y, pos):
        if pos == self.n*self.n:
            return True
        
        for i in range(8):
            new_x = cur_x + move_x[i]
            new_y = cur_y + move_y[i]
            if self.isSafe(new_x, new_y, board):
                board[new_x][new_y] = pos
                if self.solveKTUtil(board, new_x, new_y, move_x, move_y, pos+1):
                    return True
                board[new_x][new_y] = -1
        return False

'''
Permutation of a Given String

A permutation also called an “arrangement number” or “order,” 
is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. 
A string of length N has N! permutations. 

'''

class backtrack_permuteString: 

    def __init__(self):
        self.res = []
        self.s = []
        self.used = set()

    def permuteString(self, s):
        sl = list(s)
        self.backtrack(sl)
        for s in self.res:
            print("permute string: ", s )
        return self.res
    
    def backtrack(self, list):
        if len(self.s) == len(list):
            self.res.append(self.s[:])
            return
        for i in range(len(list)):
            if i not in self.used:
                self.used.add(i)
                self.s.append(list[i])
                self.backtrack(list)
                self.s.pop()
                self.used.remove(i)

# g = backtrack_permuteString()
# g.permuteString("abc")

    '''
    time complexity:
        o(n * n!)
    
    space complexity:
        o(n)
        
    '''
        
        
