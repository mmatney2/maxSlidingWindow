import collections
def maxSlide(nums, k):
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        # print(r)
        # print(r)
        while q and nums[q[-1]] < nums[r]:
            # print(nums[r])
            # print(q[-1])
            # print(nums[q[-1]])
            q.pop()
        q.append(r)
        # print(q)

        if l > q[0]:
            print(q[0])
            q.popleft()
            # print(q)
        if  (r + 1) >= k:
            output.append(nums[q[0]])
            # print(output)
            l += 1
        r += 1
    return output
print(maxSlide([2,4,6,9], 2))