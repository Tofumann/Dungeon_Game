from tkinter import filedialog
from a2 import Weapon, PoisonDart, PoisonSword, HealingRock, Tile, create_tile, Entity, Player, Slug, NiceSlug, AngrySlug, ScaredSlug, SlugDungeonModel, load_level, DungeonMap, DungeonInfo, ButtonPanel, SlugDungeon, play_game
import tkinter as tk

# def test_weapon(): # 4.1.1
#     # test 4.1.1
    
    
#     print("Testing Weapon class:")
#     weapon = Weapon()
#     print(f"get_name(): {weapon.get_name()}")
#     print(f"get_symbol(): {weapon.get_symbol()}")
#     print(f"get_effect(): {weapon.get_effect()}")
#     print(f"get_targets((1, 1)): {weapon.get_targets((1, 1))}")
#     print(f"str(weapon): {str(weapon)}")
#     print(f"repr(weapon): {repr(weapon)}")
# if __name__ == "__main__":
#     test_weapon()


# def test_poison_dart(): # 4.1.2
#     poison_dart = PoisonDart()
    
#     print("Testing PoisonDart class:")
#     print(f"get_name(): {poison_dart.get_name()}")
#     print(f"get_symbol(): {poison_dart.get_symbol()}")
#     print(f"get_effect(): {poison_dart.get_effect()}")
#     print(f"get_targets((1, 1)): {poison_dart.get_targets((1, 1))}")
#     print(f"get_targets((8, 8)): {poison_dart.get_targets((8, 8))}")
#     print(f"str(poison_dart): {str(poison_dart)}")
#     print(f"repr(poison_dart): {repr(poison_dart)}")

# if __name__ == "__main__":
#     test_poison_dart()

# def test_poison_sword(): # 4.1.3
#     # 4.1.3
#     poison_sword = PoisonSword()
    
#     print(f"poison_sword.get_name(): {poison_sword.get_name()}")
#     print(f"poison_sword.get_symbol(): {poison_sword.get_symbol()}")
#     print(f"poison_sword.get_effect(): {poison_sword.get_effect()}")
#     print(f"poison_sword.get_targets((1, 1)): {poison_sword.get_targets((1, 1))}")
#     print(f"poison_sword.get_targets((0, 0)): {poison_sword.get_targets((0, 0))}")
#     print(f"str(poison_sword): {str(poison_sword)}")
#     print(f"poison_sword: {poison_sword}")

# if __name__ == "__main__":
#     test_poison_sword()

# def test_healing_rock(): # 4.1.4
#     healing_rock = HealingRock()
    
#     print(f"healing_rock.get_name(): {healing_rock.get_name()}")
#     print(f"healing_rock.get_symbol(): {healing_rock.get_symbol()}")
#     print(f"healing_rock.get_effect(): {healing_rock.get_effect()}")
#     print(f"healing_rock.get_targets((1, 1)): {healing_rock.get_targets((1, 1))}")
#     print(f"str(healing_rock): {str(healing_rock)}")
#     print(f"healing_rock: {healing_rock}")

# if __name__ == "__main__":
#     test_healing_rock()

# def test_tile(): # 4.1.5
#     # Test with a blocking tile
#     tile = Tile("#", True)
#     print(f">>> tile = Tile('#', True)")
#     print(f">>> tile.is_blocking()\n{tile.is_blocking()}")
#     print(f">>> tile.get_weapon()\n{tile.get_weapon()}")
    
#     healing_rock = HealingRock()
#     print(f">>> healing_rock = HealingRock()")
#     print(f">>> tile.set_weapon(healing_rock)")
#     tile.set_weapon(healing_rock)
    
#     print(f">>> tile.get_weapon()\n{tile.get_weapon()}")
#     print(f">>> tile.get_weapon().get_effect()\n{tile.get_weapon().get_effect()}")
    
#     print(f">>> tile.remove_weapon()")
#     tile.remove_weapon()
    
#     print(f">>> tile.get_weapon()\n{tile.get_weapon()}")
#     print(f">>> str(tile)\n'{str(tile)}'")
#     print(f">>> tile\n{repr(tile)}")
    
#     # Test with a non-blocking tile
#     tile = Tile("hello", False)
#     print(f">>> tile = Tile('hello', False)")
#     print(f">>> tile\n{repr(tile)}")
#     print(f">>> tile.is_blocking()\n{tile.is_blocking()}")

# if __name__ == "__main__":
#     test_tile()

# def test_create_tile(): # 4.1.6
#     print(">>> wall = create_tile('#')")
#     wall = create_tile("#")
#     print(f">>> wall\n{repr(wall)}")
#     print(f">>> wall.is_blocking()\n{wall.is_blocking()}")
#     print(f">>> wall.get_weapon()\n{wall.get_weapon()}")

