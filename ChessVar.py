# Author: April Wang 
# GitHub username: xiaolongbytes 
# Date: 03/04/2024 
# Description: This project implements a variant of chess that involves falcon and hunter pieces, where victory is
#               determined by capturing the king. There is no check/checkmate, no castling, en passant, or pawn promotion.
#               Locations on the board are specified with "algebraic notation"

class Board:
    """Represents a board with chess pieces
    Contains Piece objects and EmptySquare objects
    Is called by ChessVar"""
    def __init__(self) -> None:
        """Creates a board with all the pieces in their starting positions"""
        self._pieces = {
            "black rook a" : Rook("black"),
            "black knight b" : Knight("black"),
            "black bishop c" : Bishop("black"),
            "black queen" : Queen("black"),
            "black king" : King("black"),
            "black bishop f": Bishop("black"),
            "black knight g": Knight("black"),
            "black rook h": Rook("black"),
            "black pawn a": Pawn("black"),
            "black pawn b": Pawn("black"),
            "black pawn c": Pawn("black"),
            "black pawn d": Pawn("black"),
            "black pawn e": Pawn("black"),
            "black pawn f": Pawn("black"),
            "black pawn g": Pawn("black"),
            "black pawn h": Pawn("black"),
            "black falcon": Falcon("black"),
            "black hunter": Hunter("black"),
            "white rook a" : Rook("white"),
            "white knight b" : Knight("white"),
            "white bishop c" : Bishop("white"),
            "white queen" : Queen("white"),
            "white king" : King("white"),
            "white bishop f": Bishop("white"),
            "white knight g": Knight("white"),
            "white rook h": Rook("white"),
            "white pawn a": Pawn("white"),
            "white pawn b": Pawn("white"),
            "white pawn c": Pawn("white"),
            "white pawn d": Pawn("white"),
            "white pawn e": Pawn("white"),
            "white pawn f": Pawn("white"),
            "white pawn g": Pawn("white"),
            "white pawn h": Pawn("white"),
            "white falcon": Falcon("white"),
            "white hunter": Hunter("white"),
            "empty": EmptySquare(),
        }
        self._board = [
            [self._pieces["black rook a"], self._pieces["black knight b"], self._pieces["black bishop c"], self._pieces["black queen"], self._pieces["black king"], self._pieces["black bishop f"], self._pieces["black knight g"], self._pieces["black rook h"]],
            [self._pieces["black pawn a"], self._pieces["black pawn b"], self._pieces["black pawn c"], self._pieces["black pawn d"], self._pieces["black pawn e"], self._pieces["black pawn f"], self._pieces["black pawn g"], self._pieces["black pawn h"], ],
            [self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], ],
            [self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], ],
            [self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], ],
            [self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], self._pieces["empty"], ],
            [self._pieces["white pawn a"], self._pieces["white pawn b"], self._pieces["white pawn c"], self._pieces["white pawn d"], self._pieces["white pawn e"], self._pieces["white pawn f"], self._pieces["white pawn g"], self._pieces["white pawn h"], ],
            [self._pieces["white rook a"], self._pieces["white knight b"], self._pieces["white bishop c"], self._pieces["white queen"], self._pieces["white king"], self._pieces["white bishop f"], self._pieces["white knight g"], self._pieces["white rook h"]],
        ]
        
        self._avail_fairy_pieces = {
            "f" : self._pieces["black falcon"],
            "h" : self._pieces["black hunter"],
            "F" : self._pieces["white falcon"],
            "H" : self._pieces["white hunter"],
        }

    def show_board(self):
        """Prints current board state to terminal"""
        for row in self._board:
            for square in row:
                print(square.get_symbol(), end=" ")
            print()

    def get_piece_object(self, piece_name):
        """Returns the object with the provided name"""
        return self._pieces[piece_name]
    
    def get_fairy_piece_object(self, fairy_piece_name):
        """Returns the fairy piece with the provided fairy name: white falcon 'F', white hunter 'H', black falcon 'f', black hunter 'h'"""
        return self._avail_fairy_pieces.get(fairy_piece_name)

    def get_max_index(self):
        """Returns the max index of the board (assumes that board is square with equal number of rows and columns"""
        return len(self._board) - 1
    
    def get_piece_at_coord(self, column:int, row: int):
        """Returns the object at the given column and row indices"""
        return self._board[row][column]
    
    def is_piece_in_play(self, piece_name) -> bool:
        """Returns whether the piece corresponding to the inputted piece name appears on the board"""
        for row in self._board:
            if self._pieces[piece_name] in row:
                return True
        return False
    
    def move_piece(self, origin_column:int, origin_row:int, destination_column:int, destination_row: int):
        """Moves Piece from origin square to destination square"""
        self._board[destination_row][destination_column] = self._board[origin_row][origin_column]
        self._board[origin_row][origin_column] = self._pieces["empty"]

    def is_on_board(self, column:int, row: int) -> bool:
        """Returns whether the inputted coordinates are within the bounds of the chess board"""
        min_index = 0
        max_index = self.get_max_index()
        return (column >= min_index and column <= max_index) and (row >= min_index and row <= max_index)
    
    def is_empty(self, column:int, row: int) -> bool:
        """Returns whether the square is empty"""
        return self._board[row][column] == self._pieces["empty"]
    
    def count_major_pieces(self, color:str) -> int:
        """Counts the number of rooks, knights, bishops, and queen the color has in play"""
        major_pieces_in_play = 0
        black_major_pieces = [
            "black rook a",
            "black knight b",
            "black bishop c",
            "black queen",
            'black bishop f',
            "black knight g",
            "black rook h"
        ]
        white_major_pieces = [
            "white rook a",
            "white knight b",
            "white bishop c",
            "white queen",
            "white bishop f",
            "white knight g",
            "white rook h",
        ]
        if color == "black":
            for piece in black_major_pieces:
                if self.is_piece_in_play(piece):
                    major_pieces_in_play += 1
        else:
            for piece in white_major_pieces:
                if self.is_piece_in_play(piece):
                    major_pieces_in_play += 1

        return major_pieces_in_play
    
    def count_fairy_pieces(self, color:str) -> int:
        """Counts the number of fairy pieces the color has in play"""
        fairy_pieces_in_play = 0
        black_fairy_pieces = [
            "black falcon",
            "black hunter",
        ]
        white_fairy_pieces = [
            "white falcon",
            "white hunter",
        ]
        if color == "black":
            for piece in black_fairy_pieces:
                if self.is_piece_in_play(piece):
                    fairy_pieces_in_play += 1
        else:
            for piece in white_fairy_pieces:
                if self.is_piece_in_play(piece):
                    fairy_pieces_in_play += 1

        return fairy_pieces_in_play
    
    def place_fairy_piece(self, fairy_piece_name, destination_column:int, destination_row:int):
        """Removes the placed fairy piece from the list of available fairy pieces and places fairy piece at the destination"""
        object = self._avail_fairy_pieces[fairy_piece_name]
        self._board[destination_row][destination_column] = object
        del self._avail_fairy_pieces[fairy_piece_name]


