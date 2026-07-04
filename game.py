import random
import time

def play_game():
    player_hp = 100
    gold = 0
    monsters = ["Shadow Snake", "Corrupted Goblin", "Orc Rogue"]
    
    print("⚔️ WELCOME TO THE TERMINAL DUNGEON ⚔️")
    print("------------------------------------")
    time.sleep(1)

    while player_hp > 0:
        print(f"\n❤️ HP: {player_hp} | 💰 Gold: {gold}")
        action = input("Type 'f' to explore forward, or 'q' to quit the dungeon: ").lower()
        
        if action == 'q':
            print(f"\nYou fled the dungeon with {gold} gold! Cowardly, but wise.")
            break
        elif action == 'f':
            event = random.choice(["monster", "treasure", "empty"])
            
            if event == "empty":
                print("...Just a dusty, empty corridor. You keep moving.")
                
            elif event == "treasure":
                found_gold = random.randint(10, 50)
                gold += found_gold
                print(f"✨ You found a hidden chest! Added +{found_gold} Gold.")
                
            elif event == "monster":
                monster = random.choice(monsters)
                print(f"⚠️ A wild {monster} jumps out of the shadows!")
                
                # Simple battle loop
                while player_hp > 0:
                    battle_choice = input("Type 'a' to attack or 'r' to run away: ").lower()
                    if battle_choice == 'a':
                        player_damage = random.randint(15, 35)
                        monster_damage = random.randint(10, 25)
                        
                        print(f"💥 You slash the {monster} for {player_damage} damage!")
                        player_hp -= monster_damage
                        print(f"🩸 The {monster} hits you back for {monster_damage} damage!")
                        
                        if random.random() > 0.4: # 60% chance to defeat monster per turn
                            print(f"💀 You defeated the {monster}!")
                            gold += 20
                            break
                    elif battle_choice == 'r':
                        print("🏃 You scrambled backward into the last room safely!")
                        break
        else:
            print("Invalid command! Focus, adventurer.")
            
    if player_hp <= 0:
        print("\n💀 YOU DIED! The dungeon claims another soul.")
        print(f"Final Score - Gold Collected: {gold}")

if __name__ == "__main__":
    play_game()

