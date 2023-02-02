import Reduction
import ReadFile

s = 'X6.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 16, 17, 17)
R = Reduction.relative_red_tree(u, C, D)
for i in R:
    print(i)

