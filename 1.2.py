import ReadFile
import Reduction

s = 'X23.xlsx'
u = ReadFile.read_xlsx_row(s)
rs = len(u[0])
C, D = ReadFile.cd(u, 1, rs - 2, rs - 1, rs - 1)
R = Reduction.pos(u, C, D)
print(len(u)-1)
print(len(R))
