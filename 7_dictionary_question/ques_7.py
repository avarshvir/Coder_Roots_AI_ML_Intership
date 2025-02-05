#Q7 WAP to plan for a vacation. Take input from asking for the budget.
# Suggest multiple countries to stay in that budget.
# Ask user to select a country and display a place to visit in that country.
#output
# Welcome to trip planner
# Enter your budget (5000-10000, 10000-20000, 20000-30000, 30000-40000)
# 25000
#ountry available under 30000 are:
# India
# Australia
# USA
#select your choice: India
# the place to visit in the India is the Taj Mahal

def sel_contries():
    country_sel = input("Select country: ")
    return country_sel


print("Welcome to Trip Planner")
budget_in = int(input("Enter your budget ($5000-$10000, $10000-$20000, $20000-$30000, $30000-$40000): "))
if budget_in < 10000 and budget_in >= 1000:
    print("Country available under 10000 are:")
    print("1. bhutan \n2. nepal \n3. sri lanka")
    selected_country = sel_contries()
    if selected_country == 'bhutan':
        print("The Place to visit in the Bhutan is the Thimpu")
    elif selected_country == 'nepal':
        print("The Place to visit in the Nepal is the Kathmandu")
    elif selected_country == 'sri lanka':
        print("The Place to visit in the Sri Lanka is the Colombo")
    else:
        print("Invalid Choice.")

elif budget_in >= 10000  and budget_in < 20000:
    print("Country available between 10000 - 20000 are:")
    print("1. Vietnam \n2. Thailand \n3. Malaysia")
    selected_country = sel_contries()
    if selected_country == 'vietnam':
        print("The Place to visit in the Vietnam is the Hanoi")
    elif selected_country == 'thailand':
        print("The Place to visit in the Thailand is the Bangkok")
    elif selected_country == 'malaysia':
        print("The Place to visit in the Malaysia is the George Town")
    else:
        print("Invalid Choice.")

elif budget_in >= 20000  and budget_in < 30000:
    print("Country available between 20000 - 30000 are:")
    print("1. India \n2. China \n3. Russia")
    selected_country = sel_contries()
    if selected_country == 'India' or 'india':
        print("The Place to visit in the India is the Taj Mahal")
    elif selected_country == 'China' or 'china':
        print("The Place to visit in the China is the Great Wall of China")
    elif selected_country == 'Russia' or 'russia':
        print("The Place to visit in the Russia is the Moscow")
    else:
        print("Invalid Choice.")

elif budget_in >= 30000  and budget_in <= 40000:
    print("Country available between 30000 - 40000 are:")
    print("1. South Korea \n2. Japan \n3. USA")
    selected_country = sel_contries()
    if selected_country == 'south korea':
        print("The Place to visit in the South Korea is the Samsung City")
    elif selected_country == 'Japan':
        print("The Place to visit in the Japan is the Tokyo")
    elif selected_country == 'usa' or 'USA':
        print("The Place to visit in the USA is the Statue of Liberty")
    else:
        print("Invalid Choice.")

elif budget_in <1000 or budget_in > 40000:
    print("Sorry for that but we have only budget trip between 1000 to 40000 dollars")
else:
    print("Invalid")




    
    