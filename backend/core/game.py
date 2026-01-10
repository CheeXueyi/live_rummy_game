from abc import ABC, abstractmethod
from enum import Enum
from collections import deque

RUMMY_POINTS = 20


class Tile(ABC):
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

RANK_ORDER = {
    Rank.ACE: 1,
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4,
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 11,
    Rank.QUEEN: 12,
    Rank.KING: 13,
}

class Normal_Tile(Tile):
    def __init__(self, suit: Suit, rank: Rank, is_rummy: bool = False):
        self.suit = suit
        self.rank = rank
        self.is_rummy = is_rummy # keep track of this for rendering purpose


class Rummy_Tile(Tile):
    pass

class Hand:
    def __init__(self, starting_tiles: list[Tile]):
        self.tiles = starting_tiles

class Draw_Pile:
    def __init__(self):
        self.pile: deque[Tile] = deque()

class Collection(ABC):
    @abstractmethod
    def can_add_front(self, tile: Normal_Tile) -> bool:
        "Returns True if given tile can be added to the front of this collection"
        pass

    @abstractmethod
    def can_add_back(self, tile: Normal_Tile) -> bool:
        "Returns True if given tile can be added to the back of this collection"
        pass
    
    @abstractmethod
    def add_tile_front(self, tile: Normal_Tile) -> bool:
        "adds given Tile to front of this Collection. Returns whether the move is successfull or not"
        pass

    @abstractmethod
    def add_tile_back(self, tile: Normal_Tile) -> bool:
        "adds given Tile to the back of this Collection. Returns whether the move is successfull or not"
        pass



class SequenceCollection(Collection):
    def __init__(self, starting_collection: list[Normal_Tile], suit: Suit):
        # error checks
        self.collection = deque(starting_collection)
        self.suit = suit


    def can_add_front(self, tile: Normal_Tile) -> bool:
        # make a list of the collection after tile is added
        collection_preview = [tile]
        collection_preview.extend(list(self.collection))
        
        # check if collection with added tile is valid
        return self._is_valid(collection_preview)
            

    def can_add_back(self, tile: Normal_Tile) -> bool:
        # make a list of the colleciton after tile is added
        collection_preview = list(self.collection)
        collection_preview.append(tile)

        # check if collection with added tile is valid
        return self._is_valid(collection_preview)


    def add_tile_front(self, tile: Normal_Tile) -> bool:
        if not self.can_add_front(tile):
            return False
        
        self.collection.appendleft(tile)
        return True


    def add_tile_back(self, tile: Normal_Tile) -> bool:
        if not self.can_add_back(tile):
            return False

        self.collection.append(tile)
        return True


    def _is_valid(self, collection: list[Normal_Tile]) -> bool:
        "Returns true if the passed in collection is a valid sequence collection"
        # check that it is the correct length
        if len(collection) < 3 or len(collection) > 14:
            return False

        # check that all tiles have the same suit
        for i in range(len(collection) - 1):
            curr_tile = collection[i]
            next_tile = collection[i + 1]
            if curr_tile.suit != next_tile.suit:
                return False
            
        # check that tiles are in increasing order
        for i in range(len(collection) - 1):
            curr_tile = collection[i]
            next_tile = collection[i + 1]
            # last tile can be ace following a king
            if i + 1 == len(collection) - 1 and curr_tile.rank == Rank.KING and next_tile.rank == Rank.ACE:
                continue

            # besides the edge case above, all others must be consecutive in correct order
            curr_tile_order = RANK_ORDER[curr_tile.rank]
            next_tile_order = RANK_ORDER[next_tile.rank]
            if curr_tile_order != next_tile_order - 1:
                return False
        
        # all checks passed
        return True



class SameRankCollection(Collection):
    def __init__(self, starting_collection: list[Normal_Tile], rank: Rank):
        self.collection = set(starting_collection)
        self.rank = rank


    def can_add_front(self, tile: Normal_Tile) -> bool:
        return self._can_add(tile)


    def can_add_back(self, tile: Normal_Tile) -> bool:
        return self._can_add(tile)


    def add_tile_front(self, tile: Normal_Tile) -> bool:
        return self. _add_tile(tile)

        
    def add_tile_back(self, tile: Normal_Tile) -> bool:
        return self. _add_tile(tile)
    

    def _add_tile(self, tile: Normal_Tile) -> bool:
        """
        Adds a tile to this collection.
        Returns true if given tile can be added to this collection. 
        Returns false and does nothing if given tile cannot be added to this collection
        Needed because same rank collection has no notion of front or back"
        """
        if not self._can_add(tile):
            return False

        self.collection.add(tile)
        return True


    def _can_add(self, tile: Normal_Tile) -> bool:
        " "
        return tile.rank == self.rank
        
    

# class Rummy_Game:
#     def __init__(self):
        