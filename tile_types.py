from typing import Tuple

import numpy as np


# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # unicode codepoint
        ("fg", "3B"),  # 3 unsigned bytes for RGB color
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # true if tile can be walked over
        ("transparent", np.bool),  # true if see through
        ("dark", graphic_dt),  # graphics for when this tile is not in FOV
        ("light", graphic_dt),  # graphics for when this tile is in view
    ]
)


def new_tile(
        *,  # Enforce the use of keywords, so that parameter order doesn't matter
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining indvidual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# Shroud represents tiles that are unexplored
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)
