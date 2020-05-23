#!/usr/bin/python3
"""
Matrix_Mul module
Contains function for multiplying matrixes
"""


def matrix_mul(m_a, m_b):
    """
    Matrix Mul module
    Allows you to multiple two matrices
    """
    r = []
    m = []
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[], []] or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[], []] or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    try:
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
    except Exception:
        raise ValueError("m_a can't be empty")
    try:
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
    except Exception:
        raise ValueError("m_b can't be empty")
    leng = 0
    for row in m_a:
        if leng == 0:
            leng = len(row)
        elif leng != len(row):
            raise TypeError('each row of m_a must should be of the same size')
        for item in row:
            if not isinstance(item, int) and not isinstance(item, int):
                raise TypeError("m_a should contain only integers or floats")
    leng = 0
    for row in m_b:
        if leng == 0:
            leng = len(row)
        elif leng != len(row):
            raise TypeError('each row of m_b must should be of the same size')
        for item in row:
            if not isinstance(item, int) and not isinstance(item, int):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            sums = 0
            for k in range(len(m_b)):
                sums = sums+(m_a[i][k]*m_b[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m
