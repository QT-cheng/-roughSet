import Classification
import ReductionTree
import math
import copy


def pos(u, C, D):
    rc = Classification.ind(u, C)
    rd = Classification.ind(u, D)
    R = set()
    for i in rc:
        for j in rd:
            if i <= j:
                R.update(i)
    return R


def pos_incomplete(u, C, D):
    rd = Classification.ind(u, D)
    R = set()
    for i in rd:
        for j in range(1, len(u)):
            if t_incomplete(u, j, C) <= i:
                R.add(j)
    return R


def discernibility_matrix(u, C):
    R = []
    for i in u:
        u0 = []
        for j in u:
            u0.append(set())
        R.append(u0)
    for i in C:
        u1 = Classification.ind(u, {i})
        r1 = u1[0]
        for j in range(1, len(u1)):
            r2 = u1[j]
            for k in r1:
                for l in r2:
                    x, d = min(k, l), max(k, l)
                    R[d][x].add(i)
            r1.update(r2)
    return R


def region_preservation_discernibility_matrix(u, C, D):
    R = relationship_preservation_discernibility_matrix(u, C, D)
    p = pos(u, C, D)
    hc = Classification.ind(u, C)
    for j in range(1, len(R)):
        for i in range(j + 1, len(R)):
            di = [z for z in hc if i in z][0]
            dj = [z for z in hc if j in z][0]
            if not ((di <= p) or (dj <= p)):
                R[i][j].clear()
    return R


def decision_preservation_discernibility_matrix(u, C, D):
    R = discernibility_matrix(u, C)
    hc = Classification.ind(u, C)
    ld = []
    for i in range(len(u[0])):
        if u[0][i] in D:
            ld.append(i)
    for j in range(1, len(R)):
        for i in range(j + 1, len(R)):
            di = [z for z in hc if i in z][0]
            dj = [z for z in hc if j in z][0]
            si, sj = set(), set()
            for k0 in di:
                rd = ''
                for k1 in ld:
                    rd += (str(u[k0][k1]) + ';')
                si.add(rd)
            for k0 in dj:
                rd = ''
                for k1 in ld:
                    rd += (str(u[k0][k1]) + ';')
                sj.add(rd)
            if si == sj:
                R[i][j].clear()
    return R


def relationship_preservation_discernibility_matrix(u, C, D):
    R = discernibility_matrix(u, C)
    r0 = Classification.ind(u, D)
    for i in r0:
        u1 = list(i)
        for j in range(len(u1)):
            for k in range(j + 1, len(u1)):
                x, d = min(u1[j], u1[k]), max(u1[j], u1[k])
                R[d][x].clear()
    return R


def incomplete_discernibility_matrix(u, C):
    R = []
    for i in u:
        u0 = []
        for j in u:
            u0.append(set())
        R.append(u0)
    lc = []
    for i in range(1, len(u[0])):
        if u[0][i] in C:
            lc.append(i)
    for j in range(1, len(u)):
        for i in range(j + 1, len(u)):
            for k in lc:
                if (u[i][k] != u[j][k]) and (u[i][k]) and (u[j][k]):
                    R[i][j].add(u[0][k])
    return R


def region_preservation_incomplete_discernibility_matrix(u, C, D):
    R = relationship_preservation_incomplete_discernibility_matrix(u, C, D)
    ld = []
    po = pos_incomplete(u, C, D)
    for i in range(1, len(u[0])):
        if u[0][i] in D:
            ld.append(i)
    for j in range(1, len(R)):
        for i in range(j + 1, len(R)):
            if not ((t_incomplete(u, i, C) <= po) or (t_incomplete(u, j, C) <= po)):
                R[i][j].clear()
    return R


def decision_preservation_incomplete_discernibility_matrix(u, C, D):
    R = incomplete_discernibility_matrix(u, C)
    ld = []
    for i in range(1, len(u[0])):
        if u[0][i] in D:
            ld.append(i)
    for j in range(1, len(R)):
        for i in range(j + 1, len(R)):
            if ee_incomplete(u, i, C, D) == ee_incomplete(u, j, C, D):
                R[i][j].clear()
    return R


