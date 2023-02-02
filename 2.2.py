import Reduction
import ReadFile

s = 'X12.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 19, 20, 20)
R = Reduction.red_discernibility_matrix(u, C)
for i in R:
    print(i)
