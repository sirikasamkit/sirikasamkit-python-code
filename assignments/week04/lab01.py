"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("sirikasamkit", 19, "Chonburi", "Thai")  # name, age, city, country
    hobbies = []
    while True:
        print("1:display")
        print("2:add hobby")
        print("3:remove hobby")
        print("4:edit age")
        print("5:exit")
        choie = input("What do you want to do?(1 - 5)")
        # Your code here
        if choie == "1":
            print("Name: ",person[0])
            print(f"Age: {person[1]}")
            print("City: ",person[2])
            print("Country: "+ person[3])
            print("Hobbies: ",hobbies)

        elif choie == "2":
            hobby = input("What is your new hobby?: ")
            hobbies.append(hobby)

        elif choie == "3":
            hobbies.pop()

        elif choie == "4":
            person_list = list(person)
            age = input("How old are you?: ")
            person_list[1] = age

        elif choie == "5":
            break

        else :
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    personal_info_manager()