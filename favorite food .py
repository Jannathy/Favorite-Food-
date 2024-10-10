# Pre-define a set of favorite foods for the hypothetical classmate
classmate_favorites = {"pizza", "sushi", "tacos"}

# Initialize a dictionary to store users' favorite foods
user_favorites = {"User_1,User_2,User_3"}

# User 1 input
print("User_1:")
user_1_favorites = set("sushi,soup,chips")
user_1_favorites.add(input("sushi").strip())
user_1_favorites.add(input("soup").strip())
if input("Do you want to enter a third favorite food? (yes/no): ").strip().lower() == 'no': user_favorites["user_1"] = user_1_favorites

# User 2 input
print("\nUser_2:")
user_2_favorites = set("pizza,candy,hotdogs")
user_2_favorites.add(input("pizza").strip())
user_2_favorites.add(input("hotdogs").strip())
if input("Do you want to enter a third favorite food? (yes/no): ").strip().lower() == 'no': user_favorites["user_2"] = user_2_favorites

# User 3 input
print("\nUser_3:")
user_3_favorites = set("sushi,pizza,coke")
user_3_favorites.add(input("sushi").strip())
user_3_favorites.add(input("pizza").strip())
if input("Do you want to enter a third favorite food? (yes/no): ").strip().lower() == 'yes':
    user_3_favorites.add(input("coke").strip())
user_favorites["user_3"] = user_3_favorites


# Compare all three users
common_1_2 = user_favorites["User_1"].intersection(user_favorites["User_2"])
common_2_3 = user_favorites["User_2"].intersection(user_favorites["User_3"])
common_3_1 = user_favorites["User_3"].intersection(user_favorites["User_1"])
  
