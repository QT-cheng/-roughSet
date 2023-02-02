import ReadFile
import Reduction

s = 'X11.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 4, 5, 5)
R = Reduction.decision_preservation_incomplete_discernibility_matrix(u, C, D)
for i in R[1:]:
    print(i[1:])