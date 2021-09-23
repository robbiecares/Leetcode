from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # nums1 pointer
    h = 0

    # nums2 pointer
    j = 0

    complete = False
    while not complete:
        # edgecase - nums2 is empty
        if not nums2:
            complete = True
            continue

        # edgecase - nums1 only contains placeholder elements
        if m == 0:
            nums1[:] = nums2
            complete = True
            continue

        while h < m + n:
            # case - the end of nums1 is found. Add the remaining nums2 elements to nums1
            if nums1[h] == 0:
                nums1[h:] = nums2[j:]
                h += len(nums2[j:])
                break

            # case - nums2 element needs to be merged into nums1
            if nums1[h] > nums2[j]:
                nums1.insert(nums2[j], h)
                j += 1
            h += 1
        complete = True

    return nums1


if __name__ == '__main__':
    merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)