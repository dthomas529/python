# This programs prints a random recipe, including the name, cuisine, category, and instructions. 

import requests

response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
meals = response.json()['meals'][0]

# Test the JSON request
print(meals)

recipe = meals['strMeal']
category = meals['strCategory']
cuisine = meals['strArea']
instructions = meals['strInstructions']

print(f"Recipe: {recipe}")
print(f"Cuisine: {cuisine}")
print(f"Category: {category}")
print(f"Instructions: {instructions}")
