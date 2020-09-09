import pandas as pd

dfOrigem = pd.read_csv("dataCSV/breast-cancer.csv", index_col=0)

'''
1. Sample code number: id number
2. Clump Thickness: 1 - 10
3. Uniformity of Cell Size: 1 - 10
4. Uniformity of Cell Shape: 1 - 10
5. Marginal Adhesion: 1 - 10
6. Single Epithelial Cell Size: 1 - 10
7. Bare Nuclei: 1 - 10
8. Bland Chromatin: 1 - 10
9. Normal Nucleoli: 1 - 10
10. Mitoses: 1 - 10
11. Class: (2 for benign, 4 for malignant)

'''

dfOrigem.columns = ['Clump-Thickness', 'Cell-Size', 'Cell-Shape', 'Marginal-Adhesion', 'Epithelial-Cell-Size', 'Bare-Nuclei', 'Bland-Chromatin', 'Normal-Nucleoli', 'Mitoses', 'Class']

dfOrigem.index.name = 'id'

print(dfOrigem)
            
dfOrigem.to_csv('dataCSV/FixedDatabase.csv')