import functools

def main():
    ways = 0
    with open("input.txt") as file:
        for line in file:
            first, nums = line[:-1].split(" ")
            nums = [int(i) for i in nums.split(",")]
            ways += solve(first, tuple(nums))
    return ways

@functools.cache
def solve(part, nums):
    if nums == tuple(): return 0 if "#" in part else 1
    if part == "": return 0

    ans = 0
    for startPoint in range(0, len(part) - nums[0] + 1): # Iterate over all start points in part
        end = startPoint + nums[0] # Initial end point will be nums[0] after the start
        while end < len(part) and part[end] == "#": 
            end += 1 # Increase the end point while next char is #, to include # in current chunk

        chunk = part[startPoint : end]

        if len(chunk) == nums[0] and not any(j == "." for j in chunk): 
            # If chunk doesn't contain any . and is correct length, then can continue
            ans += solve(part[startPoint + nums[0] + 1:], nums[1:])

        # Can't skip over a # so if one comes up, this is the last possible start position
        if part[startPoint] == "#": break
    return ans

if __name__ == "__main__":
    print(f"The answer is {main()}")
