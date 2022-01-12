def get_n_element_rec(nums, n):     # does not work for get_n_element_rec([1, 3, 2], 2020)
    if n < len(nums):
        return nums[n - 1]
    last = nums[-1]
    if last_right_index(nums[:-1], last) != -1:
        curr = len(nums) - (last_right_index(nums[:-1], last) + 1)
        return get_n_element_rec(nums + [curr], n)
    return get_n_element_rec(nums + [0], n)


def get_n(nums, n):
    if len(nums) == 1:
        return 0
    i = len(nums)
    while i < n:
        last = nums[-1]
        if last_right_index(nums[:-1], last) != -1:
            curr = len(nums) - (last_right_index(nums[:-1], last) + 1)
            nums.append(curr)
        else:
            nums.append(0)
        i += 1
    return nums[-1]


def last_right_index(nums, value):
    try:
        return len(nums) - nums[::-1].index(value) - 1
    except ValueError:
        return -1


def main():
    assert 1 == get_n([1, 3, 2], 2020)
    assert 10 == get_n([2, 1, 3], 2020)
    assert 27 == get_n([1, 2, 3], 2020)
    assert 78 == get_n([2, 3, 1], 2020)
    assert 438 == get_n([3, 2, 1], 2020)
    assert 1836 == get_n([3, 1, 2], 2020)


if __name__ == '__main__':
    main()