def relationship_preservation_incomplete_discernibility_matrix(u, C, D):
    R = incomplete_discernibility_matrix(u, C)
    ld = []
    for i in range(1, len(u[0])):
        if u[0][i] in D:
            ld.append(i)
    for j in range(1, len(R)):
        for i in range(j + 1, len(R)):
            e = 1
            for k in ld:
                if u[i][k] != u[j][k]:
                    e = 0
            if e == 1:
                R[i][j].clear()
    return R


def core_discernibility_matrix(u, C):
    R = set()
    M = discernibility_matrix(u, C)
    for i in M:
        for j in i:
            if len(j) == 1:
                R.update(j)
    return R


def relative_core_discernibility_matrix(u, C, D):
    R = set()
    M = relationship_preservation_discernibility_matrix(u, C, D)
    for i in M:
        for j in i:
            if len(j) == 1:
                R.update(j)
    return R


def red_discernibility_matrix(u, C):
    m = discernibility_matrix(u, C)
    r0 = []
    for i in m:
        for j in i:
            if j and (j not in r0):
                r0.append(j)
    r = list_of_set_concise(r0)
    R = cnf_to_dnf(r)
    return R


def red_region_preservation(u, C, D):
    m = region_preservation_discernibility_matrix(u, C, D)
    r0 = []
    for i in m:
        for j in i:
            if j and (j not in r0):
                r0.append(j)
    r = list_of_set_concise(r0)
    R = cnf_to_dnf(r)
    return R


def red_decision_preservation(u, C, D):
    m = decision_preservation_discernibility_matrix(u, C, D)
    r0 = []
    for i in m:
        for j in i:
            if j and (j not in r0):
                r0.append(j)
    r = list_of_set_concise(r0)
    R = cnf_to_dnf(r)
    return R


def red_relationship_preservation(u, C, D):
    m = relationship_preservation_discernibility_matrix(u, C, D)
    r0 = []
    for i in m:
        for j in i:
            if j and (j not in r0):
                r0.append(j)
    r = list_of_set_concise(r0)
    R = cnf_to_dnf(r)
    return R


def red_enum(u, S):
    R = []
    R1 = enum_attribute(S)
    b = Classification.ind(u, S)
    for i in R1:
        if Classification.is_equal_ind(Classification.ind(u, i), b) and is_independent(u, i):
            R.append(i)
    return R


def relative_core(u, C, D):
    R = set()
    for i in C:
        if pos(u, C, D) != pos(u, C - {i}, D):
            R.add(i)
    return R


def relative_red_enum(u, C, D):
    c = relative_core(u, C, D)
    b = pos(u, C, D)
    a = C - c
    R1 = enum_attribute(a)
    for i in R1:
        i.update(c)
    R1.append(c)
    R = []
    for i in R1:
        if is_relative_independent(u, i, D) and pos(u, i, D) == b:
            R.append(i)
    return R


def enum_attribute(a):
    a1 = list(a)
    R = []
    for i in range(1, 2 ** len(a1)):
        i1 = i
        r = set()
        count = len(a1) - 1
        while i1 != 0:
            if i1 & 1:
                r.add(a1[count])
            count = count - 1
            i1 = i1 >> 1
        R.append(r)
    return R


def relative_red_tree(u, C, D):
    m = relationship_preservation_discernibility_matrix(u, C, D)
    r0 = []
    for i in m:
        for j in i:
            if j and (j not in r0):
                r0.append(j)
    r2 = []
    for i in r0:
        r2 = r2 + [j for j in r0 if j > i]
    r = [j for j in r0 if j not in r2]
    R = []
    T = ReductionTree.to_tree(r)
    ReductionTree.read_tree(T, set(), R)
    R1 = []
    for i in R:
        R1 += [z for z in R if z > i]
    R = [z for z in R if z not in R1]
    return R


