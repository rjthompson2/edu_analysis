import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

def start(lower_amount, upper_amount):
    df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/lainguyn123/student-performance-factors/versions/6/StudentPerformanceFactors.csv')
    df = df.loc[df["Exam_Score"] >= lower_amount]
    df = df.loc[df["Exam_Score"] <= upper_amount]

    print("Average Hours Studied:", df["Hours_Studied"].mean())
    print("Average Attendance:", df["Attendance"].mean())
    print("Average Sleep Hours:", df["Sleep_Hours"].mean())
    # print()

    # print(df.columns)

if __name__ == "__main__":
    lower_amount = input("Enter the lower score to filter: ")
    upper_amount = input("Enter the upper score to filter: ")
    try:
        start(int(lower_amount), int(upper_amount))
    except:
        start(90, 100)

# Interested discovery:
# People who score between 90-100 study less, have lower attendance, and sleep less on average than those who score 70-80
