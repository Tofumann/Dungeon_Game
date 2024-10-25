import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Optional

from support import *

# Implement the classes, methods & functions described in the task sheet here

class Weapon: # 4.1.1
    def __init__(self):
        self._name = "AbstractWeapon"
        self._symbol = WEAPON_SYMBOL
        self._effect = {}
        self._range = 0

    def get_name(self) -> str:
        """Returns the name of this weapon."""
        return self._name

    def get_symbol(self) -> str:
        """Returns the symbol of this weapon."""
        return self._symbol

    def get_effect(self) -> dict[str, int]:
        """Returns a dictionary representing the weapon's effects."""
        return self._effect

    def get_targets(self, position: Position) -> list[Position]:
        x, y = position
        targets = []
        for i in range(1, self._range + 1):
            targets.extend([
                (x, y + i), (x, y - i),
                (x + i, y), (x - i, y)
            ])
        return targets

    def __str__(self) -> str:
        """Returns the name of this weapon."""
        return self.get_name()

    def __repr__(self) -> str:
        """Returns a string which could be copied and pasted into a REPL to construct a new instance identical to self."""
        return f"{self.__class__.__name__}()"

class PoisonDart(Weapon): # 4.1.2
    def __init__(self):
        super().__init__()
        self._name = "PoisonDart"
        self._symbol = POISON_DART_SYMBOL
        self._effect = {"poison": 2}
        self._range = 2

class PoisonSword(Weapon): # 4.1.3
    def __init__(self):
        super().__init__()
        self._name = "PoisonSword"
        self._symbol = POISON_SWORD_SYMBOL
        self._effect = {"damage": 2, "poison": 1}
        self._range = 1

class HealingRock(Weapon): # 4.1.4
    def __init__(self):
        super().__init__()
        self._name = "HealingRock"
        self._symbol = HEALING_ROCK_SYMBOL
        self._effect = {"healing": 2}
        self._range = 2

class Tile: # 4.1.5
    def __init__(self, symbol: str, is_blocking: bool) -> None:
        self._symbol = symbol
        self._is_blocking = is_blocking
        self._weapon = None

    def is_blocking(self) -> bool:
        return self._is_blocking

    def get_weapon(self) -> Optional[Weapon]:
        return self._weapon

    def set_weapon(self, weapon: Weapon) -> None:
        self._weapon = weapon

    def remove_weapon(self) -> None:
        self._weapon = None

    def __str__(self) -> str:
        return self._symbol

    def __repr__(self) -> str:
        return f"Tile('{self._symbol}', {self._is_blocking})"
    
def create_tile(symbol: str) -> Tile: # 4.1.6
    if symbol == WALL_TILE:
        return Tile(WALL_TILE, True)
    elif symbol == GOAL_TILE:
        return Tile(GOAL_TILE, False)
    elif symbol in (POISON_DART_SYMBOL, POISON_SWORD_SYMBOL, HEALING_ROCK_SYMBOL):
        tile = Tile(FLOOR_TILE, False)
        if symbol == POISON_DART_SYMBOL:
            tile.set_weapon(PoisonDart())
        elif symbol == POISON_SWORD_SYMBOL:
            tile.set_weapon(PoisonSword())
        elif symbol == HEALING_ROCK_SYMBOL:
            tile.set_weapon(HealingRock())
        return tile
    else:
        return Tile(FLOOR_TILE, False)