#     print("\n>>> create_tile(' ')")
#     print(repr(create_tile(" ")))

#     print("\n>>> create_tile('hello')")
#     print(repr(create_tile("hello")))

#     print("\n>>> weapon_tile = create_tile('D')")
#     weapon_tile = create_tile("D")
#     print(f">>> weapon_tile\n{repr(weapon_tile)}")
#     print(f">>> weapon_tile.get_weapon()\n{repr(weapon_tile.get_weapon())}")

# if __name__ == "__main__":
#     test_create_tile()

# def test_entity(): # 4.1.7
#     entity = Entity(10)
#     print(">>> entity = Entity(10)")
#     print(f">>> entity.get_symbol()\n'{entity.get_symbol()}'")
#     print(f">>> entity.get_name()\n'{entity.get_name()}'")
#     print(f">>> entity.get_health()\n{entity.get_health()}")
#     print(f">>> entity.get_poison()\n{entity.get_poison()}")
#     print(f">>> entity.get_weapon()\n{entity.get_weapon()}")
#     print(f">>> entity.get_weapon_targets((1, 1))\n{entity.get_weapon_targets((1, 1))}")
#     print(f">>> entity.get_weapon_effect()\n{entity.get_weapon_effect()}")
    
#     entity.equip(PoisonSword())
#     print(">>> entity.equip(PoisonSword())")
#     print(f">>> entity.get_weapon()\n{entity.get_weapon()}")
#     print(f">>> entity.get_weapon_targets((0, 0))\n{entity.get_weapon_targets((0, 0))}")
#     print(f">>> entity.get_weapon_effect()\n{entity.get_weapon_effect()}")
    
#     entity.apply_effects({'poison': 4, 'damage': 3})
#     print(">>> entity.apply_effects({'poison': 4, 'damage': 3})")
#     print(f">>> entity.get_health()\n{entity.get_health()}")
#     print(f">>> entity.get_poison()\n{entity.get_poison()}")
    
#     entity.apply_poison()
#     print(">>> entity.apply_poison()")
#     print(f">>> entity.get_health()\n{entity.get_health()}")
#     print(f">>> entity.get_poison()\n{entity.get_poison()}")
    
#     entity.apply_effects({'healing': 20})
#     print(">>> entity.apply_effects({'healing': 20})")
#     print(f">>> entity.get_health()\n{entity.get_health()}")
    
#     print(f">>> str(entity)\n'{str(entity)}'")
#     print(f">>> entity\n{repr(entity)}")

# if __name__ == "__main__":
#     test_entity()

# def test_player(): # 4.1.8
#     player = Player(20)
#     print(">>> player = Player(20)")
#     print(f">>> str(player)\n'{str(player)}'")
#     print(f">>> player\n{repr(player)}")
    
#     player.equip(PoisonDart())
#     print(">>> player.equip(PoisonDart())")
#     print(f">>> player.get_weapon_effect()\n{player.get_weapon_effect()}")
    
#     player.apply_effects({'damage': 25})
#     print(">>> player.apply_effects({'damage': 25})")
#     print(f">>> player.get_health()\n{player.get_health()}")
    
#     print(f">>> player\n{repr(player)}")

# if __name__ == "__main__":
#     test_player()

# class TestSlug(Slug): # 4.1.9
#     def choose_move(self, candidates, current_position, player_position):
#         return current_position  # Just return current position for testing

# def test_slug(): # 4.1.9
#     slug = TestSlug(5)
#     print(">>> slug = Slug(5)")
#     slug.equip(HealingRock())
#     print(">>> slug.equip(HealingRock())")
#     print(f">>> slug.get_weapon_effect()\n{slug.get_weapon_effect()}")
#     print(f">>> slug.can_move()\n{slug.can_move()}")
#     print(">>> slug.end_turn()")
#     slug.end_turn()
#     print(f">>> slug.can_move()\n{slug.can_move()}")
#     print(">>> slug.can_move()")
#     print(slug.can_move())
#     print(">>> slug.end_turn()")
#     slug.end_turn()
#     print(f">>> slug.can_move()\n{slug.can_move()}")
#     try:
#         print(">>> slug.choose_move([(0, 0), (1, 1)], (1, 0), (2, 4))")
#         slug.choose_move([(0, 0), (1, 1)], (1, 0), (2, 4))
#     except NotImplementedError as e:
#         print(f"NotImplementedError: {str(e)}")
#     print(f">>> str(slug)\n'{str(slug)}'")
#     print(f">>> slug\n{slug}")

