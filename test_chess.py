import pytest
from ChessVar import (
    EmptySquare, Piece, Pawn, Knight, Bishop, 
    Rook, Queen, King, Falcon, Hunter, Board, ChessVar
)

@pytest.fixture
def board():
    return Board()

class TestPiece:
    def test_color(self, board):
        assert board._pieces["black rook a"].get_color() == "black"
        assert board._pieces["empty"].get_color() == None
        assert board._pieces["white falcon"].get_color() == "white"

    def test_pawn(self, board):
        assert board._pieces["black pawn a"]._moves_made == 0
        board._pieces["black pawn a"].on_move()
        assert board._pieces["black pawn a"]._moves_made == 1

    def test_black_pawn_valid_destinations(self, board):
        pawn_valid_destinations = board._pieces["black pawn a"].get_valid_destinations(0,1,board)
        assert pawn_valid_destinations == [ (0,2), (0,3)]
        board._pieces["black pawn a"].on_move()
        pawn_valid_destinations = board._pieces["black pawn a"].get_valid_destinations(0,1,board)
        assert pawn_valid_destinations == [(0,2)]

        board.move_piece(1, 6, 1, 2)
        pawn_valid_destinations = board._pieces["black pawn a"].get_valid_destinations(0,1,board)
        assert pawn_valid_destinations == [(0,2), (1,2)]
        pawn_valid_destinations = board._pieces["black pawn b"].get_valid_destinations(1,1,board)
        assert pawn_valid_destinations == []
        pawn_valid_destinations = board._pieces["white pawn b"].get_valid_destinations(1,2, board)
        assert pawn_valid_destinations == [(0,1), (2,1)]

        board.move_piece(3, 6, 3, 2)
        pawn_valid_destinations = board._pieces["black pawn c"].get_valid_destinations(2,1,board)
        assert pawn_valid_destinations == [(2,2), (2,3), (1,2), (3,2)]

        board.move_piece(2, 6, 2, 3)
        pawn_valid_destinations = board._pieces["black pawn c"].get_valid_destinations(2,1,board)
        assert pawn_valid_destinations == [(2,2), (1,2), (3,2)]

    def test_white_pawn_valid_destinations(self, board):
        pawn_valid_destinations = board._pieces["white pawn c"].get_valid_destinations(2, 6,board)
        assert pawn_valid_destinations == [(2, 5), (2,4)]

    def test_black_knight_valid_destinations(self,board):
        knight_valid_destinations = board._pieces["black knight b"].get_valid_destinations(1,0,board)
        assert knight_valid_destinations == [(0,2), (2,2)]

        board.move_piece(1,0, 1,4)
        knight_valid_destinations = board._pieces["black knight b"].get_valid_destinations(1,4,board)
        assert knight_valid_destinations == [(0,6),(2,6),(0,2), (2,2), (3,5), (3, 3)]

    def test_white_knight_valid_destinations(self, board):
        knight_valid_destinations = board._pieces["white knight g"].get_valid_destinations(6,7,board)
        assert knight_valid_destinations == [(5, 5), (7,5)]

        board.move_piece(6,7, 6,3)
        knight_valid_destinations = board._pieces["white knight g"].get_valid_destinations(6,3,board)
        assert knight_valid_destinations == [(5, 1), (7,1), (5,5), (7,5), (4,2),(4,4)]

    def test_black_bishop_valid_destinations(self, board):
        bishop_valid_destinations = board._pieces["black bishop c"].get_valid_destinations(2,0, board)
        assert bishop_valid_destinations == []

        board.move_piece(2,0,2,3)
        bishop_valid_destinations = board._pieces["black bishop c"].get_valid_destinations(2,3, board)
        assert bishop_valid_destinations == [(3, 4), (4,5), (5,6), (1,4), (0, 5), (1,2), (3,2)]

    def test_white_bishop_valid_destinations(self, board):
        bishop_valid_destinations = board._pieces["white bishop c"].get_valid_destinations(2,7, board)
        assert bishop_valid_destinations == []

        board.move_piece(2,7,2,4)
        bishop_valid_destinations = board._pieces["white bishop c"].get_valid_destinations(2,4, board)
        assert bishop_valid_destinations == [(3, 3), (4,2), (5,1), (1,3), (0,2), (1,5), (3,5)]

    def test_black_rook_valid_destinations(self, board):
        rook_valid_destinations = board._pieces["black rook a"].get_valid_destinations(0,0, board)
        assert rook_valid_destinations == []

        board.move_piece(0,0,2,4)
        rook_valid_destinations = board._pieces["black rook a"].get_valid_destinations(2,4, board)
        assert rook_valid_destinations == [(3,4), (4,4), (5,4), (6,4), (7,4), (1,4),(0,4), (2,5), (2,6),(2,3),(2,2)]

    def test_white_rook_valid_destinations(self, board):
        rook_valid_destinations = board._pieces["white rook h"].get_valid_destinations(7,7, board)
        assert rook_valid_destinations == []

        board.move_piece(7,7,7,4)
        rook_valid_destinations = board._pieces["white rook h"].get_valid_destinations(7,4, board)
        assert rook_valid_destinations == [(6,4), (5,4), (4,4), (3,4), (2,4), (1,4), (0,4), (7, 3), (7,2), (7,1), (7, 5)]

    def test_black_queen_valid_destination(self, board):
        queen_valid_destinations = board._pieces["black queen"].get_valid_destinations(3, 0, board)
        assert queen_valid_destinations == []

        board.move_piece(3,0, 2,4)
        queen_valid_destinations = board._pieces["black queen"].get_valid_destinations(2, 4, board)
        assert queen_valid_destinations == [(3,4), (4,4), (5,4), (6,4), (7,4), (1,4),(0,4), (2,5), (2,6),(2,3),(2,2), (3, 5), (4,6), (1,5), (0, 6), (1,3), (0, 2), (3,3), (4,2)]

    def test_black_king_valid_destinations(self, board):
        king_valid_destinations = board._pieces["black king"].get_valid_destinations(4,0, board)
        assert king_valid_destinations == []

        board.move_piece(4,0, 4,5)
        king_valid_destinations = board._pieces["black king"].get_valid_destinations(4,5, board)
        assert king_valid_destinations == [(5,5), (3,5), (4,6), (4,4), (5,6), (3,6),(3,4), (5,4)]

