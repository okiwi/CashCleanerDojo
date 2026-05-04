
class Grid:

    _DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self):
        self.grid = [["_" for i in range(8)] for j in range(8)]
        self.SetCell("D4", "W")
        self.SetCell("E5", "W")
        self.SetCell("D5", "B")
        self.SetCell("E4", "B")

    def __str__(self):
        output = "\n  A B C D E F G H\n"
        for i in range(8):
            output += str(i+1) + " " + " ".join(self.grid[i]) + "\n"
        return output

    def _CheckCoordinate(self, coordinate):
        if len(coordinate) != 2:
            return False
        
        if coordinate[0] < 'A' or coordinate[0] > 'H':
            return False

        if coordinate[1] < '1' or coordinate[1] > '8':
            return False

        return True
    
    def _TranslateCoordinate(self, row, column):
        return chr(ord('A') + column) + str(row + 1)

    def GetCell(self, coordinate):
        if not self._CheckCoordinate(coordinate):
            return None
        
        row = int(coordinate[1]) - 1
        col = ord(coordinate[0]) - ord('A')
        return self.grid[row][col]
    
    def SetCell(self, coordinate, value):
        if not self._CheckCoordinate(coordinate):
            return False

        row = int(coordinate[1]) - 1
        col = ord(coordinate[0]) - ord('A')
        self.grid[row][col] = value
        return True
    
    def _clearValidPlacements(self):
        for row in range(8):
            for column in range(8):
                if self.grid[row][column] == "O":
                    self.grid[row][column] = "_"
    
    def computeValidPlacements(self, player):
        self._clearValidPlacements()
        for row in range(8):
            for column in range(8):
                coordinate = self._TranslateCoordinate(row, column)
                if (self.GetCell(coordinate) != player):
                    continue
                for dr, dc in self._DIRECTIONS:
                    candidate = self._CheckAxis(coordinate, player, dr, dc)
                    if candidate is not None:
                        self.SetCell(candidate, "O")


    def _CheckAxis(self, coordinate, player, rowDirection, columnDirection):
        opponent = "B" if player == "W" else "W"
        row = int(coordinate[1]) - 1
        col = ord(coordinate[0]) - ord('A')
        foundOpponent = False

        while True:
            row += rowDirection
            col += columnDirection
            if row < 0 or row >= 8 or col < 0 or col >= 8:
                return None
            cellValue = self.grid[row][col]
            if cellValue == opponent:
                foundOpponent = True
            elif cellValue == "_" and foundOpponent:
                return self._TranslateCoordinate(row, col)
            else:
                return None
            
    def ReversePieces(self, coordinate, player):
        for dr, dc in self._DIRECTIONS:
            self._ReverseAxis(coordinate, player, dr, dc)

    def _ReverseAxis(self, coordinate, player, rowDirection, columnDirection):
        opponent = "B" if player == "W" else "W"
        row = int(coordinate[1]) - 1
        col = ord(coordinate[0]) - ord('A')
        cellsToReverse = []

        while True:
            row += rowDirection
            col += columnDirection
            if row < 0 or row >= 8 or col < 0 or col >= 8:
                return
            cellValue = self.grid[row][col]
            if cellValue == opponent:
                cellsToReverse.append((row, col))
            elif cellValue == player :
                for r, c in cellsToReverse:
                    self.grid[r][c] = player
                return
            else:
                return

class Game:
    def __init__(self):
        self.grid = Grid()
        self.nextPlayer = "W"
        self.grid.computeValidPlacements(self.nextPlayer)
        self.Print()

    def Play(self, coordinate):
        if self.grid.GetCell(coordinate) != "O":
            return False
        if self.grid.SetCell(coordinate, self.nextPlayer):
            self.grid.ReversePieces(coordinate, self.nextPlayer)
            self.endTurn()
            return True
        return False
    
    def Print(self):
        print(self.nextPlayer)
        print(self.grid)
    
    def endTurn(self):
        if self.nextPlayer == "W":
            self.nextPlayer = "B"
        else:
            self.nextPlayer = "W"
        self.grid.computeValidPlacements(self.nextPlayer)
        self.Print()


def test_NewGrid():
    # Arrange

    # Act
    grid = Grid()

    # Assert
    assert (grid.GetCell("D4") == "W")
    assert (grid.GetCell("D5") == "B")
    assert (grid.GetCell("E5") == "W")
    assert (grid.GetCell("E4") == "B")

def test_GetCell():
    # Arrange
    grid = Grid()
    grid.SetCell("A1", "X")
    grid.SetCell("H8", "O")

    # Act
    cellA1 = grid.GetCell("A1")
    cellH8 = grid.GetCell("H8")

    # Assert
    assert (cellA1 == "X")
    assert (cellH8 == "O")

   
def test_GetCell_InvalidCoordinate_None():
    # Arrange
    grid = Grid()

    # Act
    cellA0 = grid.GetCell("A0")
    cellFF = grid.GetCell("FF")
    cellWhiteSpace = grid.GetCell("  ")
    cellA = grid.GetCell("A")
    cellEmpty = grid.GetCell("")

    # Assert
    assert (cellA0 is None)
    assert (cellFF is None)
    assert (cellWhiteSpace is None)
    assert (cellA is None)
    assert (cellEmpty is None)

def test_SetCell_InvalidCoordinate_False():
    # Arrange
    grid = Grid()

    # Act
    cellA0 = grid.SetCell("A0", "X")
    cellFF = grid.SetCell("FF", "X")
    cellWhiteSpace = grid.SetCell("  ", "X")
    cellA = grid.SetCell("A", "X")
    cellEmpty = grid.SetCell("", "X")

    # Assert
    assert (cellA0 is False)
    assert (cellFF is False)
    assert (cellWhiteSpace is False)
    assert (cellA is False)
    assert (cellEmpty is False)

def test_PrintGrid():
    # Arrange
    expectedGridOutput = """
  A B C D E F G H
1 _ _ _ _ _ _ _ _
2 _ _ _ _ _ _ _ _
3 _ _ _ _ _ _ _ _
4 _ _ _ W B _ _ _
5 _ _ _ B W _ _ _
6 _ _ _ _ _ _ _ _
7 _ _ _ _ _ _ _ _
8 _ _ _ _ _ _ _ _
"""
    grid = Grid()

    # Act
    assert (str(grid) == expectedGridOutput)

def test_ValidPlacement():
    # Arrange
    game = Game()

    # Act
    assert(game.Play("D4") is False)
    assert(game.Play("C5") is True)

def test_WholeGame():
    game = Game()

    assert(game.Play("D6") is True)

    assert(game.Play("C5") is False)
    assert(game.Play("C6") is True)