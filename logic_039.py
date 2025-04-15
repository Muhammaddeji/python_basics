import datetime
import random

def to_uppercase(text):
    return text.upper()

def get_today_date():
    return datetime.date.today().strftime("2025-04-14")

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def get_random_number():
    return random.randint(1, 100)

def get_full_name():
    return "Adegbite Sheriff Adedeji"