# if __name__ == "__main__":
#     test_slug()

# def test_nice_slug(): # 4.1.10
#     nice_slug = NiceSlug()
#     print(">>> nice_slug = NiceSlug()")
#     print(f">>> nice_slug\n{nice_slug}")
#     print(f">>> str(nice_slug)\n'{str(nice_slug)}'")
#     print(f">>> nice_slug.get_health()\n{nice_slug.get_health()}")
#     print(f">>> nice_slug.get_weapon()\n{nice_slug.get_weapon()}")
#     print(f">>> nice_slug.get_weapon_effect()\n{nice_slug.get_weapon_effect()}")
#     print(">>> nice_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4))")
#     print(nice_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4)))

# if __name__ == "__main__":
#     test_nice_slug()

# def test_angry_slug(): # 4.1.11
#     angry_slug = AngrySlug()
#     print(">>> angry_slug = AngrySlug()")
#     print(f">>> angry_slug\n{angry_slug}")
#     print(f">>> str(angry_slug)\n'{str(angry_slug)}'")
#     print(f">>> angry_slug.get_health()\n{angry_slug.get_health()}")
#     print(f">>> angry_slug.get_weapon()\n{angry_slug.get_weapon()}")
#     print(f">>> angry_slug.get_weapon_effect()\n{angry_slug.get_weapon_effect()}")
#     print(">>> angry_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4))")
#     print(angry_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4)))

# if __name__ == "__main__":
#     test_angry_slug()

# def test_scared_slug(): # 4.1.12
#     scared_slug = ScaredSlug()
#     print(">>> scared_slug = ScaredSlug()")
#     print(f">>> scared_slug\n{scared_slug}")
#     print(f">>> str(scared_slug)\n'{str(scared_slug)}'")
#     print(f">>> scared_slug.get_health()\n{scared_slug.get_health()}")
#     print(f">>> scared_slug.get_weapon()\n{scared_slug.get_weapon()}")
#     print(f">>> scared_slug.get_weapon_effect()\n{scared_slug.get_weapon_effect()}")
#     print(">>> scared_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4))")
#     print(scared_slug.choose_move([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (2, 4)))

# if __name__ == "__main__":
#     test_scared_slug()

# def test_slug_dungeon_model(): # 4.1.13
#     tiles = [
#         [create_tile("#"), create_tile("#"), create_tile("#"), create_tile("#")],
#         [create_tile("#"), create_tile(" "), create_tile(" "), create_tile("#")],
#         [create_tile("#"), create_tile(" "), create_tile(" "), create_tile("#")],
#         [create_tile("#"), create_tile("S"), create_tile("G"), create_tile("#")],
#         [create_tile("#"), create_tile("#"), create_tile("#"), create_tile("#")]
#     ]
#     slugs = {(1, 1): AngrySlug()}
#     player = Player(20)
#     model = SlugDungeonModel(tiles, slugs, player, (2, 1))

#     print(">>> model.get_tiles()")
#     print(model.get_tiles())
#     print(">>> model.get_slugs()")
#     print(model.get_slugs())
#     print(">>> model.get_player()")
#     print(model.get_player())
#     print(">>> model.get_player_position()")
#     print(model.get_player_position())
#     print(">>> model.get_tile((0, 0))")
#     print(model.get_tile((0, 0)))
#     print(">>> model.get_tile((2, 1))")
#     print(model.get_tile((2, 1)))
#     print(">>> model.get_dimensions()")
#     print(model.get_dimensions())

#     angry_slug = model.get_slugs().get((1, 1))
#     print(">>> angry_slug.get_health()")
#     print(angry_slug.get_health())
#     print(">>> angry_slug.get_weapon_effect()")
#     print(angry_slug.get_weapon_effect())
#     print(">>> player.get_health()")
#     print(player.get_health())
#     print(">>> angry_slug.get_poison()")
#     print(angry_slug.get_poison())
#     print(">>> player.get_poison()")
#     print(player.get_poison())
#     print(">>> player.get_weapon_effect()")
#     print(player.get_weapon_effect())
#     print(">>> model.get_valid_slug_positions(angry_slug)")
#     print(model.get_valid_slug_positions(angry_slug))

#     model.perform_attack(angry_slug, (1, 1))
#     print(">>> player.get_health()")
#     print(player.get_health())
#     print(">>> player.get_poison()")
#     print(player.get_poison())

#     model.perform_attack(player, model.get_player_position())
#     print(">>> angry_slug.get_health()")
#     print(angry_slug.get_health())
#     print(">>> angry_slug.get_poison()")
#     print(angry_slug.get_poison())

