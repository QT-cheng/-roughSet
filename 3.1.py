import ReadFile
import Reduction

s = 'X11.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 4, 0, 0)
R = Reduction.s_incomplete(u, C)
for i in R[1:]:
    print(i)
