import chess.pgn

pgn = open('Training_1.pgn.txt.')
game = chess.pgn.read_game(pgn)

board = game.board()
for move in game.mainline_moves():
	board.push(move)

print(board)
print(game.headers["White"], "vs", game.headers["Black"])
print('test')