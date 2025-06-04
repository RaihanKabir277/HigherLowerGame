import random
import game_data

# print(game_data.data[0]["name"])

print("\n welcome to the higher and lower game \n")

length = len(game_data.data)

def game_play():
    count = 0

    while True:

       
        item = random.randint(0, length - 1)
        print(f"\n Compare A : {game_data.data[item]["name"]}, {game_data.data[item]["description"]}, From {game_data.data[item]["country"]}")

        print("\n\n VS \n\n")

        item1 = random.randint(0, length - 1)

        print(f" Compare B : {game_data.data[item1]["name"]}, {game_data.data[item1]["description"]}, From {game_data.data[item1]["country"]}")

        follower_A = (game_data.data[item]["follower_count"])
        follower_B = (game_data.data[item1]["follower_count"])


        compare = input("Who has more followers on instragram? type 'A' or 'B' : " ).lower()
        
        if compare == "a" and follower_A > follower_B :
            print("\n" * 20)
            count += 1
            print(f"you are right, Your current score is = {count}")

        elif compare == "b" and follower_B > follower_A :
            print("\n" * 20)
            count += 1
            print(f"you are right, Your current score is = {count}")

        elif compare == "a" and follower_A < follower_B :
            print("\n" * 20)
            print(f"you are wrong, Your final score is = {count}")
            break

        elif compare == "b" and follower_B < follower_A :
            print("\n" * 20)
            print(f"you are wrong, Your final score is = {count}")
            break


        

game_play()
        

    
