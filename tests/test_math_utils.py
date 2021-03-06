"""Test utils module."""

import itertools
import unittest

import numpy as np

from mano_pybullet.math_utils import joint2mat, mat2joint, mat2rvec, rvec2mat


class TestUtils(unittest.TestCase):
    """Test utils module."""

    def test_joint_mat_conversion(self):
        """Test joint to/from mat conversion."""
        angles1 = [1.1, 0.2, 2.3]
        for num in range(1, 4):
            for axes in itertools.combinations('xyz', num):
                mat = joint2mat(''.join(axes), angles1)
                angles2 = mat2joint(mat, ''.join(axes))
                np.testing.assert_almost_equal(angles1[:len(axes)], angles2[:len(axes)])

    def test_rvec_mat_conversion(self):
        """Test rotation vector to/from mat conversion."""
        mat = np.eye(3)
        np.testing.assert_almost_equal(mat, rvec2mat(mat2rvec(mat)))
        rvec = [1.1, 0.2, 2.3]
        np.testing.assert_almost_equal(rvec, mat2rvec(rvec2mat(rvec)))
