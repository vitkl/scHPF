#!/usr/bin/env python

import numpy as np
from numpy.testing import assert_equal

from schpf import max_pairwise, max_pairwise_table


def test_overlap():
    X = np.array([
            [0.33973751, 0.72029002, 0.52763837, 0.94012605, 0.20375346],
            [0.32460224, 0.43595206, 0.8304655 , 0.31792094, 0.77330563],
            [0.00507031, 0.42707696, 0.26948512, 0.50554657, 0.31438824],
            [0.52583849, 0.54531833, 0.08530654, 0.35516516, 0.10617843],
            [0.78608326, 0.59571929, 0.09737211, 0.09474643, 0.55319175],
            [0.04245016, 0.43322226, 0.99748447, 0.45731582, 0.65861378],
            [0.04364505, 0.97239799, 0.68847276, 0.96692073, 0.60268244],
            [0.13364376, 0.40121588, 0.32770517, 0.02352124, 0.04974099],
            [0.92531954, 0.23635494, 0.29327799, 0.40788107, 0.95974159],
            [0.42295065, 0.5725946 , 0.59206089, 0.76534785, 0.77961214]])
    assert_equal(max_pairwise(X, ntop=3)[0], 2)
    assert_equal(max_pairwise(X, ntop=3, second_greatest=True)[0], 1)


def test_overlap_table():
    X = np.array([
            [13, 11,  2, 13,  5, 12,  5],
            [ 8,  6,  0,  6,  8, 14,  6],
            [11, 13, 11, 11, 14,  8, 10],
            [ 1, 12,  8, 14,  7,  1,  3],
            [ 0,  1, 10, 12,  3,  5,  2],
            [ 3,  2,  6,  5,  9,  2,  1],
            [ 9,  3,  7,  2,  4,  3,  7],
            [ 4,  4, 12,  7, 13, 10,  0],
            [ 7,  0,  9,  8,  6,  6, 12],
            [14, 14, 13,  9, 10,  9, 14],
            [ 2,  9,  4, 10, 12,  7, 13],
            [ 6, 10,  3,  1,  0, 11,  4],
            [12,  8,  1,  0,  2, 13,  9],
            [ 5,  7, 14,  3, 11,  4, 11],
            [10,  5,  5,  4,  1,  0,  8] ])
    ntop_list = [1,2,3,4,5,6]
    table = max_pairwise_table(X, ntop_list=ntop_list)
    assert np.all(table.max_overlap >= table.max2_overlap)
    assert np.all(np.diff(table.max_overlap.values) >= 0 )
    assert np.all(np.diff(table.max2_overlap.values) >= 0 )

