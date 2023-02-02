class Node:
    def __init__(self, val: list[set]):
        self.val = val
        self.l_child = []

    def add_child(self, node):
        self.l_child.append(node)


def read_tree(t: Node, s, R):
    for i in t.val:
        s = s | i
    if not t.l_child:
        R.append(s)
    else:
        for i in t.l_child:
            read_tree(i, s, R)


def to_tree(l):
    c = core(l)
    R = Node(c)
    l = difference(l, c, 0)
    a = maximum(l)
    while (set() not in l) and (len(l) != 0):
        child = Node(a)
        R.add_child(child)
        ex = exclude(l, a)
        if ex:
            child.add_child(to_tree(ex))
        l = difference(l, a, 1)
        if core(l):
            a = core(l)
        else:
            a = maximum(l)
    return R


def exclude(l, a):
    s = set()
    for i in a:
        s = s | i
    R = [i for i in l if not i & s]
    return R


def difference(l, a, p):
    s = set()
    for i in a:
        s = s | i
    R = []
    if p == 0:
        for i in l:
            if i - s:
                R.append(i - s)
    else:
        for i in l:
            R.append(i - s)
    return R


def core(l):
    R = []
    for i in l:
        if len(i) == 1:
            R.append(i)
    return R


def maximum(l):
    d = {}
    for i in l:
        for j in i:
            if j in d.keys():
                d[j] += 1
            else:
                d[j] = 1
    if not d.keys():
        return []
    m = max(d.values())
    k = [k0 for k0, v in d.items() if v == m]
    R = [{k[0]}]
    return R
