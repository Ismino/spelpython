class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.connections = {}
        self.items = []

    def connect_room(self,room, direction):
        """Kopplar samman detta rum med ett annat rum i en viss riktning"""
        self.connections[direction] = room 

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.item.remove(item)

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
        print("Föremål i rummet:", ",".join(self.current_room.items) if self.current_room.items else "Inga")
            