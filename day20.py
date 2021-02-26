from __future__ import annotations

import collections
import functools
import math
import re
from typing import Iterator
from typing import NamedTuple

SNAKE_PATTERN0 = re.compile("(?=                  # )".replace(" ", "."))
SNAKE_PATTERN1 = re.compile("#    ##    ##    ###".replace(" ", "."))
SNAKE_PATTERN2 = re.compile(" #  #  #  #  #  #   ".replace(" ", "."))


class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str


class Tile:
    def __init__(self, id: int, lines: tuple[str, ...]) -> None:
        self.id = id
        self.lines = lines

    @functools.cached_property
    def edges(self) -> Edges:
        return Edges(
            self.lines[0],
            "".join(line[-1] for line in self.lines),
            self.lines[-1],
            "".join(line[0] for line in self.lines),
        )

    @functools.cached_property
    def back_edges(self) -> tuple[str, ...]:
        return tuple(edge[::-1] for edge in self.edges)

    @functools.cached_property
    def inner(self) -> tuple[str, ...]:
        return tuple(line[1:-1] for line in self.lines[1:-1])

    def rotate(self) -> Tile:
        line_len = len(self.lines[0])
        lines = tuple(
            "".join(self.lines[line_len - 1 - j][i] for j in range(line_len))
            for i in range(line_len)
        )
        return type(self)(self.id, lines)

    def reflect(self) -> Tile:
        lines = tuple(line[::-1] for line in self.lines)
        return type(self)(self.id, lines)

    def permute(self) -> Iterator[Tile]:
        tile = self
        yield tile
        for _ in range(3):
            tile = tile.rotate()
            yield tile
        tile = tile.reflect()
        yield tile
        for _ in range(3):
            tile = tile.rotate()
            yield tile

    def __repr__(self) -> str:
        lines_str = "\n        ".join(repr(line) for line in self.lines)
        return (
            f"{type(self).__name__}(\n"
            f"    id={self.id},\n"
            f"    lines=(\n"
            f"        {lines_str}\n"
            f"    ),\n"
            f")"
        )


def reader() -> dict[int, Tile]:
    tiles = {}
    with open("inputs/day20.txt") as f:
        for tile_s in f.read().strip().split("\n\n"):
            lines = tile_s.splitlines()
            id = int(lines[0].split()[1][:-1])

            tiles[id] = Tile(id, tuple(lines[1:]))

    return tiles


def _first_corner(tiles: dict[int, Tile]) -> Tile:
    for i, tile in enumerate(tiles.values()):
        matched_edges = set()
        for j, other in enumerate(tiles.values()):
            if i == j:
                continue
            for e_i, edge in enumerate(tile.edges):
                for other_edge in other.edges:
                    if edge == other_edge:
                        matched_edges.add(e_i)
                for other_edge in other.back_edges:
                    if edge == other_edge:
                        matched_edges.add(e_i)
        if len(matched_edges) == 2:
            while matched_edges != {1, 2}:
                tile = tile.rotate()
                matched_edges = {(e_i + 1) % 4 for e_i in matched_edges}
            return tile

    raise AssertionError


def part2() -> int:
    tiles = reader()

    by_connections = collections.defaultdict(set)
    connections = collections.defaultdict(set)
    for i, tile in enumerate(tiles.values()):
        n = 0
        for j, other in enumerate(tiles.values()):
            if i == j:
                continue
            for edge in tile.edges:
                for other_edge in other.edges:
                    if edge == other_edge:
                        n += 1
                        connections[tile.id].add(other.id)
                for other_edge in other.back_edges:
                    if edge == other_edge:
                        n += 1
                        connections[tile.id].add(other.id)

        by_connections[n].add(tile.id)

    corner = _first_corner(tiles)
    prev_bottom = corner.edges.top
    size = int(math.sqrt(len(tiles)))

    rows = []
    for i in range(size):
        row = []
        if i == 0 or i == size - 1:
            target_size = 2  # looking for a corner
        else:
            target_size = 3

        # find first piece
        for id in by_connections[target_size]:
            tile = tiles[id]
            if prev_bottom in tile.edges or prev_bottom in tile.back_edges:
                for tile in tile.permute():
                    if tile.edges.top == prev_bottom:
                        break
                else:
                    raise AssertionError("unreachable: no find first orient")
                row.append(tile)
                by_connections[target_size].discard(id)
                break
        else:
            raise AssertionError("unreachable: no find first piece")

        # append rest of pieces
        for i in range(1, size):
            if i != size - 1:
                inner_target_size = target_size + 1
            else:
                inner_target_size = target_size

            target_edge = row[-1].edges.right
            for id in by_connections[inner_target_size]:
                tile = tiles[id]
                if target_edge in tile.edges or target_edge in tile.back_edges:
                    for tile in tile.permute():
                        if tile.edges.left == target_edge:
                            break
                    else:
                        raise AssertionError("unreachable: no find orient")
                    row.append(tile)
                    by_connections[inner_target_size].discard(id)
                    break
            else:
                raise AssertionError("unreachable: no find next piece")

        rows.append(row)
        prev_bottom = row[0].edges.bottom

    tile_height = len(rows[0][0].inner)

    grid = Tile(
        -1,
        tuple(
            "".join(tile.inner[i] for tile in row)
            for row in rows
            for i in range(tile_height)
        ),
    )

    for grid in grid.permute():
        count = 0
        for i, line in enumerate(grid.lines[:-2]):
            for match in SNAKE_PATTERN0.finditer(line):
                if SNAKE_PATTERN1.match(
                    grid.lines[i + 1], match.start()
                ) and SNAKE_PATTERN2.match(grid.lines[i + 2], match.start()):
                    count += 1

        if count > 0:
            octothorpes = sum(c == "#" for line in grid.lines for c in line)
            return octothorpes - 15 * count

    raise AssertionError("unreachable")


if __name__ == "__main__":
    print(part2())
