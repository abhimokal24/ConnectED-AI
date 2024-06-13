import csv
import pandas as pd
from faker import Faker
import random

fake = Faker('en_IN')  # Set the locale to India

def calculate_percentage(study_hours):
    if study_hours == 0:
        return round(random.uniform(20, 40), 2)
    elif 0 < study_hours <= 1.5:
        return round(random.uniform(50, 60), 2)
    elif 1.5 < study_hours <= 3:
        return round(random.uniform(60, 80), 2)
    else:
        return round(random.uniform(80, 100), 2)

def calculate_subject_marks(age, percentage):
    if age == 15:
        return {
            'marathi_marks': round(random.uniform(20, 40)),
            'hindi_marks': round(random.uniform(30, 50)),
            'english_marks': round(random.uniform(40, 60)),
            'science_marks': round(random.uniform(50, 70)),
            'mathematics_marks': round(random.uniform(60, 80)),
            'social_studies_marks': round(random.uniform(30, 50))
        }
    elif age == 16:
        return {
            'marathi_marks': round(random.uniform(30, 50)),
            'hindi_marks': round(random.uniform(40, 60)),
            'english_marks': round(random.uniform(50, 70)),
            'science_marks': round(random.uniform(60, 80)),
            'mathematics_marks': round(random.uniform(70, 90)),
            'social_studies_marks': round(random.uniform(40, 60))
        }
    else:
        # For age 17 and other cases
        return {
            'marathi_marks': round(random.uniform(40, 60)),
            'hindi_marks': round(random.uniform(50, 70)),
            'english_marks': round(random.uniform(60, 80)),
            'science_marks': round(random.uniform(70, 90)),
            'mathematics_marks': round(random.uniform(80, 100)),
            'social_studies_marks': round(random.uniform(50, 70))
        }

def generate_data(num_points):
    data = []
    used_ids = set()  # Set to keep track of generated IDs
    used_contact_numbers = set()  # Set to keep track of generated contact numbers
    
    # List of states with varying frequencies
    state_distribution = ['Maharashtra'] * 25 + ['Karnataka'] * 15 + ['Gujarat'] * 15 + ['Rajasthan'] * 15 + ['Kerala'] * 15 + ['Punjab'] * 8 + ['Sikkim'] * 8 + ['Haryana'] * 8 + ['Bihar'] * 8 + ['Goa'] * 8 + ['Other'] * 4
    
    for _ in range(num_points):
        while True:
            student_id = fake.random_number(12)  # Generate a 12-digit student ID
            if student_id not in used_ids:
                used_ids.add(student_id)
                break
        
        while True:
            contact_number = fake.random_number(10)  # Generate a 10-digit contact number
            if contact_number not in used_contact_numbers:
                used_contact_numbers.add(contact_number)
                break
        
        name = fake.name()
        state = random.choice(state_distribution)  # Randomly choose state based on the distribution
        age = fake.random_element(elements=[15] * 3 + [16] * 2 + [17])  # Generate age based on the specified distribution
        gender = fake.random_element(elements=['Male'] * 56 + ['Female'] * 44)  # Randomly choose gender based on the distribution
        
        # Generate study hours with specified distribution
        study_hours_distribution = [0] * 5 + [round(random.uniform(1, 4), 2) for _ in range(70)] + [round(random.uniform(4, 8), 2) for _ in range(5)]
        study_hours = random.choice(study_hours_distribution)
        
        # Calculate percentage based on study hours
        percentage = calculate_percentage(study_hours)
        
        # Calculate subject-wise marks based on age and percentage
        subject_marks = calculate_subject_marks(age, percentage)
        
        data.append({
            'studentID': student_id,
            'name': name,
            'state': state,
            'contact_number': contact_number,
            'age': age,
            'gender': gender,
            'study_hours': study_hours,
            'percentage': percentage,
            **subject_marks
        })
    
    return data

# Generate 90,000 data points
num_points = 5000
dataset = generate_data(num_points)

# Save the dataset to a CSV file (StudentMarks.csv)
csv_file_path = 'StudentMarks.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['studentID', 'name', 'state', 'contact_number', 'age', 'gender', 'study_hours', 'percentage',
                  'marathi_marks', 'hindi_marks', 'english_marks', 'science_marks', 'mathematics_marks', 'social_studies_marks']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for data_point in dataset:
        writer.writerow(data_point)

print(f'Data has been saved to {csv_file_path}')

# Display the head of the dataset using pandas
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
print(df.head())