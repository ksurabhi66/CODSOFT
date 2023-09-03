import random

options = ("rock", "paper", "scissors")

def play_round():
    computer = random.choice(options)
    player = None
    
    while True:
        player = input("Enter your choice (rock, paper, scissors): ")
        if player in options:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    
    
    print(f"player:={player}")

    print(f"computer:={computer}")


    if player == computer:
        return "It's a tie!", 0
    elif player == "rock" and computer == "scissors":
        return "You win!", 1
    elif player == "paper" and computer == "rock":
        return "You win!", 1
    elif player == "scissors" and computer == "paper":
        return "You win!", 1
    else:
        return "You lost!", -1

def main():
    player_score = 0
    computer_score = 0  
    
    rounds = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Enter your choice (rock, paper, scissors)")
    
    while True:
        print(f"\nRound {rounds + 1}")
        result_message, result = play_round()
        
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1
            
        rounds += 1
        
        print(result_message)
        print(f"Player's score: {player_score}")
        print(f"Computer's score: {computer_score}\n")
        
        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again != "yes":
            print(f"Thanks for playing!\nFinal score - Player: {player_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()