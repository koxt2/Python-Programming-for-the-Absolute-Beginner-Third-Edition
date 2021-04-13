# Python Programming for the Absolute Beginner, Third Edition
# Chapter 5, Challenge 34

# Create a Who's your daddy? program that lets the user enter the name of a male and produce the name of his father and grandfather.
# Allow the user to add, replace and delete son-father-grandfather pairs.

# son/father list
tree = {"Richard":["Robert","John"], "Joshua":["Billy","William"], "Gavin":["Colin","Grover"], "Harrison":["Richard","Robert"], "Jonathan":["John","Andrew"], "Michael":["Wieslav","Josep"]}
choice = ""
paternal = None
grandfather = None
father = None
def application ():
    global choice
    print("""Father/Son dictionary
        
        0 Quit
        1 Look up a son to find the father and grandfather
        2 Add a father/Son
        3 Remove a father/son
        4 Replace a father/son
        """)
    choice = input("Select an option: ")

    if choice == "1":
        son = input("\nWhat is the name of the son? ").capitalize()
        if son in tree:
            paternal = tree[son]
            father = paternal[0]
            grandfather = paternal[1]
            print(son + "'s father is", father)
            print("The name of", son + "'s grandfather, ie", father, "'s father, is", grandfather)
        else:
            print(son, "is not on the list... the father is unknown")
    elif choice == "2":
        son = input("What is the name of the son? ").capitalize()
        if son not in tree:
            father = input("What is the name of the father? ").capitalize()
            tree[son] = father
            grandfather = input("What is the name of the grandfather? ").capitalize()
            print("\n", son, ",", father, "and", grandfather, "have been added to the list")
        else:
            print(son, "already belongs on the list")
    elif choice == "3":
        son = input("What is the name of the son of the son/father/grandfather group that you would like to remove from the list? ").capitalize()
        if son in tree:
            del tree[son]
            print(son, ",his father and grandfather have been removed from the list")
        else:
            print(son, "is not on the list so they cannot be removed")
    elif choice == "4":
        son = input("What is the name of the son of the pair you would like to ammend? ").capitalize()
        if son in tree:
            father = input("What is the new name of the father? ").capitalize()
            grandfather = input("What is the new name of the grandfather? ").capitalize()
            tree[son][0] = father
            tree[son][1] = grandfather
            print("The names of", son + "'s father and grandfather have been updated")
        else:
            print(son, "is not on the list... the father is unknown")
while choice != "0":
    application()
else:
    print("Good-bye")


        

    
