

def inital_state():
    state = (
        0,0,0,
        0,0,0,
        0,0,0
    )
    return state


def legal_state(state):
    """Returns a list of indices representing legal moves (empty positions)."""
    return [i for i, val in enumerate(state) if val == 0]


def next_state(state, action, player):
    """Returns a new state tuple after placing player mark at the action index."""
    new_state = list(state)
    new_state[action] = player
    return tuple(new_state)




WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def winner(state):
    """
    Returns:
        1 (X) if X won,
       -1 (O) if O won,
        0 if draw,
        None if game is still running.
    """
    for a, b, c in WIN_LINES:
        if state[a] == state[b] == state[c] != 0:
            return state[a]
    if 0 not in state:
        return 0
    return None


def render(state):
    """Renders the 3x3 Tic-Tac-Toe board to stdout."""
    symbols = {1: 'X', -1: 'O', 0: ' '}
    chars = [symbols[val] for val in state]
    print(f"{chars[0]} | {chars[1]} | {chars[2]}")
    print("---------")
    print(f"{chars[3]} | {chars[4]} | {chars[5]}")
    print("---------")
    print(f"{chars[6]} | {chars[7]} | {chars[8]}")


def main():
    EMPTY = 0
    X = 1
    O = -1

    state = (
        1, 0, -1,
        0, 1, 0,
        0, 0, -1,
    )
    render(state)
    print("Winner:", winner(state))


if __name__ == "__main__":
    main()