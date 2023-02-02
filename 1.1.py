import ReadFile
import Classification

s = 'X6.xlsx'
u = ReadFile.read_xlsx_row(s)
C, D = ReadFile.cd(u, 1, 16, 17, 17)
R = Classification.ind(u, C)
print(R)
