import ReadFile
import Reduction

s = 'X21.xlsx'
u = ReadFile.read_xlsx_row(s)
rs = len(u[0])
C, D = ReadFile.cd(u, 1, rs - 2, rs - 1, rs - 1)
R = Reduction.mibark_reduction(u, C, D)
print(R)
