from curses.ascii import isdigit

class Player:



    def __init__(self):

        self.name = "player"
        self.symbol = "X"
    def set_name(self):
        nm = input("Enter your name:")
        self.name = nm
    def set_symbol(self):
        while True:
            sym = (input("choose your symbol:")).upper()
            if sym.isalpha():
                self.symbol = sym
                break
            print("Symbols are one letter")

class Menu:
    def startMenu(self):
        print("Welcome to THE BEST X-O game ever!!")
        while True:

            choice = int(input("1-START GAME \n2-QUIT GAME\nEnter choice number:"))
            if choice == 1 or choice == 2:
                break
            print("choose 1 or 2")
        return choice
    def endMenu(self):
        print("GAME OVER!!")
        while True:
            choice = int(input("1-RESTART GAME \n2-QUIT GAME\nEnter choice number:"))
            if choice == 1 or choice == 2:
                break
            print("choose 1 or 2")
        return choice

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]

    def desplayBoard(self):
        board = self.board
        print("GAME:")
        print(f"{board[0]}|{board[1]}|{board[2]}\n_____\n{board[3]}|{board[4]}|{board[5]}\n_____\n{board[6]}|{board[7]}|{board[8]}")

    def updateBoard(self,symbol):
        pos = int(input("choose number of box: "))
        if self.board[pos - 1].isdigit() and  1<=pos<=9:
            self.board[pos - 1] = symbol
            return True
        else:
            return False

    def resetBoard(self):
        self.board = [str(i) for i in range(1,10)]

class Game:
    #board player minu
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.turn = 0

    def startGame(self):
        choice = Menu.startMenu(self)
        if choice == 1:
            self.setPlayer()
            self.playGame()
        elif choice == 2:
            print("See you later!!")
            exit()

    def playGame(self):
        while True:
            self.turnPlay()
            if self.drawGame() or self.winGame():
                choice = self.menu.endMenu()
                self.board.resetBoard()
                if choice == 1:
                    self.turn = 0
                    self.startGame()
                    break
                elif choice == 2:
                    print("Thx for playing!!")
                    exit()
                    break


    def drawGame(self):
        return all(not cell.isdigit() for cell in self.board.board)


    def winGame(self):
        combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for combo in combos:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                print(f"the player {self.players[1-self.turn].name} is the winer!!")
                return True
        else:
            return False

    def turnPlay(self):
        player = self.players[self.turn]
        self.board.desplayBoard()
        print(f"{self.players[self.turn].name}'s turn [{self.players[self.turn].symbol}]")
        while True:
            if self.board.updateBoard(self.players[self.turn].symbol) is True:
                break
        self.turn = 1 - self.turn





    def setPlayer(self):
        for number,player in enumerate(self.players, start=1):
            print("-"*20)
            print(f"Player {number} enter you details:")
            player.set_name()
            player.set_symbol()


game = Game()
game.startGame()