class TestBoard:
    def test_get_piece_object(self, board):
        assert board.get_piece_object("white pawn a") == board._pieces["white pawn a"]

    def test_max(self, board):
        assert board.get_max_index() == 7
    
    def test_get_piece(self, board):
        assert board.get_piece_at_coord(0,0) == board._pieces["black rook a"]
        assert board.get_piece_at_coord(0,4) == board._pieces["empty"]

    def test_get_fairy_piece(self, board):
        assert board.get_fairy_piece_object("F") == board._pieces["white falcon"]
        assert board.get_fairy_piece_object("H") == board._pieces["white hunter"]
        assert board.get_fairy_piece_object("f") == board._pieces["black falcon"]
        assert board.get_fairy_piece_object("h") == board._pieces["black hunter"]
    
    def test_is_piece_in_play(self, board):
        assert board.is_piece_in_play("white falcon") == False
        assert board.is_piece_in_play("black king") == True
  
    def test_move_piece(self, board):
        board.move_piece(0,0,0,6)
        assert board.get_piece_at_coord(0,0) == board._pieces["empty"]
        assert board.get_piece_at_coord(0,6) == board._pieces["black rook a"]
        assert board.is_piece_in_play("white pawn a") == False
    
    def test_is_on_board(self, board):
        assert board.is_on_board(0,0) == True
        assert board.is_on_board(1,1) == True
        assert board.is_on_board(7,0) == True
        assert board.is_on_board(7,7) == True
        assert board.is_on_board(0,7) == True

        assert board.is_on_board(-1,0) == False
        assert board.is_on_board(8,0) == False
        assert board.is_on_board(8,8) == False
        assert board.is_on_board(0,8) == False
    
    def test_is_empty(self, board):
        assert board.is_empty(0,0) == False
        assert board.is_empty(3,3) == True

    def test_count_pieces(self,board):
        assert board.count_major_pieces("black") == 7
        assert board.count_major_pieces("white") == 7
        assert board.count_fairy_pieces("black") == 0
        assert board.count_fairy_pieces("white") == 0

    def test_falcon(self,board):
        board.place_fairy_piece("F", 2,4)
        assert board._avail_fairy_pieces == {
            "f" : board._pieces["black falcon"],
            "h" : board._pieces["black hunter"],
            "H" : board._pieces["white hunter"],
        }
        falcon_valid_destinations = board._pieces["white falcon"].get_valid_destinations(2,4, board)
        assert falcon_valid_destinations == [(3,3), (4,2), (5,1), (1,3), (0,2), (2,5)]

    def test_hunter(self,board):
        board.place_fairy_piece("h", 2,4)
        assert board._avail_fairy_pieces == {
            "f" : board._pieces["black falcon"],
            "F" : board._pieces["white falcon"],
            "H" : board._pieces["white hunter"],
        }
        falcon_valid_destinations = board._pieces["black hunter"].get_valid_destinations(2,4, board)
        assert falcon_valid_destinations == [(2,5), (2,6), (1,3), (0,2), (3,3), (4,2)]

