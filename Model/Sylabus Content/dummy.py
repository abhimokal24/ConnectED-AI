import random
import pandas as pd

# Function to generate Indian full names
def generate_full_name():
    first_names = ["Aarav", "Vihaan", "Arnav", "Advik", "Reyansh", "Mohammad", "Aayan", "Aaryan", "Aryan", "Kabir", "Ritik", "Aarush", "Ishaan", "Shaurya", "Vivaan", "Vivaan", "Aadi", "Aarush", "Arjun", "Sai", "Pranav", "Aditya", "Vihaan", "Shreyansh", "Dhruv", "Atharva", "Darsh", "Kian", "Krish", "Rudra", "Ansh", "Anvi", "Aaradhya", "Aditi", "Saanvi", "Sara", "Shreya", "Ananya", "Aadhya", "Pihu", "Khushi", "Riya", "Nidhi", "Nandini", "Myra", "Jiya", "Neha"]
    last_names = ["Patel", "Shah", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Shah", "Patel", "Shah", "Sharma", "Patel", "Shah", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma", "Sharma", "Patel", "Shah", "Sharma"]

    full_name = random.choice(first_names) + " " + random.choice(last_names)
    return full_name

# Function to generate random age between 19 to 24
def generate_age():
    return random.randint(19, 24)

# Function to generate random gender with 44% male and 56% female
def generate_gender():
    gender = random.choices(["Male", "Female"], weights=[44, 56], k=1)
    return gender[0]

# Function to generate random marks for each subject
def generate_marks():
    return random.randint(0, 100)

# Generate student data
data = []
for _ in range(12424):
    name = generate_full_name()
    age = generate_age()
    gender = generate_gender()
    network_marks = generate_marks()
    web_marks = generate_marks()
    ml_marks = generate_marks()
    dwm_marks = generate_marks()
    stats_marks = generate_marks()
    total_marks = network_marks + web_marks + ml_marks + dwm_marks + stats_marks
    percentage = (total_marks / 500) * 100
    cgpa = round((percentage / 9.5), 2)  # Assuming 9.5 is the maximum percentage to get a CGPA of 10
    data.append([name, age, gender, network_marks, web_marks, ml_marks, dwm_marks, stats_marks, total_marks, percentage, cgpa])

# Create DataFrame
columns = ["Name", "Age", "Gender", "Computer Network", "Web Computing", "Machine Learning", "Data Warehouse and Mining", "Statistics", "Total", "Percentage", "CGPA"]
df = pd.DataFrame(data, columns=columns)

# Ensure at least 67% students have marks above 32 in each subject
df.loc[df["Computer Network"] < 33, "Computer Network"] = random.randint(33, 100)
df.loc[df["Web Computing"] < 33, "Web Computing"] = random.randint(33, 100)
df.loc[df["Machine Learning"] < 33, "Machine Learning"] = random.randint(33, 100)
df.loc[df["Data Warehouse and Mining"] < 33, "Data Warehouse and Mining"] = random.randint(33, 100)
df.loc[df["Statistics"] < 33, "Statistics"] = random.randint(33, 100)

# Correct total marks calculation
df["Total"] = df.iloc[:, 3:8].sum(axis=1)

# Save DataFrame to CSV
df.to_csv("student_data.csv", index=False)

print("Dataset created and saved as 'student_data.csv'")