#     model.handle_player_move((1, 0))
#     print(">>> player.get_health()")
#     print(player.get_health())
#     print(">>> player.get_poison()")
#     print(player.get_poison())
#     print(">>> player.get_weapon()")
#     print(player.get_weapon())
#     print(">>> player.get_weapon_effect()")
#     print(player.get_weapon_effect())
#     print(">>> player.get_weapon_targets(model.get_player_position())")
#     print(player.get_weapon_targets(model.get_player_position()))
#     print(">>> angry_slug.get_health()")
#     print(angry_slug.get_health())
#     print(">>> angry_slug.get_poison()")
#     print(angry_slug.get_poison())
#     print(">>> model.get_slugs()")
#     print(model.get_slugs())
#     print(">>> model.get_player_position()")
#     print(model.get_player_position())
#     print(">>> model.has_won()")
#     print(model.has_won())
#     print(">>> model.has_lost()")
#     print(model.has_lost())

# if __name__ == "__main__":
#     test_slug_dungeon_model()

# def test_load_level(): # 4.1.14
#     model = load_level('levels/level1.txt')
    
#     # Get dimensions
#     rows, cols = model.get_dimensions()
#     print(f"Dimensions: {rows}x{cols}")
    
#     # Print player max health
#     print(f"Player Max Health: {model.get_player().get_health()}")
#     print()
    
#     # Create a text representation of the level
#     level_display = []
#     for row in range(rows):
#         row_display = []
#         for col in range(cols):
#             position = (row, col)
#             # Check for player
#             if position == model.get_player_position():
#                 row_display.append('P')
#             # Check for slugs
#             elif position in model.get_slugs():
#                 slug = model.get_slugs()[position]
#                 if isinstance(slug, AngrySlug):
#                     row_display.append('A')
#                 elif isinstance(slug, NiceSlug):
#                     row_display.append('N')
#                 elif isinstance(slug, ScaredSlug):
#                     row_display.append('L')
#             # Check for tiles and weapons
#             else:
#                 tile = model.get_tile(position)
#                 weapon = tile.get_weapon()
#                 if weapon:
#                     if isinstance(weapon, PoisonSword):
#                         row_display.append('S')
#                     else:
#                         row_display.append(str(weapon)[0])
#                 else:
#                     row_display.append(str(tile))
#         level_display.append(''.join(row_display))
    
#     # Print the level representation
#     print("Level Layout:")
#     for row in level_display:
#         print(row)
    
#     # Print entity positions
#     print("\nEntity Positions:")
#     print(f"Player: {model.get_player_position()}")
#     for pos, slug in model.get_slugs().items():
#         print(f"{type(slug).__name__}: {pos}")

# if __name__ == "__main__":
#     test_load_level()

# def test_load_level(): # 4.1.14 level2
#     model = load_level('levels/level2.txt')
    
#     # Get dimensions
#     rows, cols = model.get_dimensions()
#     print(f"Dimensions: {rows}x{cols}")
    
#     # Print player max health
#     print(f"Player Max Health: {model.get_player().get_health()}")
#     print()
    
#     # Create a text representation of the level
#     level_display = []
#     for row in range(rows):
#         row_display = []
#         for col in range(cols):
#             position = (row, col)
#             # Check for player
#             if position == model.get_player_position():
#                 row_display.append('P')
#             # Check for slugs
#             elif position in model.get_slugs():
#                 slug = model.get_slugs()[position]
#                 if isinstance(slug, AngrySlug):
#                     row_display.append('A')
#                 elif isinstance(slug, NiceSlug):
#                     row_display.append('N')
#                 elif isinstance(slug, ScaredSlug):
#                     row_display.append('L')
#             # Check for tiles and weapons
#             else:
#                 tile = model.get_tile(position)
#                 weapon = tile.get_weapon()
#                 if weapon:
#                     if isinstance(weapon, PoisonSword):
#                         row_display.append('S')
#                     else:
#                         row_display.append(str(weapon)[0])
#                 else:
#                     row_display.append(str(tile))
#         level_display.append(''.join(row_display))
    
#     # Print the level representation
#     print("Level Layout:")
#     for row in level_display:
#         print(row)
    
#     # Print entity positions
#     print("\nEntity Positions:")
#     print(f"Player: {model.get_player_position()}")
#     for pos, slug in model.get_slugs().items():
#         print(f"{type(slug).__name__}: {pos}")

# if __name__ == "__main__":
#     test_load_level()

# def test_dungeon_map(): # 4.2.1
#     root = tk.Tk()
#     root.title("DungeonMap Test")

#     # Test with level1
#     print("Testing Level 1:")
#     model1 = load_level('levels/level1.txt')
#     dimensions1 = model1.get_dimensions()
    
