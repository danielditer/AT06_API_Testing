# Module ageCalculator

# Create 1 module to Calculate age in minutes, hours and days


# Calculates age in
def calculate_age_in_minutes(age: int):
    if age > -1: return age * 525600


# Calculates age in hours
def calculate_age_in_hours(age: int):
    if age > -1: return age * 8760


# Calculates age in days
def calculate_age_in_days(age: int):
    if age > -1: return age * 365
