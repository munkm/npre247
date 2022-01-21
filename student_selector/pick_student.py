import pandas as pd

students = pd.read_csv("./roster.csv")

print(students.sample()['Name'].values[0])