class EmptySquare:
    """Represents an empty square on the board"""
    def __init__(self) -> None:
        self._color = None

    def get_symbol(self) -> str:
        """Returns the symbol used to print the board graphic"""
        return '\u2610'

    def get_color(self):
        """Returns the color of the empty square (aka none)"""
        return self._color

class Piece:
    """Represents a chess piece"""
    def __init__(self, color:str) -> None:
        self._color = color  

    def get_color(self):
        """Returns piece color"""
        return self._color
    
    def on_move(self):
        """Implements any side effects after a piece's valid move"""
        pass

    def get_symbol(self):
        """Returns the symbol used when printing the board graphic"""
        pass

    def move(self, origin_column, origin_row, squares_moved_forwards_backwards, squares_moved_left_right):
        """Returns coordinates if piece moved forward, depending on the piece color
        Forward = positive squares moved (forward backwards)
        Backwards = negative squares moved (forward backwards)
        Left = negative squares moved (left right)
        Right = positive squares moved (left right)"""
        if self._color == "black":
            destination_row = origin_row + squares_moved_forwards_backwards
        else:
            destination_row = origin_row - squares_moved_forwards_backwards
        destination_column = origin_column + squares_moved_left_right
        return destination_column, destination_row
    
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        pass

class Pawn(Piece):
    """Represents a pawn chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self._moves_made = 0
    
    def on_move(self):
        """Increment's the piece's moves by 1"""
        self._moves_made += 1

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265F'
        else:
            return '\u2659'
        
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []        
        # Check Pawn moving forward 1 square
        trial_column_forward1, trial_row_forward1 = self.move(origin_column, origin_row, 1, 0)
        # The move is valid if the move doesn't take it off the board, and the spot is empty
        if board.is_on_board(trial_column_forward1, trial_row_forward1) and board.is_empty(trial_column_forward1, trial_row_forward1):
            valid_destinations.append( (trial_column_forward1, trial_row_forward1) )
            # if Pawn is not blocked and it's on its starting rank it has the option of moving two squares in one turn
            trial_column, trial_row = self.move(origin_column, origin_row, 2, 0)
            # The move is valid if the Pawn hasn't moved yet, the move doesn't take it off the board, and the spot is empty
            if self._moves_made == 0 and board.is_on_board(trial_column, trial_row) and board.is_empty(trial_column, trial_row):
                valid_destinations.append( (trial_column, trial_row) )
        
        # Check if there are any pieces to capture diagonally
        trial_column_diagleft, trial_row_diagleft = self.move(trial_column_forward1, trial_row_forward1, 0, -1)
        # The move is valid if the move is on the board and the spot is occupied by the opposite color
        if board.is_on_board(trial_column_diagleft, trial_row_diagleft) and board.get_piece_at_coord(trial_column_diagleft, trial_row_diagleft).get_color() != self._color and not board.is_empty(trial_column_diagleft, trial_row_diagleft):
            valid_destinations.append( (trial_column_diagleft, trial_row_diagleft) )
        # Similarly for the other diagonal direction
        trial_column_diagright, trial_row_diagright = self.move(trial_column_forward1, trial_row_forward1, 0, 1)
        if board.is_on_board(trial_column_diagright, trial_row_diagright) and board.get_piece_at_coord(trial_column_diagright, trial_row_diagright).get_color() != self._color and not board.is_empty(trial_column_diagright, trial_row_diagright):
            valid_destinations.append( (trial_column_diagright, trial_row_diagright) )

        return valid_destinations

class Knight(Piece):
    """Represents a knight chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265E'
        else:
            return '\u2658'
        
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (2, -1),
            (2, 1),
            (-2, -1),
            (-2, 1),
            (1, -2),
            (1, 2),
            (-1, -2),
            (-1, 2),
        ]

        for (row_offset, column_offset) in possible_moves:
            trial_column, trial_row = self.move(origin_column, origin_row, row_offset, column_offset)
            if board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
        
        return valid_destinations

