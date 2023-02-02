import copy


def ind(u, S):
    R = []
    l = []
    for i in S:
        l.append(u[0].index(i))
    u1 = []
    for i in u:
        if not i:
            u1.append([])
            continue
        l1 = []
        for j in l:
            l1.append(i[j])
        u1.append(l1)
    for i in range(1, len(u1)):
        if not u1[i]:
            continue
        e = 1
        for j in R:
            if u1[int(list(j)[0])] == u1[i]:
                j.add(i)
                e = 0
        if e == 1:
            R.append({i})
    return R


def is_equal_ind(l1, l2):
    if len(l1) != len(l2):
        return False
    l3 = copy.deepcopy(l2)
    for i in l1:
        if i not in l3:
            return False
        else:
            l3.remove(i)
    if not l3:
        return True
    else:
        return False