class Entity: # 4.1.7
    def __init__(self, max_health: int) -> None:
        self._max_health = max_health
        self._health = max_health
        self._poison = 0
        self._weapon = None

    def get_symbol(self) -> str:
        return ENTITY_SYMBOL

    def get_name(self) -> str:
        return "Entity"

    def get_health(self) -> int:
        return self._health

    def get_poison(self) -> int:
        return self._poison

    def get_weapon(self) -> Optional[Weapon]:
        return self._weapon

    def equip(self, weapon: Weapon) -> None:
        self._weapon = weapon

    def get_weapon_targets(self, position: Position) -> list[Position]:
        return self._weapon.get_targets(position) if self._weapon else []

    def get_weapon_effect(self) -> dict[str, int]:
        return self._weapon.get_effect() if self._weapon else {}

    def apply_effects(self, effects: dict[str, int]) -> None:
        if 'healing' in effects:
            self._health = min(self._max_health, self._health + effects['healing'])
        if 'damage' in effects:
            self._health = max(0, self._health - effects['damage'])
        if 'poison' in effects:
            self._poison += effects['poison']

    def apply_poison(self) -> None:
        """Apply poison effect and reduce poison counter."""
        if self._poison > 0:
            self._health = max(0, self._health - 1)  # Only apply 1 damage per turn
            self._poison = max(0, self._poison - 1)

    def is_alive(self) -> bool:
        return self._health > 0

    def __str__(self) -> str:
        return self.get_name()

    def __repr__(self) -> str:
        return f"Entity({self._max_health})"
    
class Player(Entity): # 4.1.8
    
    def __init__(self, max_health: int) -> None:
        super().__init__(max_health)

    def get_symbol(self) -> str:
        return PLAYER_SYMBOL

    def get_name(self) -> str:
        return "Player"

    def __repr__(self) -> str:
        return f"Player({self._max_health})"

class Slug(Entity): # 4.1.9
    def __init__(self, max_health: int) -> None:
        super().__init__(max_health)
        self._can_move = True

    def get_symbol(self) -> str:
        return SLUG_SYMBOL

    def get_name(self) -> str:
        return "Slug"

    def choose_move(self, candidates: list[Position], current_position: Position,
                    player_position: Position) -> Position:
        raise NotImplementedError("Slug subclasses must implement a choose_move method.")

    def can_move(self) -> bool:
        return self._can_move

    def end_turn(self) -> None:
        self._can_move = not self._can_move

    def __repr__(self) -> str:
        return f"Slug({self._max_health})"
    
class NiceSlug(Slug): # 4.1.10
    def __init__(self):
        super().__init__(10)  # max_health of 10
        self.equip(HealingRock())

    def get_symbol(self) -> str:
        return NICE_SLUG_SYMBOL

    def get_name(self) -> str:
        return "NiceSlug"

    def choose_move(self, candidates: list[Position], current_position: Position,
                    player_position: Position) -> Position:
        return current_position  # Stay where it is

    def __repr__(self) -> str:
        return "NiceSlug()"    
    
class AngrySlug(Slug): # 4.1.11
    def __init__(self):
        super().__init__(5)  # max_health of 5
        self.equip(PoisonSword())

    def get_symbol(self) -> str:
        return ANGRY_SLUG_SYMBOL

    def get_name(self) -> str:
        return "AngrySlug"

    def choose_move(self, candidates: list[Position], current_position: Position,
                    player_position: Position) -> Position:
        positions = candidates + [current_position]
        return min(positions, key=lambda pos: (self._distance_squared(pos, player_position), pos))

    def _distance_squared(self, pos1: Position, pos2: Position) -> int:
        return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

    def __repr__(self) -> str:
        return "AngrySlug()"
    
class ScaredSlug(Slug): # 4.1.12
    def __init__(self):
        super().__init__(3)  # max_health of 3
        self.equip(PoisonDart())

    def get_symbol(self) -> str:
        return SCARED_SLUG_SYMBOL

    def get_name(self) -> str:
        return "ScaredSlug"

    def choose_move(self, candidates: list[Position], current_position: Position,
                    player_position: Position) -> Position:
        positions = candidates + [current_position]
        return max(positions, key=lambda pos: (self._distance_squared(pos, player_position), pos))

    def _distance_squared(self, pos1: Position, pos2: Position) -> int:
        return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

    def __repr__(self) -> str:
        return "ScaredSlug()"

