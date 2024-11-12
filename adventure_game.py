class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def connect_room(self, room, direction):
        """Kopplar samman detta rum med ett annat rum i en viss riktning."""
        self.connections[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.name}: {self.description}"

class Game:
    def __init__(self):
        self.rooms = {}
        self.player_inventory = []
        self.current_room = None

    def add_room(self, room):
        self.rooms[room.name] = room

    def start(self, start_room):
        self.current_room = start_room
        print("Välkommen till äventyrsspelet!")
        self.describe_current_room()

    def describe_current_room(self):
        print("\nDu är i:", self.current_room)
        print("Föremål i rummet:", ", ".join(self.current_room.items) if self.current_room.items else "Inga")
        print("Vägar:", ", ".join(self.current_room.connections.keys()))

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            self.describe_current_room()
        else:
            print("Du kan inte gå i den riktningen.")

    def take_item(self, item):
        if item in self.current_room.items:
            self.player_inventory.append(item)
            self.current_room.remove_item(item)
            print(f"Du plockade upp: {item}")
        else:
            print("Det föremålet finns inte här.")

    def check_inventory(self):
        print("Din inventering:", ", ".join(self.player_inventory) if self.player_inventory else "Tom")

    def play(self):
        while True:
            command = input("\nVad vill du göra? (gå [riktning], plocka [föremål], inventering, avsluta): ").split()
            if not command:
                print("Ogiltigt kommando.")
                continue

            action = command[0]

            if action == "gå" and len(command) > 1:
                self.move(command[1])
            elif action == "plocka" and len(command) > 1:
                self.take_item(command[1])
            elif action == "inventering":
                self.check_inventory()
            elif action == "avsluta":
                print("Spelet avslutas. Tack för att du spelade!")
                break
            else:
                print("Ogiltigt kommando.")

# Skapa rummen och spelet
hall = Room("Hall", "En stor hall med gamla målningar.")
kök = Room("Kök", "Ett kök med ett bord fyllt av gammal mat.")
bibliotek = Room("Bibliotek", "Ett tyst bibliotek med dammiga böcker.")
skattkammare = Room("Skattkammare", "En glittrande skattkammare full av guld!")

# Koppla samman rummen
hall.connect_room(kök, "öster")
kök.connect_room(hall, "väster")
kök.connect_room(bibliotek, "norr")
bibliotek.connect_room(kök, "söder")
bibliotek.connect_room(skattkammare, "öster")
skattkammare.connect_room(bibliotek, "väster")

# Lägg till föremål
kök.add_item("nyckel")
bibliotek.add_item("bok")
skattkammare.add_item("guldmynt")

# Skapa och starta spelet
game = Game()
game.add_room(hall)
game.add_room(kök)
game.add_room(bibliotek)
game.add_room(skattkammare)
game.start(hall)
game.play()
