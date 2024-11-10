import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/lainguyn123/student-performance-factors/versions/6/StudentPerformanceFactors.csv')
df = df.loc[df["Exam_Score"] >= 90]

print("Average Hours Studied:", df["Hours_Studied"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Average Sleep Hours:", df["Sleep_Hours"].mean())
print("Average Physical Activity:", df["Physical_Activity"].mean())
print()

print(df.columns)