class TestChessVar:
    @pytest.fixture
    def game(self):
        return ChessVar()
    
    def test_translate_string_to_index(self, game):
        assert game._translate_string_to_index("c1") == (2,7)

    def test_advance_turn(self, game):
        game._advance_turn()
        assert game._turns == 1
        assert game._current_turn == "black"
    
    def test_origin_or_destination_are_invalid(self,game):
        assert game._origin_or_destination_are_invalid(0,0,1,1) == False
        assert game._origin_or_destination_are_invalid(0,0,8,1) == True
        assert game._origin_or_destination_are_invalid(-1,0,1,1) == True
        assert game._origin_or_destination_are_invalid(0,8,1,9) == True

    def test_game_state_is_finished(self, game):
        assert game._game_state_is_finished() == False
        game._game_state = "BLACK_WON"
        assert game._game_state_is_finished() == True

    def test_origin_piece_cant_move(self, game):
        assert game._origin_piece_cant_move(0,0) == True
        assert game._origin_piece_cant_move(7,7) == False
        game._advance_turn()
        assert game._origin_piece_cant_move(7,7) == True
        assert game._origin_piece_cant_move(0,0) == False

    def test_enter_fairy_piece(self, game):
        assert game.enter_fairy_piece("f", "g2") == False
        assert game.enter_fairy_piece("F", "c2") == False
        assert game._board.count_fairy_pieces("black") == 0
        assert game._board.count_fairy_pieces("white") == 0
        assert game._board._avail_fairy_pieces == {
            "f" : game._board._pieces["black falcon"],
            "h" : game._board._pieces["black hunter"],
            "F" : game._board._pieces["white falcon"],
            "H" : game._board._pieces["white hunter"],
        }

        game._board.move_piece(2, 7, 2, 0)
        game._board.move_piece(7,0, 7,7)
        assert game.enter_fairy_piece("h", "h8") == False
        assert game.enter_fairy_piece("F", "h8") == False
        assert game.enter_fairy_piece("F", "c1") == True
        assert game._current_turn == "black"
        assert game._board.count_fairy_pieces("black") == 0
        assert game._board.count_fairy_pieces("white") == 1
        assert game._board._avail_fairy_pieces == {
            "f" : game._board._pieces["black falcon"],
            "h" : game._board._pieces["black hunter"],
            "H" : game._board._pieces["white hunter"],
        }