class SlugDungeonModel: # 4.1.13
    def __init__(self, tiles: 'list[list[Tile]]', slugs: 'dict[Position, Slug]',
                player: 'Player', player_position: Position) -> None:
        self._tiles = tiles
        self._slugs = dict(slugs)  # Make a copy of the slugs dictionary
        self._player = player
        self._player_position = player_position
        self._previous_player_position = player_position

    def get_tiles(self) -> 'list[list[Tile]]':
        return self._tiles

    def get_slugs(self) -> 'dict[Position, Slug]':
        return self._slugs

    def get_player(self) -> 'Player':
        return self._player

    def get_player_position(self) -> Position:
        return self._player_position

    def get_tile(self, position: Position) -> 'Tile':
        row, col = position
        return self._tiles[row][col]

    def get_dimensions(self) -> 'tuple[int, int]':
        return len(self._tiles), len(self._tiles[0])

    def get_valid_slug_positions(self, slug: 'Slug') -> 'list[Position]':
        if not slug.can_move():
            return []
        slug_pos = next(pos for pos, s in self._slugs.items() if s == slug)
        valid_positions = [slug_pos]
        for delta in POSITION_DELTAS:
            new_pos = (slug_pos[0] + delta[0], slug_pos[1] + delta[1])
            if self._is_valid_position(new_pos):
                valid_positions.append(new_pos)
        return valid_positions

    def _is_valid_position(self, position: Position) -> bool:
        rows, cols = self.get_dimensions()
        row, col = position
        if 0 <= row < rows and 0 <= col < cols:
            tile = self.get_tile(position)
            return not tile.is_blocking() and position not in self._slugs and position != self._player_position
        return False

    def perform_attack(self, entity: 'Entity', position: Position) -> None:
        weapon = entity.get_weapon()
        if weapon:
            targets = weapon.get_targets(position)
            effects = weapon.get_effect().copy()  # Create a copy of effects
            
            # Handle attacks on player
            if isinstance(entity, Slug) and self._player_position in targets:
                self._player.apply_effects(effects)
            
            # Handle attacks on slugs
            if isinstance(entity, Player):
                for target_pos in targets:
                    if target_pos in self._slugs:
                        self._slugs[target_pos].apply_effects(effects)


    def end_turn(self) -> None:
        """
        Process end of turn effects and slug movement.
        """
        # Apply poison to player first
        self._player.apply_poison()
        
        # Handle dead slugs and their effects
        dead_slugs = []
        for pos, slug in self._slugs.items():
            # Apply poison and check if slug dies
            slug.apply_poison()
            if not slug.is_alive():
                dead_slugs.append(pos)
                # Drop weapon when slug dies
                weapon = slug.get_weapon()
                if weapon:
                    self.get_tile(pos).set_weapon(weapon)
        
        # Remove dead slugs
        for pos in dead_slugs:
            del self._slugs[pos]
        
        # Handle slug movement - preserve order
        original_positions = list(self._slugs.items())  # Get ordered list of slug positions
        new_positions = {}
        
        # Process each slug in original order
        for old_pos, slug in original_positions:
            new_pos = old_pos  # Default to not moving
            
            if slug.can_move():
                valid_positions = [pos for pos in self.get_valid_slug_positions(slug)
                                if pos not in new_positions]
                
                if valid_positions:  # Only try to move if there are valid positions
                    # Choose move based on previous player position
                    chosen_pos = slug.choose_move(valid_positions, old_pos, self._previous_player_position)
                    if chosen_pos in valid_positions:
                        new_pos = chosen_pos
            
            # Always add to new positions, whether moved or not
            new_positions[new_pos] = slug
            
            # Update turn status
            slug.end_turn()
        
        # Update slug positions
        self._slugs = new_positions
        
        # Have all slugs attack from their positions
        for pos, slug in self._slugs.items():
            self.perform_attack(slug, pos)

    def handle_player_move(self, position_delta: Position) -> None:
        new_pos = (self._player_position[0] + position_delta[0],
                self._player_position[1] + position_delta[1])
        
        # Check if new position is within bounds
        rows, cols = self.get_dimensions()
        if not (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols):
            return

        # Handle position change
        if position_delta == (0, 0) or self._is_valid_position(new_pos):
            if position_delta != (0, 0):
                # Update previous position before moving
                self._previous_player_position = self._player_position  # Add this line
                
                # Handle weapon pickup before moving
                tile = self.get_tile(new_pos)
                weapon = tile.get_weapon()
                if weapon:
                    self._player.equip(weapon)
                    tile.remove_weapon()
                self._player_position = new_pos
            
            # Perform player's attack
            self.perform_attack(self._player, self._player_position)
            
            # Process end of turn
            self.end_turn()

    def has_won(self) -> bool:
        return (not self._slugs and
            str(self.get_tile(self._player_position)) == GOAL_TILE)


    def has_lost(self) -> bool:
        return not self._player.is_alive()

