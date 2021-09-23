from unittest import TestCase
from merge_sorted_array import merge


class test_merge_sorted_array(TestCase):
    """Test cases for the merge sorted array exercise."""

    # provided test cases
    def test_standard_input(self):
        self.assertEqual(merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3), [1, 2, 2, 3, 5, 6])

    def test_nums2_empty(self):
        self.assertEqual(merge(nums1=[1], m=1, nums2=[], n=0), [1])

    def test_nums1_placeholder_elements_only(self):
        self.assertEqual(merge(nums1=[0, 0, 0], m=0, nums2=[2, 5, 6], n=3), [2, 5, 6])

    def test_nums1_len_2_nums2_len1(self):
        self.assertEqual(merge(nums1=[1, 0], m=1, nums2=[2], n=1), [1, 2])
