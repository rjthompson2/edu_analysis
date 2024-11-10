import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/lainguyn123/student-performance-factors/versions/6/StudentPerformanceFactors.csv')

print("Average Exam Score:", df["Exam_Score"].mean())
print()

print("Average Postgraduate Educated Parents Score:",df.loc[df['Parental_Education_Level'] == "Postgraduate"]["Exam_Score"].mean())
print("Average College Educated Parents Score:",df.loc[df['Parental_Education_Level'] == "College"]["Exam_Score"].mean())
print("Average High School Educated Parents Score:",df.loc[df['Parental_Education_Level'] == "High School"]["Exam_Score"].mean())
print()

print("Average Extracurricular Score:",df.loc[df['Extracurricular_Activities'] == "Yes"]["Exam_Score"].mean())
print("Average Non-Extracurricular Score:",df.loc[df['Extracurricular_Activities'] == "No"]["Exam_Score"].mean())
print()

print("Average No Learning Disability Score:",df.loc[df['Extracurricular_Activities'] == "No"]["Exam_Score"].mean())
print("Average Learning Disability Score:",df.loc[df['Extracurricular_Activities'] == "Yes"]["Exam_Score"].mean())
print()

print("Average Positive Influence Score:",df.loc[df['Peer_Influence'] == "Positive"]["Exam_Score"].mean())
print("Average Neutral Influence Score:",df.loc[df['Peer_Influence'] == "Neutral"]["Exam_Score"].mean())
print("Average Negative Influence Score:",df.loc[df['Peer_Influence'] == "Negative"]["Exam_Score"].mean())
print()

print("Average High Involvement Score:",df.loc[df['Parental_Involvement'] == "High"]["Exam_Score"].mean())
print("Average Medium Involvement Score:",df.loc[df['Parental_Involvement'] == "Medium"]["Exam_Score"].mean())
print("Average Low Involvement Score:",df.loc[df['Parental_Involvement'] == "Low"]["Exam_Score"].mean())
print()


print("Average High Quality Score:",df.loc[df['Teacher_Quality'] == "High"]["Exam_Score"].mean())
print("Average Medium Quality Score:",df.loc[df['Teacher_Quality'] == "Medium"]["Exam_Score"].mean())
print("Average Low Quality Score:",df.loc[df['Teacher_Quality'] == "Low"]["Exam_Score"].mean())
print()

print(df.columns)
print(df["Teacher_Quality"].unique())