def load_level(filename: str) -> SlugDungeonModel: # 4.1.14
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    max_health = int(lines[0].strip())
    player = Player(max_health)
    tiles = []
    slugs = {}
    player_position = None
    
    # Start from index 1 (after max_health line)
    for row, line in enumerate(lines[1:]):
        tile_row = []
        for col, char in enumerate(line.strip()):
            # Calculate actual position (row - 1 since we're starting after header)
            position = (row, col)
            
            if char == WALL_TILE:
                tile_row.append(create_tile(WALL_TILE))
            elif char == GOAL_TILE:
                tile_row.append(create_tile(GOAL_TILE))
            elif char in (NICE_SLUG_SYMBOL, ANGRY_SLUG_SYMBOL, SCARED_SLUG_SYMBOL):
                tile_row.append(create_tile(FLOOR_TILE))
                if char == NICE_SLUG_SYMBOL:
                    slugs[position] = NiceSlug()
                elif char == ANGRY_SLUG_SYMBOL:
                    slugs[position] = AngrySlug()
                elif char == SCARED_SLUG_SYMBOL:
                    slugs[position] = ScaredSlug()
            elif char in (POISON_DART_SYMBOL, POISON_SWORD_SYMBOL, HEALING_ROCK_SYMBOL):
                tile = create_tile(FLOOR_TILE)
                if char == POISON_DART_SYMBOL:
                    tile.set_weapon(PoisonDart())
                elif char == POISON_SWORD_SYMBOL:
                    tile.set_weapon(PoisonSword())
                elif char == HEALING_ROCK_SYMBOL:
                    tile.set_weapon(HealingRock())
                tile_row.append(tile)
            elif char == PLAYER_SYMBOL:
                tile_row.append(create_tile(FLOOR_TILE))
                player_position = position
            else:  # Empty floor tile
                tile_row.append(create_tile(FLOOR_TILE))
        tiles.append(tile_row)

    if player_position is None:
        raise ValueError("No player position found in the level file")

    return SlugDungeonModel(tiles, slugs, player, player_position)

