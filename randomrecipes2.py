import tkinter as TK
import requests
from threading import Thread

api = ""
recipes = []  
recipe_number = ()

# Execute the program
window = tk.TK()
window.geometry("980x260")
window.title
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="grey")


def preload_recipes():
    global recipes

    print("***Loading more recipes***")
    for x in range (10):
        random_recipe = requests.get(api).json()
        content = random_recipe["content"]
        cuisine = random_recipe["cuisine"]
        recipe =  content + "\n" + "Cuisine: " + cuisine
        print(content)

        recipes.append(recipe)

    print("***Finished loading more recipes***")


preload_recipes()


def get_random_recipe():
    global recipe_label
    global recipes
    global recipe_number

    recipe_label.configure(text=recipes[recipe_number])
    recipe_number = recipe_number + 1
    print(recipe_number)

if recipes[recipe_number] == recipes[-3]:
    thread = Thread(target=preload_recipes)
    thread.start()




# UI
recipe_label = tk.label(window, text="Click on the button to a recipe", height=6, pady=10, wraplength=800, font=("Helvetica", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)


button = tk.Button(text="Get recipe", command=recipes, bg='#0052cc', fg='#ffffff')
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)





if __name__ == "__main__":
    window.mainloop()




 