def attribute_reduction(u, C, D):
    M0 = []
    C = mibark_reduction(u, C, D)
    l = []
    lC = list(C)
    lC = sorted(lC)
    lD = list(D)
    lD = sorted(lD)
    A = lC + lD
    for i in A:
        l.append(u[0].index(i))
    for i in u:
        l0 = []
        for j in l:
            l0.append(i[j])
        M0.append(l0)
    for i in M0[1:]:
        if M0.count(i) > 1:
            M0.remove(i)
    M1 = [[u[0][0]] + M0[0]]
    for i in range(1, len(M0)):
        M1.append([i] + M0[i])
    Fc = [set()]
    S = set()
    for i in range(1, len(M1)):
        S.add(i)
    for i in range(1, len(M1)):
        dh = [s for s in Classification.ind(M1, D) if i in s]
        dt = dh[0]
        cc = set()
        for j in C:
            ch = [s for s in Classification.ind(M1, C - {j}) if i in s]
            ct = ch[0]
            if not (ct <= dt):
                cc.add(j)
        Fc.append(cc)
    F = [M1[0]]
    for i in range(1, len(Fc)):
        g = enum_attribute(C - Fc[i])
        for j in g:
            j.update(Fc[i])
        g.append(Fc[i])
        for j in g:
            if is_relative_reduction_attribute(M1, i, j, D):
                l0 = [i]
                for k in lC:
                    if k in j:
                        l0.append(M1[i][M1[0].index(k)])
                    else:
                        l0.append('x')
                for k in lD:
                    l0.append(M1[i][M1[0].index(k)])
                F.append(l0)
    F0 = []
    for i in F:
        F0.append(i[1:])
    zi = {}
    zm = {}
    for i in F[1:]:
        if i[0] in zm.keys():
            if zm[i[0]] < F0.count(i[1:]):
                zm[i[0]] = F0.count(i[1:])
                zi[i[0]] = i[1:]
        else:
            zm[i[0]] = F0.count(i[1:])
            zi[i[0]] = i[1:]
    R = [F[0]]
    for i in zi.values():
        R.append(i)
    R1 = []
    for i in R:
        if i not in R1:
            R1.append(i)
    R = R1
    for i in range(1, len(R)):
        R[i] = [i] + R[i]
    return R


def list_of_set_concise(l):
    l2 = []
    for i in l:
        l2 = l2 + [j for j in l if j > i]
    R1 = [j for j in l if j not in l2]
    R = []
    for i in R1:
        if i not in R:
            R.append(i)
    return R


def cnf_to_dnf(l):
    first = l[0]
    R = []
    for i in first:
        R.append({i})
    for i in l[1:]:
        R1 = []
        for j in i:
            for k in R:
                if (k | {j}) not in R1:
                    R1.append(k | {j})
        R = list_of_set_concise(R1)
    return R


def is_independent(u, S):
    b = Classification.ind(u, S)
    for i in S:
        if Classification.is_equal_ind(Classification.ind(u, S - {i}), b):
            return False
    return True


def is_relative_independent(u, C, D):
    b = pos(u, C, D)
    for i in C:
        if b == pos(u, C - {i}, D):
            return False
    return True


def is_relative_reduction_attribute(u, x, C, D):
    dh = [s for s in Classification.ind(u, D) if x in s]
    dt = dh[0]
    ch = [s for s in Classification.ind(u, C) if x in s]
    ct = ch[0]
    if not (ct <= dt):
        return False
    for i in C:
        ch = [s for s in Classification.ind(u, C - {i}) if x in s]
        ct = ch[0]
        if ct <= dt:
            return False
    return True


def s_incomplete(u, C):
    lc = []
    for i in range(1, len(u[0])):
        if u[0][i] in C:
            lc.append(i)
    R = [set()]
    for i in range(1, len(u)):
        r = set()
        for j in range(1, len(u)):
            e = 1
            for k in lc:
                if not ((u[i][k] == u[j][k]) or (not u[i][k]) or (not u[j][k])):
                    e = 0
            if e == 1:
                r.add(j)
        R.append(r)
    return R


def t_incomplete(u, x, C):
    lc = []
    for i in range(1, len(u[0])):
        if u[0][i] in C:
            lc.append(i)
    R = set()
    for i in range(1, len(u)):
        e = 1
        for j in lc:
            if not ((u[x][j] == u[i][j]) or (not u[x][j]) or (not u[i][j])):
                e = 0
        if e == 1:
            R.add(i)
    return R


def ee_incomplete(u, x, C, D):
    t = t_incomplete(u, x, C)
    ld = []
    for i in range(1, len(u[0])):
        if u[0][i] in D:
            ld.append(i)
    R = set()
    for i in t:
        r = ''
        for j in ld:
            r += str(u[i][j]) + ';'
        R.add(r)
    return R