class DungeonMap(AbstractGrid):
    def __init__(self, master, dimensions):
        super().__init__(master, dimensions, DUNGEON_MAP_SIZE)
        self.configure(bg=WALL_COLOUR)

    def redraw(self, tiles: 'list[list[Tile]]', player_position: Position, 
            slugs: 'dict[Position, Slug]') -> None:
        self.clear()
        
        # Draw tiles
        for row, tile_row in enumerate(tiles):
            for col, tile in enumerate(tile_row):
                x_min, y_min, x_max, y_max = self.get_bbox((row, col))
                
                # Draw tile background
                if str(tile) == WALL_TILE:
                    color = WALL_COLOUR
                elif str(tile) == GOAL_TILE:
                    color = GOAL_COLOUR
                else:
                    color = FLOOR_COLOUR
                
                self.create_rectangle(
                    x_min, y_min, x_max, y_max,
                    fill=color,
                    outline='black' if color != WALL_COLOUR else ''
                )
                
                # Draw weapon if present
                weapon = tile.get_weapon()
                if weapon:
                    center_x, center_y = self.get_midpoint((row, col))
                    self.create_text(
                        center_x, center_y,
                        text=weapon.get_symbol(),
                        font=REGULAR_FONT
                    )
        
        # Draw entities
        cell_size = min(self.get_cell_size())
        entity_radius = cell_size // 3
        
        # Draw slugs first
        for pos, slug in slugs.items():
            sx, sy = self.get_midpoint(pos)
            color = 'light pink' if slug.can_move() else SLUG_COLOUR
            
            # Draw slug circle
            self.create_oval(
                sx - entity_radius,
                sy - entity_radius,
                sx + entity_radius,
                sy + entity_radius,
                fill=color,
                outline='black'
            )
            
            # Draw slug symbol
            if isinstance(slug, ScaredSlug):
                text = "Scared\nSlug"
            elif isinstance(slug, AngrySlug):
                text = "Angry\nSlug"
            elif isinstance(slug, NiceSlug):
                text = "Nice\nSlug"
            else:
                text = slug.get_symbol()
                
            self.create_text(
                sx, sy,
                text=text,
                font=REGULAR_FONT,
                justify='center'
            )
        
        # Draw player last (so it's on top)
        px, py = self.get_midpoint(player_position)
        self.create_oval(
            px - entity_radius,
            py - entity_radius,
            px + entity_radius,
            py + entity_radius,
            fill=PLAYER_COLOUR,
            outline='black'
        )
        self.create_text(
            px, py,
            text="Player",
            font=REGULAR_FONT,
            fill='black'
        )


class DungeonInfo(AbstractGrid):
    def __init__(self, master, dimensions):
        # Fix the dimensions check for player info
        size = PLAYER_INFO_SIZE if dimensions[0] == 2 else SLUG_INFO_SIZE
        super().__init__(master, dimensions, size)
        self.configure(bg='white')

    def redraw(self, entities: 'dict[Position, Entity]') -> None:
        self.clear()
        
        # Draw headers
        headers = ["Name", "Position", "Weapon", "Health", "Poison"]
        for col, header in enumerate(headers):
            self.annotate_position((0, col), header, font=REGULAR_FONT)

        # Sort entities - Player first, then slugs by position
        sorted_entities = sorted(entities.items(), key=lambda x: (
            not isinstance(x[1], Player),  # Player first
            x[0]  # Then by position
        ))

        # Draw entity information
        for row, (pos, entity) in enumerate(sorted_entities, start=1):
            # Draw each column of information
            # Name
            name = "Player" if isinstance(entity, Player) else entity.get_name()
            self.annotate_position(
                (row, 0),
                name,
                font=REGULAR_FONT
            )
            
            # Position
            self.annotate_position(
                (row, 1),
                f"({pos[0]}, {pos[1]})",
                font=REGULAR_FONT
            )
            
            # Weapon
            weapon = entity.get_weapon()
            weapon_text = weapon.get_name() if weapon else "None"
            self.annotate_position(
                (row, 2),
                weapon_text,
                font=REGULAR_FONT
            )
            
            # Health
            self.annotate_position(
                (row, 3),
                str(entity.get_health()),
                font=REGULAR_FONT
            )
            
            # Poison
            self.annotate_position(
                (row, 4),
                str(entity.get_poison()),
                font=REGULAR_FONT
            )


class ButtonPanel(tk.Frame): # 4.2.3
    def __init__(self, root: tk.Tk, on_load: Callable, on_quit: Callable) -> None:
        super().__init__(root)
        
        # Create Load Game button (leftmost)
        load_button = tk.Button(self, text="Load Game", command=on_load)
        load_button.pack(side='left', padx=5)
        
        # Create Quit button (rightmost)
        quit_button = tk.Button(self, text="Quit", command=on_quit)
        quit_button.pack(side='right', padx=5)

