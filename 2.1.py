import Reduction
import ReadFile

s = 'X6.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 16, 17, 17)
R = Reduction.discernibility_matrix(u, C)
for i in R[1:]:
    print(i[1:])
