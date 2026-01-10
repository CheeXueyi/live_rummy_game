# Rummy Game Design Discussion Notes

## Collection Naming
- **SequenceCollection**: For consecutive same-suit sequences (2, 3, 4, ...)
- **SameRankCollection**: For same-rank different-suit collections (2♥, 2♦, 2♠, ...)
- Recommendation: These names are clear and domain-standard.

## Architecture: Game Loop Location
- **Decision**: Put game loop logic in `Rummy_Game` class
- **Rationale**: Single responsibility - no unnecessary wrapper classes
- **Rummy_Game responsibilities**:
  - Manages players, piles, table collections
  - Executes turn validation
  - Applies moves to game state
  - Determines win condition
  - Calculates final scores
- **Separation**: Player/AI decides moves (strategy), Rummy_Game orchestrates (state management)

## Tile Class Design
- **Decision**: Use single `Normal_Tile` class, not individual classes per rank
- **Rationale**: 
  - All normal tiles behave identically
  - Points are deterministic based on rank
  - Avoids 13+ unnecessary classes
- **Implementation**: Extract points calculation into helper function
  ```python
  def get_tile_points(rank: Rank) -> int:
      if rank == Rank.ACE: return 15
      elif rank in (Rank.JACK, Rank.QUEEN, Rank.KING): return 10
      elif Rank.TWO <= rank <= Rank.TEN: return rank.value
  ```
- **Tile constructor**: `Normal_Tile(suit, rank)` - compute points, don't pass as parameter

## Missing Core Classes
1. **Discard_Pile**: Separate from Draw_Pile. Players can draw last discarded tile instead of from deck.
2. **Player**: Holds Hand, tracks identity and turn position
3. **Rummy_Game**: Main orchestrator (currently commented out)

## Data Structure Improvements
- **Hand.tiles**: Change to `deque` for efficient removal during gameplay
  ```python
  self.tiles = deque(starting_tiles)
  ```
- **SameRankCollection**: Using `set()` is risky (allows accidental duplicates). Use `list` instead with explicit duplicate checks.

## Table Class Design
- **Pros**:
  - Cleaner separation of concerns
  - Easier to test collection logic in isolation
  - Single place for collection-related queries/validation
  - Better for future features (arrangement, visualization)
- **Cons**:
  - Adds complexity for MVP
  - Extra layer of indirection
  - Over-engineering for simple list of collections
- **Recommendation**: Skip for MVP. Start with `list[Collection]` in `Rummy_Game`. Refactor later if needed.

## Game Objects Summary (Current)
- **Tile** (abstract) → Normal_Tile, Rummy_Tile
- **Collection** (abstract) → SequenceCollection, SameRankCollection
- **Hand** (needs deque fix)
- **Draw_Pile**, **Discard_Pile** (missing)
- **Player** (missing)
- **Rummy_Game** (needs implementation)

## Next Steps
1. Implement `get_tile_points()` helper
2. Add `Discard_Pile` and `Player` classes
3. Uncomment and flesh out `Rummy_Game` with core methods:
   - `get_current_player()`
   - `validate_move()`
   - `apply_move()`
   - `next_turn()`
   - `is_finished()`
   - `get_scores()`
4. Implement collection validation logic (sequences, same rank checks)

# Dealing with played rummy tiles
After rummy is played, the rummy takes on an identity of a normal tile.
We need to deal with this somehow in our data models.
Implement this by giving normal tile a flag "was rummy tile"
Then when a rummy tile gets played, player has to specify the identity of the rummy tile
This is when we instantiate a new normal tile of the player's choosing with the rummy tile set

