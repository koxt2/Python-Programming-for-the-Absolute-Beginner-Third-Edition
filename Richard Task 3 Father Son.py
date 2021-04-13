# Python Programming for the Absolute Beginner, Third Edition
# Chapter 5, Challenge 3

# Create a Who's your daddy? program that lets the user enter the name of a male and produce the name of his father.
# Allow the user to add, replace and delete son-father pairs.

# Option 4 needs to be finished. 

# son/father list
tree = {"Richard":"Robert", "Gavin":"Colin", "Harrison":"Richard", "Jonathan":"John", "Josepth":"Wieslaw"}
choice = ""

#print("""Father/Son dictionary
 #     
  #    0 Quit
   #   1 Look up a son to find the father
    #  2 Add a father/Son
     # 3 Remove a father/son
      #4 Replace a father/son
      #""")

#while not choice:
#    choice = input("Select an option: ")
def application():
    global choice
    print("""Father/Son dictionary
    
    0 Quit
    1 Look up a son to find the father
    2 Add a father/Son
    3 Remove a father/son
    4 Replace a father/son
    """)
    choice = input("Select an option: ")

    if choice == "1":
        son = input("What is the name of the son? ").capitalize()
        if son in tree:
            father = tree[son]
            print("The father of", son, "is", father)
        else:
            print(son, "is not on the list... the father is unknown")
    elif choice == "2":
        son = input("What is the name of the son? ").capitalize()
        if son not in tree:
            father = input("What is the name of the father? ").capitalize()
            tree[son] = father
            print("\n", son, "and", father, "have been added to the list")
        else:
            print(son, "already belongs on the list")
    elif choice == "3":
        son = input("What is the name of the son of the pair that you would like to remove from the list? ").capitalize()
        if son in tree:
            del tree[son]
            print(son, "and his father have been remove from the list")
        else:
            print(son, "is not on the list so they cannot be removed")
    elif choice == "4":
        son = input("What is the name of the son of the pair you would like to ammend? ").capitalize()      
        if son in tree:
            father = input("What is the new name of the father? ").capitalize()
            son = input("What is the new name of the son?").capitalize
            tree[son] = father
            #tree[son] = son
            print("The name of", son, "father has been updated")
        else:
            print(son, "is not on the list... the father is unknown")
while choice != "0":
    application()
else:
    print("Good-bye")


        

    
