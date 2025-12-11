"""
def setZeroes(matrix):
    n, m = len(matrix), len(matrix[0])
    col0 = 1  # Flag to track if the first column should be zeroed

    # Step 1: Mark rows and columns that should be zeroed using the first row and first column
    for i in range(n):
        if matrix[i][0] == 0:
            col0 = 0  # First column should be zeroed
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row
                matrix[0][j] = 0  # Mark column

    # Step 2: Update matrix based on markers (excluding first row & column)
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle the first row
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Step 4: Handle the first column
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
setZeroes(matrix)

# Print the modified matrix
for row in matrix:
    print(row)

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)

def countSubarraysWithSum(arr, k):
    prefix_sum_count = {0: 1}  # Dictionary to store prefix sum frequencies
    preSum = 0
    count = 0

    for num in arr:
        preSum += num  # Update prefix sum
        #print(preSum)
        remove = preSum - k  # Check if (preSum - k) exists in dictionary -2,0,3,1,6,4
        #print(remove)
        count += prefix_sum_count.get(remove, 0)  # Add occurrences of (preSum - k)
        #print("___",count)
        prefix_sum_count[preSum] = prefix_sum_count.get(preSum, 0) + 1  # Update prefix sum count
        print(prefix_sum_count[preSum] )

    return count

# Example Usage:
arr = [1, 2, 3, -2, 5]
k = 3
print(countSubarraysWithSum(arr, k))  # Output: 4


from collections import Counter

def majority_element_better(nums):
    n = len(nums)
    freq_map = Counter(nums)
    #print(freq_map)
    print(freq_map.items())
    return [key for key, value in freq_map.items() if value > n // 3]

# Example Usage
nums = [3, 2, 3, 1, 1, 1, 2, 2]
print(majority_element_better(nums))  # Output: [1, 2]


def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicates for i
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:  # Avoid duplicates for j
                continue

            k, l = j + 1, n - 1  # Two pointers

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                print(total)

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    # Avoid duplicate results
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans


# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))  # Expected output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


from collections import defaultdict

def subarrays_with_xor_k(arr, k):
    xr = 0
    xor_count = defaultdict(int)
    xor_count[xr] = 1  # {0:1}
    count = 0

    for num in arr:
        xr ^= num  # Compute prefix XOR
        x = xr ^ k  # Find required XOR sum
        count += xor_count[x]  # Add occurrences of required XOR
        xor_count[xr] += 1  # Update frequency of XOR values

    return count

# Example usage:
arr = [4, 2, 2, 6, 4]
k = 6
print(subarrays_with_xor_k(arr, k))  # Output: 4

def merge_overlapping_intervals(intervals):
    intervals.sort()  # Step 1: Sort based on start time
    merged = []

    for interval in intervals:
        print(interval)
        # Step 2: If merged is empty or no overlap, add interval
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Step 3: Merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
            #print(interval[1])

    return merged

# Example Usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_overlapping_intervals(intervals))
# Expected Output: [[1, 6], [8, 10], [15, 18]]


def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = (n + m + 1) // 2  # Ensure rounding up
    print(gap)

    while gap > 0:
        i, j = 0, gap
        while j < (n + m):
            # Determine which arrays we're comparing
            if j < n:
                a, b = arr1, arr1  # Both in arr1
            elif i < n:
                a, b = arr1, arr2  # One in arr1, one in arr2
            else:
                a, b = arr2, arr2  # Both in arr2

            # Compare and swap if needed
            if a[i % n] > b[j % n]:
                a[i % n], b[j % n] = b[j % n], a[i % n]

            i += 1
            j += 1

        gap = (gap + 1) // 2 if gap > 1 else 0  # Reduce gap


# Example usage
arr1 = [1, 4, 7, 8]
arr2 = [2, 3, 6, 9]
merge(arr1, arr2)
print(arr1, arr2)  # Output: [1, 2, 3, 4] [6, 7, 8, 9]

def find_missing_repeating(arr):
    n = len(arr)

    # Step 1: Calculate expected sum and sum of squares
    SN = (n * (n + 1)) // 2
    print(SN)
    S2N = (n * (n + 1) * (2 * n + 1)) // 6
    print(S2N)

    # Step 2: Calculate actual sum and sum of squares from the array
    S = sum(arr)
    print(S)
    S2 = sum(x * x for x in arr)
    print(S2)

    # Step 3: Calculate values
    val1 = S - SN  # y - x
    print(val1)
    val2 = (S2 - S2N) // val1  # x + y
    print(val2)

    # Step 4: Solve for missing (x) and repeating (y)
    x = (val2 - val1) // 2  # Missing number
    print("m x",x)
    y = x + val1  # Repeating number
    print("m y", y)

    return [x, y]

# Example Usage
arr = [4, 3, 6, 2, 1, 1]  # Here 1 is repeating, and 5 is missing
print(find_missing_repeating(arr))  # Output: [5, 1]"""



