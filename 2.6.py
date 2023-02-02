import Reduction
import ReadFile
import time

s = 'X23.xlsx'
u = ReadFile.read_xlsx_row(s)
rs = len(u[0])
C, D = ReadFile.cd(u, 1, rs - 2, rs - 1, rs - 1)
start = time.time()
R = Reduction.red_relationship_preservation(u, C, D)
end = time.time()
print(end - start)
for i in R:
    print(i)
print(len(R))
