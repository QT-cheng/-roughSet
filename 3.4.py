import ReadFile
import Reduction

s = 'X6.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 16, 17, 17)
R1 = Reduction.AI1_accelerator(u, C, D)
R2 = Reduction.AIQ1_accelerator(u, C, D)
print(R1)
print(R2)