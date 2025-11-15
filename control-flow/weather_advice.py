#!/usr/bin/env python3
# This script uses conditional statements (if/elif/else) to provide
# clothing recommendations based on user input regarding the weather.

# Prompt user for input, ensuring the input is stripped of whitespace
# and converted to lowercase for case-insensitive checking.
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Use conditional statements to check the weather condition
if weather == "sunny":
    # Recommendation for sunny weather
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    # Recommendation for rainy weather
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    # Recommendation for cold weather
    print("Make sure to wear a warm coat and a scarf.")

else:
    # Handles any input that doesn't match the predefined conditions
    print("Sorry, I don't have recommendations for this weather.")