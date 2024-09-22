import json
import subprocess
import random
import sqlite3

class BackroomsGame:
    def __init__(self):
        self.current_room = "entrance"
        self.inventory = ["flashlight"]
        self.health = 100
        self.sanity = 100
        self.map = {"entrance": True}

    def start(self):
        print("Benvenuto nelle Backrooms...")
        while True:
            self.display_room()
            self.update_map()
            self.check_random_event()
            self.check_monster()
            action = input("Cosa vuoi fare? ").lower()
            self.process_action(action)
            self.check_game_over()

    def display_room(self):
        room_description = subprocess.check_output(["./room_description", self.current_room]).decode()
        print(room_description)
        print(f"Salute: {self.health} | Sanità mentale: {self.sanity}")

    def update_map(self):
        self.map[self.current_room] = True
        print("Mappa attuale:")
        subprocess.call(["node", "map_display.js", json.dumps(self.map)])

    def check_random_event(self):
        event = subprocess.check_output(["node", "random_events.js"]).decode().strip()
        print(event)
        if "pericolo" in event.lower():
            self.health -= 10
            print("Hai perso 10 punti salute!")
        elif "inquietante" in event.lower():
            self.sanity -= 5
            print("Hai perso 5 punti sanità mentale!")

    def check_monster(self):
        monster = subprocess.check_output(["./monster_encounter", self.current_room]).decode().strip()
        if monster != "none":
            print(f"Un {monster} appare!")
            action = input("Vuoi combattere (c) o fuggire (f)? ").lower()
            if action == 'c':
                damage = random.randint(10, 30)
                self.health -= damage
                print(f"Hai sconfitto il {monster}, ma hai perso {damage} punti salute!")
            else:
                self.move(random=True)
                self.sanity -= 15
                print("Sei fuggito, ma hai perso 15 punti sanità mentale!")

    def process_action(self, action):
        if action == "inventario":
            self.show_inventory()
        elif action == "muovi":
            self.move()
        elif action == "usa":
            self.use_item()
        elif action == "raccogli":
            self.collect_item()
        elif action == "salva":
            self.save_game()
        elif action == "carica":
            self.load_game()
        elif action == "risolvi puzzle":
            self.solve_puzzle()
        elif action == "esci":
            print("Grazie per aver giocato!")
            exit()
        else:
            print("Azione non riconosciuta.")

    def show_inventory(self):
        subprocess.call(["perl", "inventory.pl"] + self.inventory)

    def move(self, random=False):
        if random:
            new_room = subprocess.check_output(["./move", self.current_room, "random"]).decode().strip()
        else:
            new_room = subprocess.check_output(["./move", self.current_room]).decode().strip()
        self.current_room = new_room

    def use_item(self):
        item = input("Quale oggetto vuoi usare? ").lower()
        if item in self.inventory:
            effect = subprocess.check_output(["ruby", "use_item.rb", item]).decode().strip()
            print(effect)
            if "salute" in effect:
                self.health += 20
            elif "sanità" in effect:
                self.sanity += 20
            self.inventory.remove(item)
        else:
            print("Non hai questo oggetto nell'inventario.")

    def collect_item(self):
        item = subprocess.check_output(["go", "run", "items.go", self.current_room]).decode().strip()
        if item != "none":
            self.inventory.append(item)
            print(f"Hai raccolto: {item}")
        else:
            print("Non ci sono oggetti da raccogliere in questa stanza.")

    def save_game(self):
        conn = sqlite3.connect('game_progress.db')
        c = conn.cursor()
        c.execute('''INSERT INTO player_progress 
                     (current_room, inventory, health, sanity, map) 
                     VALUES (?, ?, ?, ?, ?)''', 
                  (self.current_room, json.dumps(self.inventory), 
                   self.health, self.sanity, json.dumps(self.map)))
        conn.commit()
        conn.close()
        print("Gioco salvato!")

    def load_game(self):
        conn = sqlite3.connect('game_progress.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM player_progress 
                     ORDER BY timestamp DESC LIMIT 1''')
        data = c.fetchone()
        if data:
            self.current_room = data[1]
            self.inventory = json.loads(data[2])
            self.health = data[3]
            self.sanity = data[4]
            self.map = json.loads(data[5])
            print("Gioco caricato!")
        else:
            print("Nessun salvataggio trovato.")
        conn.close()

    def solve_puzzle(self):
        puzzle = subprocess.check_output(["runhaskell", "puzzle.hs", "get"]).decode().strip()
        print(f"Puzzle: {puzzle}")
        answer = input("La tua risposta: ")
        result = subprocess.check_output(["runhaskell", "puzzle.hs", "check", answer]).decode().strip()
        print(result)
        if "Corretto" in result:
            self.sanity += 10
            print("Hai guadagnato 10 punti sanità mentale!")

    def check_game_over(self):
        if self.health <= 0:
            print("Hai perso tutta la salute. Game Over!")
            exit()
        elif self.sanity <= 0:
            print("Hai perso tutta la sanità mentale. Game Over!")
            exit()

if __name__ == "__main__":
    game = BackroomsGame()
    game.start()