class Bishop(Piece):
    """Represents a bishop chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)
    
    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265D'
        else:
            return '\u2657'
            
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (1,1),
            (1,-1),
            (-1,-1),
            (-1,1),
        ]

        for (row_offset, column_offset) in possible_moves:
            column_counter = column_offset
            row_counter = row_offset
            trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)
            while board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
                if board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color and not board.is_empty(trial_column, trial_row):
                    break
                column_counter += column_offset
                row_counter += row_offset
                trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)

        return valid_destinations

class Rook(Piece):
    """Represents a rook chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265C'
        else:
            return '\u2656'
                
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]
        
        for (row_offset, column_offset) in possible_moves:
            column_counter = column_offset
            row_counter = row_offset
            trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)
            while board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
                if board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color and not board.is_empty(trial_column, trial_row):
                    break
                column_counter += column_offset
                row_counter += row_offset
                trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)

        return valid_destinations


class Queen(Piece):
    """Represents a queen chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)
    
    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265B'
        else:
            return '\u2655'
                
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (1,-1),
            (-1,-1),
            (-1,1),
        ]
        
        for (row_offset, column_offset) in possible_moves:
            column_counter = column_offset
            row_counter = row_offset
            trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)
            while board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
                if board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color and not board.is_empty(trial_column, trial_row):
                    break
                column_counter += column_offset
                row_counter += row_offset
                trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)

        return valid_destinations

class King(Piece):
    """Represents a king chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u265A'
        else:
            return '\u2654'
                
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (1,-1),
            (-1,-1),
            (-1,1),
        ]

        for (row_offset, column_offset) in possible_moves:
            trial_column, trial_row = self.move(origin_column, origin_row, row_offset, column_offset)
            if board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )

        return valid_destinations


