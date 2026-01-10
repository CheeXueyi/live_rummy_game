from game import Tile, Rummy_Tile, Normal_Tile, Rank
from typing import NamedTuple

RANK_SCORES = {
    Rank.ACE: 15,
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4,
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 10,
    Rank.QUEEN: 10,
    Rank.KING: 10
}

RUMMY_TILE_SCORE = 20


def get_normal_tile_score(tile: Normal_Tile) -> int:
    if tile.rank not in RANK_SCORES:
        raise Exception("INVALID RANK")
    return RANK_SCORES[tile.rank]    


def get_tile_score(tile: Tile) -> int:
    if isinstance(tile, Normal_Tile):
        return get_normal_tile_score(tile)

    if isinstance(tile, Rummy_Tile):
        return RUMMY_TILE_SCORE

    raise Exception("TILE TYPE NOT COVERED BY SCORE CALCULATION")
