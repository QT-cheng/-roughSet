import Reduction
import ReadFile

s = 'X3.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 4, 5, 5)
R = Reduction.relative_core(u, C, D)
print(R)