class Falcon(Piece):
    """Represents a falcon chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u2666'
        else:
            return '\u2662'
                
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (1,1),
            (1,-1),
            (-1,0),
        ]
        
        for (row_offset, column_offset) in possible_moves:
            column_counter = column_offset
            row_counter = row_offset
            trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)
            while board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
                if board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color and not board.is_empty(trial_column, trial_row):
                    break
                column_counter += column_offset
                row_counter += row_offset
                trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)

        return valid_destinations

class Hunter(Piece):
    """Represents a hunter chess piece
    Inherits from Piece"""
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def get_symbol(self) -> str:
        """Returns the piece's unicode"""
        if self.get_color() == "black":
            return '\u2617'
        else:
            return '\u2616'
                
    def get_valid_destinations(self, origin_column:int, origin_row:int, board):
        """Returns a list of tuples, where each tuple is a valid coordinate for a destination square"""
        valid_destinations = []
        possible_moves = [
            (1,0),
            (-1,-1),
            (-1,1),
        ]
        
        for (row_offset, column_offset) in possible_moves:
            column_counter = column_offset
            row_counter = row_offset
            trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)
            while board.is_on_board(trial_column, trial_row) and board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color:
                valid_destinations.append( (trial_column, trial_row) )
                if board.get_piece_at_coord(trial_column, trial_row).get_color() != self._color and not board.is_empty(trial_column, trial_row):
                    break
                column_counter += column_offset
                row_counter += row_offset
                trial_column, trial_row = self.move(origin_column, origin_row, row_counter, column_counter)

        return valid_destinations

