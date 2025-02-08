import random
import time

def print_intro():
    print("\nWelcome, brave adventurer! You stand at the entrance of the Dungeon of Shadows.")
    print("Your quest is to retrieve the Lost Amulet of Eldoria hidden deep within the maze-like depths.")
    print("Choose your actions wisely, for danger lurks around every corner!\n")

def get_choice(options):
    print("\nChoose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Enter the number of your choice: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Invalid choice. Please enter a valid number: ")
    return int(choice)

def encounter_enemy():
    enemies = ["Goblin", "Skeleton Warrior", "Dark Mage", "Ogre"]
    enemy = random.choice(enemies)
    print(f"\nA {enemy} appears!")
    print("Prepare for battle!")
    return enemy

def combat(player_hp, enemy_hp, enemy_name):
    print(f"\nYou are fighting {enemy_name}!")
    while player_hp > 0 and enemy_hp > 0:
        print(f"\nYour HP: {player_hp} | {enemy_name} HP: {enemy_hp}")
        action = get_choice(["Attack", "Defend", "Try to Run", "Use Magic", "Use Item"])
        if action == 1:  # Attack
            player_damage = random.randint(5, 15)
            enemy_hp -= player_damage
            print(f"You strike {enemy_name}, dealing {player_damage} damage!")
        elif action == 2:  # Defend
            enemy_damage = random.randint(5, 12)
            block = min(random.randint(5, 13), enemy_damage)
            print(f"You raise your shield, reducing incoming damage by {block}!")
        elif action == 3:  # Run
            if random.random() < 0.5:
                print("You successfully escape!")
                return True
            else:
                print(f"{enemy_name} blocks your escape!")
        elif action == 4:  # Use Magic
            magic_damage = random.randint(10, 20)
            enemy_hp -= magic_damage
            print(f"You cast a spell, dealing {magic_damage} damage to {enemy_name}!")
        elif action == 5:  # Use Item
            print("You search your inventory...")
            print("(Feature to use items will be implemented later)")
        
        if enemy_hp > 0:
            enemy_damage = random.randint(5, 12)
            print(f"{enemy_name} attacks and deals {enemy_damage} damage!")
            player_hp -= max(0, enemy_damage - block)
    
    if player_hp > 0:
        print(f"\nYou have defeated {enemy_name}!")
        return True
    else:
        print(f"\nYou have fallen in battle against {enemy_name}...")
        return False

def dungeon_master():
    player_hp = 50
    inventory = []
    battle_count = 0
    last_encounter = None
    print_intro()
    
    while True:
        choice = get_choice(["Enter the dungeon", "Check inventory", "Rest", "Look for a secret passage", "Leave the quest"])
        
        if choice == 1:
            print("\nYou step into the dark halls of the dungeon...")
            possible_encounters = ["enemy", "treasure", "trap", "nothing"]
            if battle_count >= 5:
                encounter = "final_boss"
            else:
                if last_encounter:
                    possible_encounters.remove(last_encounter)
                encounter = random.choice(possible_encounters)
            last_encounter = encounter
            
            if encounter == "enemy":
                enemy = encounter_enemy()
                if not combat(player_hp, random.randint(20, 40), enemy):
                    break  # Player dies
                battle_count += 1
            elif encounter == "treasure":
                treasure = random.choice(["Health Potion", "Magic Scroll", "Silver Sword", "Gold Coins"])
                print(f"You find a {treasure}!")
                inventory.append(treasure)
            elif encounter == "trap":
                trap_damage = random.randint(5, 15)
                player_hp -= trap_damage
                print(f"You trigger a trap and lose {trap_damage} HP!")
            elif encounter == "final_boss":
                print("You have reached the deepest chamber of the dungeon...")
                print("A powerful presence looms before you...")
                print("Kyle Sava, the final boss, emerges with a menacing glare!")
                if not combat(player_hp, 100, "Kyle Sava"):
                    break  # Player dies
                else:
                    print("You have defeated Kyle Sava and retrieved the Lost Amulet of Eldoria! You are victorious!")
                    break
            else:
                print("The room is eerily empty...")
        elif choice == 2:
            print("\nYour inventory:")
            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("You have no items yet.")
        elif choice == 3:
            print("You take a rest... This will take 5 seconds.")
            time.sleep(5)
            player_hp += 10
            print("You feel refreshed and regain 10 HP.")
        elif choice == 4:
            print("You search for hidden paths...")
            if random.random() < 0.3:
                print("You discover a hidden passage leading deeper into the dungeon!")
            else:
                print("You find nothing but dust and cobwebs.")
        elif choice == 5:
            print("You turn back, leaving the dungeon behind...")
            break
    
    print("\nYour adventure has come to an end!")

if __name__ == "__main__":
    dungeon_master()