def mibark_reduction(u, C, D):
    c = relative_core_discernibility_matrix(u, C, D)
    B = c
    while I(u, B, D) < I(u, C, D):
        g = C - B
        z = {}
        for i in g:
            z[i] = c_I(u, i, D, B)
        m = max(z.values())
        mas = [k for k, v in z.items() if v == m]
        z = {}
        for i in mas:
            z[i] = len(Classification.ind(u, {i} | B))
        m = min(z.values())
        mis = [k for k, v in z.items() if v == m]
        p = mis[0]
        B.add(p)
    return B


def reduction_cebarkcc(u, C, D):
    c = relative_core_discernibility_matrix(u, C, D)
    Att = C - c
    B = c
    while c_H(u, D, B) > c_H(u, D, C):
        z = {}
        for i in Att:
            z[i] = c_H(u, D, B | {i})
        m = min(z.values())
        mis = [k for k, v in z.items() if v == m]
        z = {}
        for i in mis:
            z[i] = len(Classification.ind(u, {i} | B))
        m = min(z.values())
        mis = [k for k, v in z.items() if v == m]
        p = mis[0]
        B.add(p)
    return B


def reduction_cebarknc(u, C, D):
    S1 = c_H(u, D, C)
    s2 = {}
    for i in C:
        s2[i] = c_H(u, D, {i})
    S2 = sorted(s2.items(), key=lambda x: x[1])
    B = C
    for i in S2:
        S31 = c_H(u, D, B - {i[0]})
        if S31 == S1:
            B = B - {i[0]}
    return B


def AI1_accelerator(u, C, D):
    R = set()
    for i in C:
        if sig_in(u, i, C, D) > 0:
            R.add(i)
    while I(u, R, D) < I(u, C, D):
        A = C - R
        d = {}
        for i in A:
            d[i] = sig_out(u, i, R, D)
        ma = max(d.values())
        a0 = [k for k, v in d.items() if v == ma][0]
        R.add(a0)
    return R


def AIQ1_accelerator(u, C, D):
    R = set()
    for i in C:
        if sig_in(u, i, C, D) > 0:
            R.add(i)
    Pi = [R]
    ui = u
    while I(ui, R, D) < I(ui, C, D):
        p = pos(ui, Pi[-1], D)
        for j in ui:
            if not j:
                continue
            if j[0] in p:
                j.clear()
        A = C - R
        d = {}
        for j in A:
            d[j] = sig_out(ui, j, R, D)
        ma = max(d.values())
        a0 = [k for k, v in d.items() if v == ma][0]
        R.add(a0)
        Pi.append(Pi[-1] | {a0})
    return R


def sig_in(u, a, B, D):
    return c_H(u, D, B - {a}) - c_H(u, D, B)


def sig_out(u, a, B, D):
    return c_H(u, D, B) - c_H(u, D, B | {a})


def c_H(u, D, C):
    hCD, hC = Classification.ind(u, C | D), Classification.ind(u, C)
    HCD, HC = 0, 0
    for i in hC:
        b = len(i) / (len(u) - 1)
        HC = HC - b * math.log2(b)
    for i in hCD:
        b = len(i) / (len(u) - 1)
        HCD = HCD - b * math.log2(b)
    return HCD - HC


def I(u, C, D):
    hC, hD, hCD = Classification.ind(u, C), Classification.ind(u, D), Classification.ind(u, C | D)
    HC, HD, HCD = 0, 0, 0
    for i in hC:
        b = len(i) / (len(u) - 1)
        HC = HC - b * math.log2(b)
    for i in hD:
        b = len(i) / (len(u) - 1)
        HD = HD - b * math.log2(b)
    for i in hCD:
        b = len(i) / (len(u) - 1)
        HCD = HCD - b * math.log2(b)
    return HC + HD - HCD


def c_I(u, p, D, B):
    hpB = Classification.ind(u, {p} | B)
    hDB = Classification.ind(u, D | B)
    hpDB = Classification.ind(u, {p} | D | B)
    hB = Classification.ind(u, B)
    HpB, HDB, HpDB, HB = 0, 0, 0, 0
    for i in hpB:
        b = len(i) / (len(u) - 1)
        HpB = HpB - b * math.log2(b)
    for i in hDB:
        b = len(i) / (len(u) - 1)
        HDB = HDB - b * math.log2(b)
    for i in hpDB:
        b = len(i) / (len(u) - 1)
        HpDB = HpDB - b * math.log2(b)
    for i in hB:
        b = len(i) / (len(u) - 1)
        HB = HB - b * math.log2(b)
    return HpB + HDB - HpDB - HB
