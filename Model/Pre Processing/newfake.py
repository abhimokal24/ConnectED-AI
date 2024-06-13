from faker import Faker
import random
import pandas as pd

fake = Faker()

# Set seed for reproducibility
random.seed(42)

# Number of students
num_students = 1000

# Generate dataset
data = {
    'studentname': [fake.name() for _ in range(num_students)],
    'seatnumber': [random.randint(10000000, 99999999) for _ in range(num_students)],
    'age': random.choices([20, 21, 22], weights=[55, 19, 26], k=num_students),
}

# Generate subject-wise marks and study hours
subjects = ['CSS', 'DAV', 'IVP', 'ML', 'SEPM']
for subject in subjects:
    data[subject] = [random.randint(0, 80) for _ in range(num_students)]

# Ensure at least 15% students have marks less than 32 in at least one subject
for i in range(int(num_students * 0.15)):
    student_index = random.randint(0, num_students - 1)
    subject = random.choice(subjects)
    data[subject][student_index] = random.randint(0, 31)

# Ensure at least 2/3 of the students have more than 32 marks in each subject
for subject in subjects:
    for i in range(int(num_students * (2 / 3))):
        data[subject][i] = random.randint(33, 80)

# Generate study hours
data['study_hour'] = [round(random.uniform(0, 5), 2) for _ in range(num_students)]

# Calculate total marks
data['total_marks'] = [sum(data[subject][i] for subject in subjects) for i in range(num_students)]

# Generate percentage based on the formula
data['percentage'] = [(marks / 400) * 100 for marks in data['total_marks']]

# Generate CGPA based on the percentage with 2 digits after the decimal
data['CGPA'] = [round((percentage / 10), 2) for percentage in data['percentage']]

# Create DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('semvii_studentdata.csv', index=False)

# Display a message
print("Dataset saved as semvii_studentdata.csv")
