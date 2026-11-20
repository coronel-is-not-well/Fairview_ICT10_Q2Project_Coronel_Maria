from pyscript import document, display

Members = ["Sabine Shark", "Dylan Dove", "Tanya Tiger", "Ramone Ram", "Kirsten Kangaroo", "Atrisha Alpaca", "Lance Lion", "Sean Seal", "Diego Dog", "Maria Mouse", "Edrian Elephant", "Eliana Eagle", "Raven Raven", "Annika Ant", "Amanda Axolotl", "Sunny Sheep", "Rodolfo Rat", "Maiselle Macaw", "Matt Monkey", "Andre Armadillo", "Anissa Albatross", "Frances Fox", "Ynigo Yak", "Zack Zebra", "Rohan Rabbit", "Jhoana Jaguar"] # names of 10 Ruby <3

def Submit1(e):

    NameF = document.getElementById("FName").value # getting the value of the input of the first name

    NameL = document.getElementById("LName").value # getting the value of the input of the first name

    members_new = NameF.capitalize() + " " + NameL.capitalize() # combining them and making them capitalized with a space

    Message = f"Congratulations {members_new}! You are part of the Maria Mouse Clubhouse." if members_new in Members else f"Sorry {members_new}, your name is not on the list." # checking if the members new is in the list of members

    display(Message, target="CMC") # making it seen

Grade7 = {"Raven Denum", "Sabine Agacita"}

Grade8 = {"Frances Sevilla", "Kirsten Caagbay"}

Grade9 = {"Rodolfo Lao", "Lance Catu"}

Grade10 = {"Maria Coronel"} # listing members

GradesAll = Grade7 | Grade8 | Grade9 | Grade10 # putting them together

def Submit(e):

    NewName = document.getElementById("firstname").value.capitalize() + " " + document.getElementById("lastname").value.capitalize() # getting the input value

    Final = GradesAll | {NewName} # all together

    display(Final, target="output1")

    display(len(Final), target="output2")

NonMetals = {"H":("Hydrogen", 1, 1.008), 
             "He":("Helium", 2, 4.0026),
             "C":("Carbon", 6, 12.011),
             "N":("Nitrogen", 7, 14.007),
             "O":("Oxygen", 8, 15.999),
             "F":("Flourine", 9, 18.998),
             "N":("Neon", 10, 20.18),
             "P":("Phosphorus", 15, 30.974),
             "S":("Sulfur", 16, 32.07),
             "Cl":("Chlorine", 17, 35.45),
             "Ar":("Argon", 18, 39.9),
             "Se":("Selenium", 34, 78.97),
             "Br":("Bromine", 35, 79.9),
             "Kr":("Krypton", 36, 83.8),
             "I":("Iodine", 53, 126.9),
             "Xe":("Xenon", 54, 131.29),
             "Rn":("Radon", 86, 86),} # dictionaries of the elements (symbol : (name, atomic number, atomic mass))

def SearchSymbol(e): #function

    ElementSym = document.getElementById("ElementInput").value.capitalize() #getting the value of what the user typed in

    result = NonMetals.get(ElementSym, ('Element not found', "-", "-")) # seeing if what was inputed is in the dictionaries, and when not, element not found will show up

    document.getElementById("Symbol").innerText = ElementSym
    document.getElementById("EName").innerText = result[0]
    document.getElementById("AtomicNo").innerText = result[1]
    document.getElementById("AtomicMass").innerText = result[2] # getting the values then making it appear on the main page