#     dungeon_map1 = DungeonMap(root, dimensions1)
#     dungeon_map1.pack(padx=10, pady=10)
#     dungeon_map1.redraw(
#         model1.get_tiles(),
#         model1.get_player_position(),
#         model1.get_slugs()
#     )
    
#     # Create a button to switch to level2
#     def switch_to_level2():
#         dungeon_map1.pack_forget()
        
#         model2 = load_level('levels/level2.txt')
#         dimensions2 = model2.get_dimensions()
        
#         dungeon_map2 = DungeonMap(root, dimensions2)
#         dungeon_map2.pack(padx=10, pady=10)
#         dungeon_map2.redraw(
#             model2.get_tiles(),
#             model2.get_player_position(),
#             model2.get_slugs()
#         )

#     switch_button = tk.Button(root, text="Switch to Level 2", command=switch_to_level2)
#     switch_button.pack(pady=5)
    
#     # Add a quit button
#     quit_button = tk.Button(root, text="Quit", command=root.destroy)
#     quit_button.pack(pady=5)

#     # Print verification info
#     print("\nVerification Points:")
#     print("1. Check that walls are dark brown")
#     print("2. Check that floor tiles are light colored with black outlines")
#     print("3. Check that the goal tile is yellow")
#     print("4. Check that the player is shown as a blue circle with 'Player' text")
#     print("5. Check that slugs are shown as:")
#     print("   - Green circles when they cannot move")
#     print("   - Light pink circles when they can move")
#     print("6. Check that weapons (S) are shown as text on their tiles")
#     print("7. Check that all positions match the level file layout")
#     print("\nExpected Level 1 Layout:")
#     print("- Player at bottom left")
#     print("- AngrySlug at top right (should be in green)")
#     print("- Weapon 'S' in the middle")
#     print("\nExpected Level 2 Layout:")
#     print("- Player at top left")
#     print("- AngrySlug at top right")
#     print("- NiceSlug in middle right")
#     print("- Weapon 'S' at bottom")
    
#     root.mainloop()

# if __name__ == "__main__":
#     test_dungeon_map()


# def test_dungeon_info(): # 4.2.2
#     root = tk.Tk()
    
#     # Create a DungeonInfo instance
#     dimensions = (5, 5)  # Sample dimensions
#     info = DungeonInfo(root, dimensions)
#     info.pack()

#     # Create sample entities
#     player = Player(30)
#     player.equip(PoisonSword())
#     entities = {(6, 4): player}

#     # Test redraw method
#     info.redraw(entities)
    
#     root.mainloop()

# if __name__ == "__main__":
#     test_dungeon_info()


# def test_button_panel(): # 4.2.3
#     root = tk.Tk()
#     root.title("Button Panel Test")
    
#     def on_load():
#         print("Load Game clicked")
    
#     def on_quit():
#         root.destroy()
    
#     # Create and pack the button panel
#     panel = ButtonPanel(root, on_load, on_quit)
#     panel.pack(pady=10)
    
#     root.mainloop()

# if __name__ == "__main__":
#     test_button_panel()


# def test_slug_dungeon():
#     root = tk.Tk()
#     root.title("Slug Dungeon")
    
#     game = SlugDungeon(root, 'levels/level1.txt')
    
#     root.mainloop()

# if __name__ == "__main__":
#     test_slug_dungeon()

# def test_play_game():
#     root = tk.Tk()
#     root.title("Slug Dungeon")
    
#     # Test with level1.txt
#     play_game(root, 'levels/level1.txt')

# if __name__ == "__main__":
#     test_play_game()

import unittest
from typing import List, Tuple, Dict, Optional
from a2 import *

class TestGameplay(unittest.TestCase):
# Test the exact scenario from failing tests
    def test_scenario(self):
        initial_pos = self.model.get_player_position()
        initial_health = self.model.get_player().get_health()
        
        # First wait
        self.model.handle_player_move((0, 0))
        print(f"After first wait - Health: {self.model.get_player().get_health()}, "
            f"Poison: {self.model.get_player().get_poison()}")
        
        # Second wait    
        self.model.handle_player_move((0, 0))
        print(f"After second wait - Health: {self.model.get_player().get_health()}, "
            f"Poison: {self.model.get_player().get_poison()}")
        
        self.assertFalse(self.model.has_lost())
        
        # Third wait
        self.model.handle_player_move((0, 0))
        print(f"After third wait - Health: {self.model.get_player().get_health()}, "
            f"Poison: {self.model.get_player().get_poison()}")

if __name__ == '__main__':
    unittest.main()