def merge(arr, low, mid, high):
    temp, left, right, cnt = [], low, mid + 1, 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)
            right += 1

    temp.extend(arr[left:mid+1])  # Add remaining left half elements
    temp.extend(arr[right:high+1])  # Add remaining right half elements
    arr[low:high+1] = temp  # Copy sorted elements back

    return cnt

def merge_sort(arr, low, high):
    #print("high",high)
    if low >= high:
        return 0
    mid = (low + high) // 2
    return (merge_sort(arr, low, mid) +
            merge_sort(arr, mid + 1, high) +
            merge(arr, low, mid, high))
    #print(merge(arr, low, mid, high))

def number_of_inversions(arr):
    return merge_sort(arr, 0, len(arr) - 1)

# Example Usage
arr = [4, 3, 6, 2, 1, 1]
print(number_of_inversions(arr))  # Output: Number of inversions


#More optimized version using BIT


def second_largest(num):
    return sorted(set(num))[-2] if len(set(num)) > 1 else None


num = [1, 2, 4, 5, 7, 7, 8]
print("Second Largest:", second_largest(num))



def consiquit_num(nums):
    maxi = 0
    cont = 0
    for i in nums:
        if i == 1:
            cont += 1
            maxi = max(maxi,cont)
            #print(maxi)
        else:
            cont = 0
    return maxi



nums = [1, 1, 1, 0, 0, 1, 1]

def find_single(a):
    ans = 0
    for i in a:
        ans =  ans ^ a[i]
    return ans

a=[1,1,2,3,3,4,4]
print(consiquit_num(nums))
print(find_single(a))

def longest_subarray_with_sum_k(arr, k):
    pre_sum_map = {}  # Dictionary to store first occurrences of prefix sums
    sum_ = 0
    max_len = 0

    for i in range(len(arr)):
        sum_ += arr[i]

        # If the sum itself equals k, update max_len
        if sum_ == k:
            max_len = max(max_len, i + 1)

        # Check if sum_ - k exists in the map
        rem = sum_ - k
        print(rem)
        if rem in pre_sum_map:
            length = i - pre_sum_map[rem]
            #print(i)
            #print(pre_sum_map[rem])
            max_len = max(max_len, length)
            #print(max_len)

        # Store first occurrence of sum_
        if sum_ not in pre_sum_map:
            pre_sum_map[sum_] = i
            print("__",pre_sum_map[sum_])

    return max_len

arr = [3, 1, 2, 5, 1]
k = 8
print(longest_subarray_with_sum_k(arr, k))  # Output: 3



def sum_of(nums):
    dict = {}
    target = 6
    for i in nums:
        #print(i)
        #num = i
        needed = target - i
        #print("___",needed)
        if needed not in dict:
            dict[nums] = i
        else:
            dict


