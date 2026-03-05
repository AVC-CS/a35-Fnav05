import pytest
import re


def regex_test(expected, lines):
    i = 0
    match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


def parse_result(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    return lines


@pytest.mark.T1
def test_main_1():
    """Line 1 must contain 3 integers and line 2 must contain 2 integers."""
    lines = parse_result('result1.txt')
    print(lines)
    # First line has numbers, second line has numbers
    regex_test([r'\d+\s+\d+\s+\d+', r'\d+\s+\d+'], lines)


@pytest.mark.T2
def test_main_2():
    """All 3 random numbers on line 1 must be between 0 and 99."""
    lines = parse_result('result2.txt')
    print(lines)
    assert len(lines) >= 1, "Expected at least 1 line of output"
    nums = re.findall(r'\d+', lines[0])
    assert len(nums) == 3, f"Expected 3 numbers on line 1, got: {lines[0]}"
    for n in nums:
        val = int(n)
        assert 0 <= val <= 99, f"Random number {val} is not in range [0, 99]"


@pytest.mark.T3
def test_main_3():
    """Total on line 2 must equal the sum of the 3 numbers on line 1."""
    lines = parse_result('result3.txt')
    print(lines)
    assert len(lines) >= 2, "Expected at least 2 lines of output"
    nums1 = re.findall(r'\d+', lines[0])
    nums2 = re.findall(r'\d+', lines[1])
    assert len(nums1) == 3, f"Expected 3 numbers on line 1, got: {lines[0]}"
    assert len(nums2) >= 1, f"Expected numbers on line 2, got: {lines[1]}"
    expected_total = int(nums1[0]) + int(nums1[1]) + int(nums1[2])
    actual_total = int(nums2[0])
    assert actual_total == expected_total, \
        f"Total mismatch: expected {expected_total}, got {actual_total}"


@pytest.mark.T4
def test_main_4():
    """Average on line 2 must equal total // 3 of the 3 numbers on line 1."""
    lines = parse_result('result4.txt')
    print(lines)
    assert len(lines) >= 2, "Expected at least 2 lines of output"
    nums1 = re.findall(r'\d+', lines[0])
    nums2 = re.findall(r'\d+', lines[1])
    assert len(nums1) == 3, f"Expected 3 numbers on line 1, got: {lines[0]}"
    assert len(nums2) == 2, f"Expected 2 numbers on line 2, got: {lines[1]}"
    expected_total = int(nums1[0]) + int(nums1[1]) + int(nums1[2])
    expected_avg = expected_total // 3
    actual_avg = int(nums2[1])
    assert actual_avg == expected_avg, \
        f"Average mismatch: expected {expected_avg}, got {actual_avg}"
