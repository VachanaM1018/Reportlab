
import pandas as pd

# Create CSV file
csv_data = """StudentID,Name,Subject,Score
1,Ananya R,Math,85
2,Rahul K,Science,78
3,Priya S,English,92
4,Arjun M,Math,66
5,Sneha P,Science,74
6,Kiran L,English,88
7,Manish V,Math,59
8,Divya T,Science,81
9,Rohit G,English,95
10,Neha J,Math,72
"""

with open("students_scores.csv", "w") as f:
    f.write(csv_data)

print("CSV file created!")

# Read CSV file
df = pd.read_csv("students_scores.csv")

# Display first 5 rows
print(df.head())
