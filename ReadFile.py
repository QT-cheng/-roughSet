import xlrd


def read_xlsx_col(s):
    workbook = xlrd.open_workbook(s)
    X = workbook.sheet_by_name('Sheet1')
    u = []
    for i in range(X.ncols):
        u.append(X.col_values(i))
    return u


def read_xlsx_row(s):
    workbook = xlrd.open_workbook(s)
    X = workbook.sheet_by_name('Sheet1')
    u = []
    for i in range(X.nrows):
        u.append(X.row_values(i))
    return u


def cd(u, cl, cr, dl, dr):
    C = set()
    D = set()
    for i in range(cl, cr + 1):
        C.add(u[0][i])
    for i in range(dl, dr + 1):
        D.add(u[0][i])
    return C, D
