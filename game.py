import random
import time
import json
import os

SAVE_FILE = "save_data.json"

def load_game():
    """Loads player data from a JSON file, or returns default stats if no save exists."""
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                print("💾 Loading saved profile...")
                time.sleep(1)
                return json.load(f)
        except:
            print("⚠️ Save file corrupted! Starting fresh.")
    
    # Default starter stats
    return {"hp": 100, "gold": 0, "potions": 2}

def save_game(hp, gold, potions):
    """Saves current player data to a JSON file."""
    data = {"hp": hp, "gold": gold, "potions": potions}
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("💾 Progress auto-saved successfully!")

def play_game():
    # Load previous progress or start fresh
    stats = load_game()
    player_hp = stats["hp"]
    gold = stats["gold"]
    potions = stats["potions"]
    
    # If the player died last time, revive them for the new run
    if player_hp <= 0:
        print("🩹 Reviving you with 50 HP for a fresh run!")
        player_hp = 50

    monsters = ["Shadow Snake", "Corrupted Goblin", "Orc Rogue"]
    
    print("\n⚔️ WELCOME BACK TO THE DUNGEON v2.5 ⚔️")
    print("------------------------------------------")

    while player_hp > 0:
        print(f"\n❤️ HP: {player_hp} | 🧪 Potions: {potions} | 💰 Gold: {gold}")
        action = input("Type 'f' to explore, 'h' to drink potion, or 'q' to quit: ").lower()
        
        if action == 'q':
            print(f"\nYou decided to head back to safety!")
            save_game(player_hp, gold, potions) # Save on manual quit
            break
            
        elif action == 'h':
            if potions > 0:
                potions -= 1
                player_hp = min(100, player_hp + 40)
                print("🧪 Drank a potion! +40 HP.")
            else:
                print("❌ Out of potions!")
                
        elif action == 'f':
            event = random.choice(["monster", "treasure", "potion_find"])
            
            if event == "potion_find":
                potions += 1
                print("🧪 You found a potion! +1 Potion.")
                
            elif event == "treasure":
                found_gold = random.randint(15, 60)
                gold += found_gold
                print(f"✨ Found a chest! +{found_gold} Gold.")
                
            elif event == "monster":
                monster = random.choice(monsters)
                print(f"⚠️ A wild {monster} lunges out!")
                
                while player_hp > 0:
                    battle_choice = input("Type 'a' to attack or 'r' to run: ").lower()
                    if battle_choice == 'a':
                        is_crit = random.random() < 0.2
                        player_damage = random.randint(15, 30)
                        if is_crit:
                            player_damage *= 2
                            print("🔥 CRITICAL HIT! 🔥")
                            
                        monster_damage = random.randint(8, 20)
                        print(f"💥 You deal {player_damage} damage!")
                        player_hp -= monster_damage
                        print(f"🩸 You took {monster_damage} damage!")
                        
                        if random.random() > 0.4:
                            print(f"💀 You destroyed the {monster}!")
                            gold += 25
                            save_game(player_hp, gold, potions) # Save after winning a fight
                            break
                    elif battle_choice == 'r':
                        print("🏃 You ran away safely!")
                        save_game(player_hp, gold, potions) # Save escape state
                        break
                        
    if player_hp <= 0:
        print("\n💀 YOU DIED! Your gold was lost in the dirt.")
        save_game(0, 0, potions) # Save death state (resets gold/hp, keeps potions)

if __name__ == "__main__":
    play_game()
