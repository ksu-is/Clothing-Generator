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
def temperature_input():
    print("What's the weather like? Options: cold, hot")
    temperature = input("Temperature: ").strip().lower()
    return temperature

# Asking the user for the type of outing.
def outing_input():
    print("Where are you going? Options: casual, formal, workout, party, church")
    outing = input("Outing: ").strip().lower()
    return outing

# Asking the user for their preference of either lighter or darker clothing.
def color_preferences():
    print("Do you prefer brighter or darker colors? Options: light, dark")
    color_preference = input("Color preference: ").strip().lower()
    return color_preference

# Asking the user for their preference of tops.
def tops_preferences():
    print("what is your preferrence in tops? Options: short sleeve, long sleeve, tank top, sweater, crop top")
    tops_preferences = input("Tops preference: ").strip().lower()
    return tops_preferences

# Asking the user for their preference of bottoms.
def bottoms_preferences():
    print("what is your preferrence in bottoms? Options: jean, jean shorts, athletic shorts, athletic pants, skirt")
    bottoms_preferences = input("Bottoms preference: ").strip().lower()
    return bottoms_preferences

# Asking the user for their preference of jackets.
def bottoms_preferences():
    print("what is your preferrence in jackets? Options: jean jacket, puffer jacket, sweater cardigan, cardigan, trench coat, blazer")
    jackets_preferences = input("Jackets preference: ").strip().lower()
    return jackets_preferences

# Asking the user for their preference of shoes.
def shoes_preferences():
    print("what is your preferrence in shoes? Options: sneakers, dress shoes, boots, flats, heels, sandals")
    shoes_preferences = input("Shoes preference: ").strip().lower()
    return shoes_preferences

# Generates an outfit suggestion based on gender, weather, type of outing, and color preference
def suggest_outfit(gender, weather, outing, color_preference):
    outfits = {
        "male": {
            "sunny and hot ": {
                "casual": [("T-shirt and shorts with sneakers", ["white", "beige", "light blue"]),
                           ("Light polo shirt and jean shorts with sandals", ["sky blue", "blue"])],
                "formal": [("Light suit with dress shoes", ["cream colored", "light pink"]),
                           ("Summer blazer with dress pant and loafers", ["tan", "brown"])],
                "workout": [("Tank top and running shorts with sneakers", ["white", "gray"])],
                            ("Lightweight shirt and shorts with sneakers", ["navy blue", "yellow"]),
                "party": [("Floral shirt and Khaki Pants sandals", ["khaki", "orange"]),
                          ("Bright-colored T-shirt and jean shorts with sneakers", ["red", "yellow", "green", "black", "white"])]
                "church": [("Light button-up short sleeve shirt and dress pants with dress loafers", ["white", "Light blue"])],
                            [("Light blazer with dress pants and dress shoes", ["cream colored", "Light gray"])]
            },           
            "sunny and cold ": {
                "casual": [("Long sleeve shirt and jeans with sneakers", ["black", "red", "grey"]),
                           ("sweater shirt and jeans with boots and leather jacket", ["grey", "blue", "white"])],
                "formal": [("suit with dress shoes and trench coat", ["tan", "cream color", "white"]),
                           ("blazer with dress pant and loafers", ["tan", "brown"])],
                "workout": [("long sleevee athletic shirt and joggers with sneakers", ["blue", "gray"])],
                            ("Lightweight hoodie and sweat pants with sneakers", ["black", "white"]),
                "party": [(" long sleeve with a button- down cardigan and jeans with boots", ["blue", "orange", "light green", "white"]),
                          ("Bright-colored zip up leather jacket with a sweater and dark plants with sneakers", ["orange", "white", "cream", "black", "white"])]
                "church": [("Dark button-up Long sleeve shirt and dress pants with dress loafers", ["white", "Light blue"])],
                            [("Light blazer with dress pants and dress shoes", ["tan", "Light brown", "brown"])]
            },
            "rainy and hot": {
                "casual": [("Raincoat and jeans with rain boots", ["navy", "dark gray"]),
                           ("Waterproof jacket and jeans with sneakers", ["black", "olive"])],
                "formal": [("blazer and formal pants with dress shoes and poncho", ["black", "gray"])],
                "workout": [("Water-resistant hoodie and joggers with sneakers", ["dark blue", "black"])],
                "party": [("Dark button down leather short sleeve jacket and dark jeans with sneakers", ["black", "dark orange"])]
                "church": [("Light blazer with jeans and loafers", ["light blue", "white"])]
            },
            "rainy and cold": {
                "casual": [("Sweater and jeans and rain jacket with boots", ["dark green", "orange"]),
                           ("Hoodie and joggers and sneakers", ["burgundy", "gray"])],
                "formal": [("Wool suit with dress boots", ["dark gray", "black"]),
                           ("Long coat and scarf with dress pants and sneakers", ["tan", "burgundy"])],
                "workout": [("Thermal gear and sweatpants with sneakers", ["black", "charcoal gray"])],
                "party": [("Water-resistant long sleeve shirt and jeans with sneakers", ["navy", "brown"])],
                "church": [("Long trench rain jacket and button-up with dress pants with dress shoes", ["white", "grey", "black"])]
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

    default_bright_colors = ["red", "yellow", "sky blue", "green", "pink", "white"]
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

# main function to run the outfit generator
def main():
    print("Welcome to the Outfit Generator!")
    gender = gender_input()
    weather = weather_input()
    outing = outing_input()
    color_preference = color_preferences()

    outfit = suggest_outfit(gender, weather, outing, color_preference)
    print(f"\nBased on your inputs, you should wear: {outfit}")

if __name__ == "__main__":
    main()