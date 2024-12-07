def evaluate(target, nums, val = 0):
    if len(nums) == 0: return val == target
    if val > target: return False

    return (
        evaluate(target, nums[1:], int(str(val) + str(nums[0]))) or # Concatenation
        evaluate(target, nums[1:], val * nums[0]) or # Multiplication
        evaluate(target, nums[1:], val + nums[0]) # Addition
    )

def main():
    ans = 0
    with open("input.txt") as file:
        for line in file:
            target, nums = line.split(": ")
            target = int(target)
            nums = [int(num) for num in nums.split(" ")]
            if evaluate(target, nums): ans += target
    return ans

if __name__ == "__main__":
    ans = main()
    print(f"The answer is {ans}")