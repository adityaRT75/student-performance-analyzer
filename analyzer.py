import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("students.csv")

# Calculate average marks
data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)

print("\nStudent Averages:\n", data[["Name", "Average"]])

# Find top student
top_student = data.loc[data["Average"].idxmax()]
print("\nTop Student:")
print(top_student["Name"], "with average", top_student["Average"])

# Subject-wise average
subject_avg = data[["Maths", "Science", "English"]].mean()
print("\nSubject Averages:\n", subject_avg)

# Plot graph
subject_avg.plot(kind='bar')
plt.title("Subject Average Marks")
plt.ylabel("Marks")
plt.show()