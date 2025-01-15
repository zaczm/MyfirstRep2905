#This function takes a lsit of ingredients and simulates
#making a sandwich
def buil_sandwich(ingredients):
    #Check if the ingredient lsit is empty
    if not ingredients:
        print("You need to choose some ingredients!")
        return
        
    print("Lets's make a sandwich!")
    print("First, we grab some bread ...")

    # Loop through each ingredient and add it to the sandwich
    for i, ingredient in enumerate(ingredients, 1):
        print(f"Adding {ingredient }...")

        print("And top it with bread!")

        #Join all ingredients for a nice final message
        print(f"\nCongrats! You made a {' and '.join(ingredients)} sandwich!")

    # Main function that handles use inputs and error catching 
    def main():
        try:
            print("Welcome to the sandwich maker!")

            # Get ingredients from user as a commoa-separated string
            ingredients_input =input("Enter ingredients (separated by commas): ")

            #Convert the input string to a list
            #1. Split string at commas
            #2. Remove extra whitespace from each ingredient
            ingredients = [i.strip() for i in ingredients_input.split(",")]

            #Call the sandwich building function with our list of ingredients
            buil_sandwich(ingredients)

        # Catch any errors the happen during execution
        except Exception as e:
            print("Oops, something went wrong!@ Let's try again.");

    # Standard Python ideion to only run the main function
    if __name__ == "__main__":
        main()
        