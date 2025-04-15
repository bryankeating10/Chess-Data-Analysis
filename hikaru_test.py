import chess.pgn
import pandas as pd

# Open the PGN file
with open("Training_2.pgn", "r", encoding="utf-8") as pgn_file:
    # Initialize game counter
    game_number = 1

    # Iterate through all games in the file
    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break  # End of file

        print(f"\n--- Game {game_number} ---")
        print("White:", game.headers.get("White"))
        print("Black:", game.headers.get("Black"))
        print("Result:", game.headers.get("Result"))

        # Optional: get main line moves
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
        print("Final Position:\n", board)

        game_number += 1
