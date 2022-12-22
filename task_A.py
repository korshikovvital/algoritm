def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        centre = (left + right) // 2
        if nums[centre] == target:
            return centre
        if nums[left] <= nums[centre]:
            if nums[left] <= target < nums[centre]:
                right = centre - 1
            else:
                left = centre + 1
        else:
            if nums[centre] < target <= nums[right]:
                left = centre + 1
            else:
                right = centre - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6