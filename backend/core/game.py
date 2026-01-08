from abc import ABC, abstractmethod
from enum import Enum
from collections import deque

RUMMY_POINTS = 20


class Tile(ABC):
    @abstractmethod
    def get_points(self):
        '''Returns the number of ponts this tile is worth'''
        pass

class Suit(Enum):
    DIAMOND = 0
    CLUB = 1
    HEART = 2
    SPADE = 3

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Normal_Tile(Tile):
    def __init__(self, suit: Suit, rank: Rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def get_points(self):
        return self.points
    
class Rummy_Tile(Tile):
    def __init__(self):
        self.points = RUMMY_POINTS
    
    def get_points(self):
        return self.points

class Hand:
    def __init__(self, starting_tiles: list[Tile]):
        self.tiles = starting_tiles

class Draw_Pile:
    def __init__(self):
        self.pile: deque[Tile] = deque()

class Collection(ABC):
    @abstractmethod
    def can_add(self, tile: Tile) -> bool:
        "Returns True if given tile can be added to this Collection"
        pass

    @abstractmethod
    def add_tile(self, tile: Tile) -> bool:
        "adds given Tile to this Collection. Returns whether the move is successfull or not"
        pass

class SequenceCollection(Collection):
    def __init__(self, starting_collection: list[Tile], suit: Suit):
        self.collection = deque(starting_collection)
        self.suit = suit
    
    def can_add(self, tile: Tile) -> bool:
        # TODO
        return False

    def add_tile(self, tile: Tile) -> bool:
        # TODO
        return False
    
class SameRankCollection(Collection):
    def __init__(self, starting_collection: list[Tile], rank: Rank):
        self.collection = set(starting_collection)
        self.rank = rank
    
    def can_add(self, tile: Tile) -> bool:
        # TODO
        return False

    def add_tile(self, tile: Tile) -> bool:
        # TODO
        return False


# class Rummy_Game:
#     def __init__(self):
        