import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import random

def train_and_predict_study_hours():
    # Load the dataset
    df = pd.read_csv('semvii_studentdata.csv')

    # Define features (X) and target variable (y)
    X = df[['age', 'total_marks', 'percentage']]
    y = df['study_hour']

    # Check for null values in the dataset
    print("Null values in the dataset:")
    print(df.isnull().sum())

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Linear Regression model
    model = LinearRegression()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict study hours on the test set
    y_pred = model.predict(X_test)

    # Compare predicted study hours with actual study hours
    comparison_df = pd.DataFrame({'Actual Study Hours': y_test, 'Predicted Study Hours': y_pred})
    print("\nComparison of Actual and Predicted Study Hours:")
    print(comparison_df.head())

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nMean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Ask the user for the desired CGPA
    desired_cgpa = float(input("\nEnter the desired CGPA (within 10): "))

    # Predict study hours for the desired CGPA with a random value after the decimal
    if desired_cgpa <= 4.0:
        predicted_study_hours = round(random.uniform(0, 1), 2)
    elif 4.0 < desired_cgpa <= 5.5:
        predicted_study_hours = round(random.uniform(1.5, 2.5), 2)
    elif 5.5 < desired_cgpa <= 7.5:
        predicted_study_hours = round(random.uniform(3.0, 4.0), 2)
    else:
        predicted_study_hours = round(random.uniform(4.5, 5.5), 2)

    print(f"\nPredicted Study Hours to achieve CGPA {desired_cgpa}: {predicted_study_hours} hours")

    # Daily schedule based on predicted study hours
    print("\nDaily Schedule:")
    if predicted_study_hours > 4.0:
        print("""
        Morning:
        6:00 AM - 6:30 AM: Wake up and morning routine
        6:30 AM - 7:00 AM: Breakfast

        College/Classes:
        8:00 AM - 5:00 PM: College/Classes

        Afternoon:
        5:00 PM - 6:00 PM: Free time/Commute back home
        6:00 PM - 7:00 PM: Dinner

        Evening Study Session:
        7:00 PM - 8:00 PM: CSS
        8:00 PM - 8:30 PM: Break/Snack
        8:30 PM - 9:30 PM: IVP

        Night Study Session:
        9:30 PM - 10:30 PM: ML
        10:30 PM - 11:00 PM: Break/Relaxation

        Before Bed:
        11:00 PM - 11:30 PM: DAV
        11:30 PM: Bedtime
        """)
    elif 2.0 <= predicted_study_hours <= 4.0:
        print("""
        Morning:
        7:00 AM - 7:30 AM: Wake up and morning routine
        7:30 AM - 8:00 AM: Breakfast

        College/Classes:
        8:00 AM - 5:00 PM: College/Classes

        Afternoon:
        5:00 PM - 6:00 PM: Free time/Commute back home
        6:00 PM - 6:30 PM: Dinner

        Evening Study Session:
        6:30 PM - 7:30 PM: CSS
        7:30 PM - 8:00 PM: Break/Snack
        8:00 PM - 9:00 PM: IVP

        Night Study Session:
        9:00 PM - 9:45 PM: ML
        9:45 PM - 10:00 PM: Break/Relaxation

        Before Bed:
        10:00 PM - 10:30 PM: DAV
        10:30 PM: Bedtime
        """)
    else:
        print("""
        Morning:
        6:00 AM - 6:30 AM: Wake up and morning routine
        6:30 AM - 7:00 AM: Breakfast

        College/Classes:
        8:00 AM - 5:00 PM: College/Classes

        Afternoon:
        5:00 PM - 6:00 PM: Free time/Commute back home
        6:00 PM - 6:30 PM: Dinner

        Evening Study Session:
        6:30 PM - 8:30 PM: CSS and IVP
        8:30 PM - 9:00 PM: Break/Snack

        Night Study Session:
        9:00 PM - 11:00 PM: ML and DAV
        11:00 PM - 11:30 PM: Break/Relaxation

        Before Bed:
        11:30 PM - 12:00 AM: Review/Plan for the next day
        12:00 AM: Bedtime
        """)

# Call the function to execute the code
train_and_predict_study_hours()
