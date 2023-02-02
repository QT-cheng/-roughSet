import Reduction
import ReadFile

s = 'X10.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 2, 3, 3)
R = Reduction.region_preservation_discernibility_matrix(u, C, D)
for i in R[1:]:
    print(i[1:])
