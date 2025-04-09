import random

# Asking the user for their gender.
def gender_input():
    print("What's your gender? Options: male, female")
    gender = input("Gender: ").strip().lower()
    return gender

# Asking the user for input based on weather
def weather_input():
    print("What's the weather like? Options: sunny, rainy")
    weather = input("Weather: ").strip().lower()
    return weather

# Asking the user for input based on temperature
def weather_input():
    print("What's the temperature like? Options: cold, hot")
    temperature = input("Temperature: ").strip().lower()
    return temperature
  
# Asking the user for the type of outing.
def outing_input():
    print("Where are you going? Options: casual, formal, workout, party")
    outing = input("Outing: ").strip().lower()
    return outing
# Asking the user for their preference of either Long sleeve, Short sleeve, Tank top, or Sweater.
def top_preferences():
    print("Do you prefer brighter or darker colors? Options: long sleeve, short sleeve, tank top, sweater")
    top_preference = input("Top preference: ").strip().lower()
    return top_preference
  
# Asking the user for their preference of either lighter or darker clothing.
def color_preferences():
    print("Do you prefer brighter or darker colors? Options: light, dark")
    color_preference = input("Color preference: ").strip().lower()
    return color_preference

# Generates an outfit suggestion based on gender, weather, type of outing, and color preference
def suggest_outfit(gender, weather, outing, color_preference):
    outfits = {
        "male": {
            "sunny and hot": {
                "casual": [("T-shirt and jean shorts", ["white", "beige", "light blue", "black", "grey"]),
                           ("Light polo shirt", ["sky blue", "yellow", "pink", "grey", "navy blue", "white", "black"])],
                "formal": [("button down and two piece suit", ["tan", "light green", "white" "light blue", "grey", "black"])],
                "workout": [("Tank top and running shorts", ["white", "grey", "black", "blue"])],
                "party": [("open short sleeve button down and matching shorts", ["bright green", "orange", "light blue", "black", "white"]),
                          ("T-shirt", ["light orange", "light green", "white", "black"])]
            },
              "sunny and cold": {
                "casual": [("T-shirt and jean shorts", ["white", "beige", "light blue", "black", "grey"]),
                           ("Light polo shirt", ["sky blue", "yellow", "pink", "grey", "navy blue", "white", "black"])],
                "formal": [("button down and two piece suit", ["tan", "light green", "white" "light blue", "grey", "black"])],
                "workout": [("Tank top and running shorts", ["white", "grey", "black", "blue"])],
                "party": [("open short sleeve button down and matching shorts", ["bright green", "orange", "light blue", "black", "white"]),
                          ("T-shirt", ["light orange", "light green", "white", "black"])]
            },
            "rainy and hot": {
                "casual": [("Raincoat and jeans", ["navy", "dark gray"]),
                           ("Waterproof jacket", ["black", "olive"])],
                "formal": [("Trench coat and formal pants", ["black", "gray"])],
                "workout": [("Water-resistant hoodie and joggers", ["dark blue", "black"])],
                "party": [("Dark blazer with waterproof pants", ["black", "dark brown"])]
            }
              "rainy and cold": {
                "casual": [("Raincoat and jeans", ["navy", "dark gray"]),
                           ("Waterproof jacket", ["black", "olive"])],
                "formal": [("Trench coat and formal pants", ["black", "gray"])],
                "workout": [("Water-resistant hoodie and joggers", ["dark blue", "black"])],
                "party": [("Dark blazer with waterproof pants", ["black", "dark brown"])]
            }
        },
        "female": {
            "sunny": {
                "casual": [("Light sundress", ["pink", "yellow", "white"]),
                           ("T-shirt and shorts", ["light blue", "beige"])],
                "formal": [("Summer dress", ["floral patterns", "pink"]),
                           ("Light blouse and skirt", ["sky blue", "white"])],
                "workout": [("Tank top and running shorts", ["white", "gray"])],
                "party": [("Floral dress", ["pink", "yellow"]),
                          ("Bright-colored jumpsuit", ["red", "orange"])]
            },
            "rainy": {
                "casual": [("Waterproof jacket", ["navy", "dark green"]),
                           ("Raincoat with leggings", ["black", "olive"])],
                "formal": [("Trench coat and dress pants", ["black", "charcoal gray"])],
                "workout": [("Water-resistant hoodie and leggings", ["dark blue", "gray"])],
                "party": [("Dark dress with a raincoat", ["black", "dark brown"])]
            },
            "cold": {
                "casual": [("Sweater and jeans", ["burgundy", "navy"]),
                           ("Hoodie and leggings", ["black", "dark gray"])],
                "formal": [("Wool coat and dress", ["deep red", "black"]),
                           ("Long trench coat", ["tan", "cream colored"])],
                "workout": [("Thermal top and joggers", ["black", "charcoal"])],
                "party": [("Sweater dress with tights", ["navy", "dark red"])]
            },
            "hot": {
                "casual": [("Sleeveless dress", ["white", "light blue"]),
                           ("Tank top and shorts", ["yellow", "beige"])],
                "formal": [("Light blouse and skirt", ["cream", "yellow"]),
                           ("Linen dress", ["pink", "white"])],
                "workout": [("Breathable tank top and shorts", ["white", "gray"])],
                "party": [("Short sundress", ["red", "floral patterns"])]
     
            }
        }
    }

    default_light_colors = ["red", "yellow", "sky blue", "green", "pink", "white"]
    default_dark_colors = ["black", "navy", "charcoal gray", "maroon", "dark green", "brown"]

    if gender in outfits and weather in outfits[gender] and outing in outfits[gender][weather]:
        outfit_choices = outfits[gender][weather][outing]
        outfit, colors = random.choice(outfit_choices)
        
        if color_preference == "dark":
            colors = [color for color in colors if color in default_dark_colors]
            if not colors:
                colors = random.sample(default_dark_colors, 2)
        elif color_preference == "bright":
            colors = [color for color in colors if color in default_bright_colors]
            if not colors:
                colors = random.sample(default_bright_colors, 2)
        
        return f"{outfit} in colors: {', '.join(colors)}"
    else:
        return "Sorry, I don't have an outfit suggestion for the given combination at this time."

# main function to run the clothing generator
def main():
    print("Welcome to the Clothing Generator!")
    gender = gender_input()
    weather = weather_input()
    outing = outing_input()
    color_preference = color_preferences()

    outfit = suggest_outfit(gender, weather, outing, color_preference)
    print(f"\nBased on your inputs, you should wear: {outfit}")

if __name__ == "__main__":
    main()
