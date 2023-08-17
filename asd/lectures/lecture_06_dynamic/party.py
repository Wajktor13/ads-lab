"""
zbiory wierzchołków niezależnych w drzewie o mkasymalnym współczynniku
rekurencja ze spamiętywaniem w grafie
"""


class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.empl =[]
        self.f = -1
        self.g = -1


def max_fun_not_going(v):
    if v.g != -1:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += max_fun(u)
    return v.g


def max_fun(v):
    if v.f != -1:
        return v.f
    f1 = max_fun_not_going(v)
    f2 = v.fun
    for u in v.emp:
        f2 += max_fun_not_going(u)
    v.f = max(f1, f2)
    return v.f