class ChessVar:
    """Represents a game of chess to be played
    Pieces are represented by Piece objects
    The board and the positions of the pieces are represented by a Board object"""
    def __init__(self) -> None:
        """Initializes an unfinished chess game with a board, with white moving first"""
        self._game_state = "UNFINISHED"
        self._board = Board()
        self._turns = 0
        self._current_turn = "white"
        self._column_to_index = {
            "a" : 0,
            "b" : 1,
            "c" : 2,
            "d" : 3,
            "e" : 4,
            "f" : 5,
            "g" : 6,
            "h" : 7, 
        }

    def get_game_state(self) -> str:
        """Returns the current game state ('UNFINISHED', 'WHITE_WON', 'BLACK_WON')"""
        return self._game_state
    
    def _translate_string_to_index(self, input:str) -> tuple:
        """Takes a user input string in the format and converts it into column and row indices 
        for the game board (e.g. 'g7' becomes (6,1) where (0,0) is the top left square of the board)"""
        column, row = [*input]
        column = self._column_to_index[column]
        row = self._board.get_max_index() +1 - int(row)
        return column, row
    
    def _advance_turn(self):
        """Increments the current turn count and updates whose turn it is"""
        self._turns += 1
        if self._turns % 2 == 0:
            self._current_turn = "white"
        else:
            self._current_turn = "black"

    def _origin_or_destination_are_invalid(self, origin_column:int, origin_row:int, destination_column:int, destination_row: int) -> bool:
        """Returns True if either origin or destination coordinates aren't on the board, false otherwise"""
        return (not self._board.is_on_board(origin_column,origin_row)) or (not self._board.is_on_board(destination_column, destination_row))
    
    def _game_state_is_finished(self) -> bool:
        """Returns True if game state is not "UNFINISHED", False otherwise"""
        return self._game_state != "UNFINISHED"
    
    def _origin_piece_cant_move(self, origin_column:int, origin_row:int) -> bool:
        """Returns True if piece at origin coordinate can't move this turn or is empty, False otherwise"""
        return self._board.get_piece_at_coord(origin_column, origin_row).get_color() != self._current_turn

    def make_move(self, origin:str, destination:str) -> bool:
        """Checks if move is valid. If not valid, returns False
        If yes, it makes the move, removes any captured piece, updates game state if necesssary, updates whose turn it is,
        then returns true."""
        # If game is already won
        if self._game_state_is_finished():
            return False
        
        origin_column, origin_row = self._translate_string_to_index(origin)
        destination_column, destination_row = self._translate_string_to_index(destination)

        # If origin or destination is outside of board
        if self._origin_or_destination_are_invalid(origin_column, origin_row, destination_column, destination_row):
            return False
        # If origin square is empty or it's not this piece's turn:
        if self._origin_piece_cant_move(origin_column, origin_row):
            return False
        
        valid_destinations = self._board.get_piece_at_coord(origin_column, origin_row).get_valid_destinations(origin_column, origin_row, self._board)

        destination_coord = (destination_column, destination_row)
        if destination_coord not in valid_destinations:
            return False

        # Move is valid, so do any "on move" piece side effects and then move the piece
        self._board.get_piece_at_coord(origin_column, origin_row).on_move()
        self._board.move_piece(origin_column, origin_row, destination_column, destination_row)

        # After move is made, checks if the kings are still in play. If not, updates game state
        if not self._board.is_piece_in_play("white king"):
            self._game_state = "BLACK_WON"
        if not self._board.is_piece_in_play("black king"):
            self._game_state = "WHITE_WON"

        # If the move made was valid and the game is not over, prepare to advance turn
        if self._game_state == "UNFINISHED":
            self._advance_turn()
        return True

    def enter_fairy_piece(self, fairy_piece_name: str, destination: str) -> bool:
        """Returns false if the fairy piece is not allowed to enter at this destination coordinate
        Otherwise it places the fairy piece at the given location, update whose turn it is, and returns true"""
        # If game is already won
        if self._game_state_is_finished():
            return False
        
        fairy_piece = self._board.get_fairy_piece_object(fairy_piece_name)
        destination_column, destination_row = self._translate_string_to_index(destination)
        
        # If the fairy piece name is invalid aka not F, H, f, or h or already in play:
        if fairy_piece is None:
            return False
        
        # If the fairy piece's color is not this turn's color:
        if fairy_piece.get_color() != self._current_turn:
            return False

        # Sets home row value based on piece color
        if fairy_piece.get_color() == "black":
            home_rows = [0,1]
        else:
            home_rows = [6,7]
        
        # If destination square is not in home rows, not on board, or not empty:
        if destination_row not in home_rows or not self._board.is_on_board(destination_column, destination_row) or not self._board.is_empty(destination_column,destination_row):
            return False

        # Checks if the number of major pieces and the number of fairy pieces on the board to see if it's valid to enter a fairy piece
        if self._board.count_major_pieces(self._current_turn) == 7:
            return False
        if self._board.count_major_pieces(self._current_turn) == 6 and self._board.count_fairy_pieces(self._current_turn) == 1:
            return False
        if self._board.count_major_pieces(self._current_turn) < 6 and self._board.count_fairy_pieces(self._current_turn) == 2:
            return False

        # If the move made was valid, remove fairy piece from available fairy places, place fairy piece at destination, and advance turn

        self._board.place_fairy_piece(fairy_piece_name, destination_column, destination_row)
        self._advance_turn()
        return True

    def show_board(self):
        """Prints current board state to the terminal"""
        return self._board.show_board()

# def main():
#     """Used for testing"""
#     game = ChessVar()
#     game._board.move_piece(2, 7, 2, 0)
#     game._board.move_piece(7,0, 7,7)
#     print(game.get_game_state())
#     print(game._current_turn)
#     game.enter_fairy_piece("F", "c1")
#     game.enter_fairy_piece("h", "h8")
#     game._board.move_piece(2,7, 2,4)
#     game._current_turn = "white"
#     game.enter_fairy_piece("F", "c1") == False
#     game.show_board()

# if __name__ == '__main__':
#     main()