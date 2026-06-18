
EMPTY = 0
X = 1
O = -1

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


def initial_state():
    return (0,) * 9


def legal_actions(state):
    """Returns a list of indices representing legal moves (empty positions)."""
    return [i for i, val in enumerate(state) if val == 0]


def next_state(state, action, player):
    """Returns a new state tuple after placing player mark at the action index."""

    assert state[action] == EMPTY
    assert action in legal_actions(state)

    new_state = list(state)
    new_state[action] = player
    return tuple(new_state)


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


def get_value(state, values):
    res = winner(state)
    if res == 1:
        return 1.0
    elif res == -1 or res == 0:
        return 0.0

    if state not in values:
        values[state] = 0.5
    return values[state]


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
    state = initial_state()
    assert legal_actions(state) == list(range(9))

    s1 = next_state(state, 4, X)
    assert state[4] == EMPTY
    assert s1[4] == X

    x_win = (
        1, 0, -1,
        0, 1, 0,
        0, 0, 1,
    )

    o_win = (
        -1, -1, -1,
        0, 1, 0,
        0, 0, 1,
    )

    draw = (
        1, -1, 1,
        1, -1, -1,
        -1, 1, 1
    )

    assert winner(x_win) == X
    assert winner(draw) == 0

    values = {}
    # Nonterminal unseen
    assert get_value(state, values) == 0.5
    assert state in values
    # Nonterminal seen (modified value)
    values[state] = 0.8
    assert get_value(state, values) == 0.8
    # Terminal X win
    assert get_value(x_win, values) == 1.0
    # Terminal O win
    assert get_value(o_win, values) == 0.0
    # Terminal draw
    assert get_value(draw, values) == 0.0

    render(state)
    print("Winner:", winner(state))



if __name__ == "__main__":
    main()