class SlugDungeon: # 4.3.1
    def __init__(self, root: 'tk.Tk', filename: str) -> None:
        self._root = root
        self._filename = filename
        
        # Create left frame for DungeonMap
        left_frame = tk.Frame(root)
        left_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
        
        # Create right frame for info displays
        right_frame = tk.Frame(root)
        right_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)
        
        # Create model
        self._model = load_level(filename)
        
        # Create DungeonMap on left side (500x500)
        self._dungeon_map = DungeonMap(
            left_frame,
            self._model.get_dimensions()
        )
        self._dungeon_map.configure(width=500, height=500)
        self._dungeon_map.pack()
        
        # Create DungeonInfo for slugs on right side (400x500)
        self._slug_info = DungeonInfo(
            right_frame,
            (7, 5)
        )
        self._slug_info.configure(width=400, height=500)
        self._slug_info.pack(fill='x')
        
        # Create bottom frame for player info
        bottom_frame = tk.Frame(root)
        bottom_frame.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
        
        # Create DungeonInfo for player in bottom frame (900x100)
        self._player_info = DungeonInfo(
            bottom_frame,
            (2, 5)
        )
        self._player_info.configure(width=900, height=100)
        self._player_info.pack(fill='x')
        
        # Create ButtonPanel at very bottom
        self._button_panel = ButtonPanel(
            root,
            self.load_level,
            root.destroy
        )
        self._button_panel.grid(row=4, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        
        # Bind keyboard events
        root.bind('<Key>', self.handle_key_press)
        
        # Initial draw
        self.redraw()

    def redraw(self) -> None:
        # Get current game state
        tiles = self._model.get_tiles()
        player_pos = self._model.get_player_position()
        slugs = self._model.get_slugs()
        
        # Update dungeon map view
        self._dungeon_map.redraw(tiles, player_pos, slugs)
        
        # Update slug info view
        self._slug_info.redraw(slugs)
        
        # Update player info view with single player
        player_dict = {player_pos: self._model.get_player()}
        self._player_info.redraw(player_dict)

    def handle_key_press(self, event: 'tk.Event') -> None:
        key = event.char.lower()
        position_delta = None

        if key == 'w':
            position_delta = (-1, 0)
        elif key == 's':
            position_delta = (1, 0)
        elif key == 'a':
            position_delta = (0, -1)
        elif key == 'd':
            position_delta = (0, 1)
        elif key == ' ':
            position_delta = (0, 0)

        if position_delta is not None:
            self._model.handle_player_move(position_delta)
            
            # Check win/loss states before redrawing
            if self._model.has_lost():
                response = messagebox.askyesno(LOSE_TITLE, LOSE_MESSAGE)
                if response:
                    self._model = load_level(self._filename)
                else:
                    self._root.destroy()
                    return
            elif self._model.has_won():
                response = messagebox.askyesno(WIN_TITLE, WIN_MESSAGE)
                if response:
                    self._model = load_level(self._filename)
                else:
                    self._root.destroy()
                    return
                    
            self.redraw()

    def load_level(self) -> None:
        """Prompt for and load a new level file."""
        filename = filedialog.askopenfilename()
        if filename:
            try:
                # Load the new model
                new_model = load_level(filename)
                if new_model:
                    # Update the filename and model
                    self._filename = filename
                    self._model = new_model
                    
                    # Update dungeon map dimensions for the new level
                    self._dungeon_map.set_dimensions(self._model.get_dimensions())
                    
                    # Redraw with new dimensions
                    self.redraw()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load level: {str(e)}")

def play_game(root: 'tk.Tk', file_path: str) -> None: # 4.4
    """
    Play the slug dungeon game.
    
    Parameters:
        root: The root tk.Tk window
        file_path: Path to the level file to load
    """
    root.title("Slug Dungeon")
    # 1. Construct the controller instance
    SlugDungeon(root, file_path)
    
    # 2. Start the event loop
    root.mainloop()
    
def main() -> None: # 4.5
    """
    Main function to start the game.
    Creates root window and starts the game with a level file.
    """
    # 1. Construct the root tk.Tk instance
    root = tk.Tk()
    root.title("Slug Dungeon")
    
    # 2. Call play_game with root and level file
    play_game(root, 'levels/level1.txt')

if __name__ == "__main__":
    main()
