"""
    There is 4 types of pieces:
        - 1 empty square
        - 1 black pawn
        - 1 white pawn
        - 1 white king
"""
NB_TYPE_PIECES = 4

ES = 0 # empty square
BP = 1 # black pawn
WP = 2 # white pawn
WK = 3 # white king



DIMENSION = 7

ARD_RI_DISPOSITION = [
                        [ES, ES, BP, BP, BP, ES, ES],
                        [ES, ES, ES, BP, ES, ES, ES],
                        [BP, ES, WP, WP, WP, ES, BP],
                        [BP, BP, WP, WK, WP, BP, BP],
                        [BP, ES, WP, WP, WP, ES, BP],
                        [ES, ES, ES, BP, ES, ES, ES],
                        [ES, ES, BP, BP, BP, ES, ES]
                    ]

