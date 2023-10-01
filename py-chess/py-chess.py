import chess
import chess.engine

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.engine_path = "/home/username/Desktop/py-chess/stockfish/stockfish-ubuntu-x86-64-modern"

    def display_board(self):
        UNICODE_PIECES = {
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
        }
        tiles = [["▒" if (i+j)%2 else " " for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.board.piece_at(chess.square(j, 7-i)):
                    tiles[i][j] = UNICODE_PIECES[self.board.piece_at(chess.square(j, 7-i)).symbol()]
        
        for i, row in enumerate(tiles[::-1], start=1):
            print(f"{i} {' '.join(row)}")
        print("   a b c d e f g h")

    def get_player_move(self):
        while True:
            try:
                move_str = input("Enter your move (e.g., e2e4): ")
                move = chess.Move.from_uci(move_str)
                if move in self.board.legal_moves:
                    return move
                print("Illegal move!")
            except ValueError:
                print("Invalid move format. Try again.")

    def get_bot_move(self):
        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
            result = engine.play(self.board, chess.engine.Limit(time=1.0))
            return result.move

    def play(self):
        self.display_board()
        while not self.board.is_game_over():
            if self.board.turn == chess.WHITE:
                move = self.get_player_move()
                self.board.push(move)
                self.display_board()
            else:
                print("Black's (Bot's) turn...")
                move = self.get_bot_move()
                self.board.push(move)
                self.display_board()

        print("Game Over!\nResult:", self.board.result())

game = ChessGame()
game.play()
