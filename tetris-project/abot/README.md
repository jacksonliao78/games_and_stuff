# Tetris Bot

A simple tetris bot that uses weighted heuristics

## Features

- **Configurable evaluation** — The bot scores each possible placement using 8 weighted factors:
  - **Height** — Penalizes higher stacks (average column height).
  - **Max height** — Penalizes the tallest column.
  - **Holes** — Penalizes empty cells with blocks above them.
  - **Bumpiness** — Penalizes differences between adjacent column heights (prefers flatter surfaces).
  - **Line clears** — Rewards moves that clear lines.
  - **Well depth** — Rewards building a well in the rightmost column (for I-piece tetrises).
  - **Flatness** — Rewards a flatter surface (lower variance of column heights).
  - **Downstack priority** — Extra weight on height when in “downstack” mode.

- **upstack vs downstack** — When average stack height is above 15, the bot switches to *downstack* mode and prioritizes clearing lines; otherwise it *upstacks* and focuses on building a clean stack.

- **Hold logic** — Before each move, the bot compares the best placement for the current piece and the best placement for the hold piece and uses whichever scores higher.

- **Move search** — Uses BFS from spawn to enumerate every valid (x, y, rotation) the piece can reach; each is scored and the best is played. (definitely not super efficint)

- **Speed cap** — Constructor takes a `speed_cap` (max pieces per second) so the bot can be slowed down for viewing or testing.

## Usage

From the tetris project root, the game runs a bot by passing a `Bot` instance and weights:

```python
from abot.bot import Bot

weights = [...]  # 8 floats: height, max_height, holes, bumpiness, line_clears, well_depth, flatness, ds_prio
bot = Bot(speed_cap=10, weights=weights)
game.run_bot(bot)
```

## Evolving weights (`generate.py`)

`generate.py` runs a simple genetic algorithm to tune the bot’s weights:

- **Population** — Starts with random weights; each generation keeps the top 10 by score and breeds/mutates to refill the population.
- **Crossover** — New bots get the average of two parents’ weights.
- **Mutation** — Small random change to each weight with a fixed probability.
- **Fitness** — Score from a 2-minute blitz game.

Run it to evolve better weight sets over many generations.
