import collections
import itertools
from collections import deque
from typing import Deque
from typing import Tuple


def reader():
    with open("inputs/day22.txt") as f:
        player1, player2 = f.read().split("\n\n")
        player1 = deque(int(i) for i in player1.splitlines()[1:])
        player2 = deque(int(i) for i in player2.splitlines()[1:])

        return player1, player2


def part1():
    def play_game(
        player1: Deque[int], player2: Deque[int]
    ) -> Tuple[Deque[int], Deque[int]]:
        while player1 and player2:
            card1, card2 = player1.popleft(), player2.popleft()

            if card1 > card2:
                player1.extend((card1, card2))
            else:
                player2.extend((card2, card1))

        return player1, player2

    player1, player2 = reader()
    player1, player2 = play_game(player1, player2)

    total = 0
    if player1:
        for i, n in enumerate(reversed(player1), 1):
            total += i * n
    else:
        for i, n in enumerate(reversed(player2), 1):
            total += i * n

    return total


def part2():
    def play_game(player1: Deque[int], player2: Deque[int]) -> Tuple[bool, Deque[int]]:
        seen = set()

        while True:
            if player1 and not player2:
                return True, player1
            elif player2 and not player1:
                return False, player2

            game_state = (tuple(player1), tuple(player2))
            if game_state in seen:
                return True, player1

            card1, card2 = player1.popleft(), player2.popleft()
            if card1 <= len(player1) and card2 <= len(player2):
                sub_player1 = collections.deque(itertools.islice(player1, card1))
                sub_player2 = collections.deque(itertools.islice(player2, card2))
                player1_won, _ = play_game(sub_player1, sub_player2)
                if player1_won:
                    player1.extend((card1, card2))
                else:
                    player2.extend((card2, card1))

            elif card1 > card2:
                player1.extend((card1, card2))

            else:
                player2.extend((card2, card1))

            seen.add(game_state)

    player1, player2 = reader()
    _, result = play_game(player1, player2)

    total = 0
    for i, el in enumerate(reversed(result), 1):
        total += i * el

    return total


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
