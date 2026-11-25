
# # import pandas as pd

# # Create CSV file
# csv_data = """StudentID,Name,Subject,Score
# 1,Ananya R,Math,85
# 2,Rahul K,Science,78
# 3,Priya S,English,92
# 4,Arjun M,Math,66
# 5,Sneha P,Science,74
# 6,Kiran L,English,88
# 7,Manish V,Math,59
# 8,Divya T,Science,81
# 9,Rohit G,English,95
# 10,Neha J,Math,72
# """

# with open("students_scores.csv", "w") as f:
#     f.write(csv_data)

# print("CSV file created!")

# # Read CSV file
# df = pd.read_csv("students_scores.csv")

# # Display first 5 rows
# print(df.head())










import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

# Load CSV
df = pd.read_csv("students_scores.csv")

# Display first 5 rows
print("\nStudent Data:")
print(df.head())

# Basic Analysis
average_score = df["Score"].mean()
highest_score = df.loc[df["Score"].idxmax()]
lowest_score = df.loc[df["Score"].idxmin()]

print("\nAverage Score:", average_score)
print("Highest Scorer:", highest_score["Name"], highest_score["Score"])
print("Lowest Scorer:", lowest_score["Name"], lowest_score["Score"])

# Generate PDF Report
pdf_file = "students_report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 750, "Student Test Score Report")

# Table Header
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 700, "ID")
c.drawString(100, 700, "Name")
c.drawString(250, 700, "Subject")
c.drawString(400, 700, "Score")

# Student Data
c.setFont("Helvetica", 12)
y = 680

for index, row in df.iterrows():
    c.drawString(50, y, str(row["StudentID"]))
    c.drawString(100, y, row["Name"])
    c.drawString(250, y, row["Subject"])
    c.drawString(400, y, str(row["Score"]))
    y -= 20

# Summary
c.setFont("Helvetica-Bold", 12)
c.drawString(50, y - 20, f"Average Score: {average_score:.2f}")
c.drawString(50, y - 40, f"Highest Score: {highest_score['Name']} ({highest_score['Score']})")
c.drawString(50, y - 60, f"Lowest Score: {lowest_score['Name']} ({lowest_score['Score']})")

c.save()

print("\nPDF Report generated:", pdf_file)