def twoSum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        #print(i)
        #print("__",num)
        more_needed = target - num  # Find the required number
        print(more_needed)

        if more_needed in num_map:  # If found in dictionary, return indices
            return [num_map[more_needed], i]

        num_map[num] = i  # Store the index of the current number

    return [-1, -1]  # Return [-1, -1] if no solution is found



nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))

def sum_of(book,target):
    book.sort()
    left = 0
    right = len(book)-1
    while left < right:
     sum = book[left] + book[right]
     if sum == target:
        return [book[left] , book[right]]
     elif sum < target:
        left +=1
     else:
        right -= 1


target = 5
book = [4, 1, 2, 3, 1]
print(sum_of(book, target))

def swap_flag(dutch_flag):
    low = 0
    mid = 0
    high = len(dutch_flag) - 1
    while mid <= high:
        if dutch_flag[mid] == 0:
            dutch_flag[low],dutch_flag[mid] = dutch_flag[mid],dutch_flag[low]
            low += 1
            mid += 1
        elif dutch_flag[mid] == 1:
            mid += 1
        else:
            dutch_flag[mid],dutch_flag[high] = dutch_flag[high],dutch_flag[mid]
            high -= 1
    return dutch_flag




dutch_flag= [2, 0, 2, 1, 1, 0]
print(swap_flag(dutch_flag))



def trap_rain_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    # Fill left_max array (highest bar from left)
    left_max[0] = heights[0]
    print(heights[0])
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Fill right_max array (highest bar from right)
    right_max[n - 1] = heights[n - 1]
    print(right_max[n - 1])
    print(heights[n - 1])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate water trapped
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped

# Example usage
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Trapped Rain Water:", trap_rain_water(heights))  # Output: 6



class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = []  # Stores backward history
        self.forward_stack = []  # Stores forward history
        self.current = homepage  # Current page

    def visit(self, url):
        """Visit a new URL, clearing the forward history."""
        self.back_stack.append(self.current)  # Save current page
        self.current = url  # Move to new page
        self.forward_stack.clear()  # Clear forward history

    def back(self, steps):
        """Go back 'steps' times in history."""
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)  # Save current page
            self.current = self.back_stack.pop()  # Move back
            steps -= 1
        return self.current

    def forward(self, steps):
        """Go forward 'steps' times in history."""
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)  # Save current page
            self.current = self.forward_stack.pop()  # Move forward
            steps -= 1
        return self.current

# Example usage
browser = BrowserHistory("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
print(browser.back(1))  # Returns "youtube.com"
print(browser.back(1))  # Returns "google.com"
print(browser.forward(1))  # Returns "youtube.com"
browser.visit("linkedin.com")  # Clears forward history
print(browser.forward(1))  # Still returns "linkedin.com" as forward history was cleared




def setZeroes(matrix):
    n, m = len(matrix), len(matrix[0])
    col0 = 1  # Flag to track if the first column should be zeroed

    # Step 1: Mark rows and columns that should be zeroed using the first row and first column
    for i in range(n):
        if matrix[i][0] == 0:
            col0 = 0  # First column should be zeroed
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row
                matrix[0][j] = 0  # Mark column

    # Step 2: Update matrix based on markers (excluding first row & column)
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle the first row
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Step 4: Handle the first column
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
setZeroes(matrix)

# Print the modified matrix
for row in matrix:
    print(row)






def longest_subarray_with_sum_k(arr, k):
    pre_sum_map = {}
    sum_ = 0
    max_len = 0

    for i, num in enumerate(arr):
        sum_ += num
        print("sum_",sum_)

        if sum_ == k:
            max_len = i + 1

        if (sum_ - k) in pre_sum_map:
            max_len = max(max_len, i - pre_sum_map[sum_ - k])

        if sum_ not in pre_sum_map:
            pre_sum_map[sum_] = i

    return max_len

arr = [3, 1, 2, 5, 1]
k = 8
print(longest_subarray_with_sum_k(arr, k))  # Output: 3






