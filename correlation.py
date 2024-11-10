import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/lainguyn123/student-performance-factors/versions/6/StudentPerformanceFactors.csv')

corre_map = df.corr()
sn.heatmap(corre_map, annot=True)

figure = plt.gcf()
figure.set_size_inches(12, 10)
plt.savefig("data/correlation_map.png", dpi=100)
plt.close()
#The best indicator of test scores are the hours studied and the attendance 