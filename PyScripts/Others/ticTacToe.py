# ticTacToe.py
#
# define object class for game node and test it
import re, random

class TicTacToe :
    nextTag  = 1
    winPats = ((0,1),(3,1),(6,1),(0,3),
               (1,3),(2,3),(0,4),(2,2))

    def __init__ (self, board, player, depth=0) :
        self.tag  = TicTacToe.nextTag
        self.board  = re.sub('\|','',board).upper() # use | to sep rows
        self.player = player
        self.depth  = depth
        self.alpha  = -9999   # New for extension
        self.beta   =  9999
        self.ivalue = 0       # Initial calculated value
        self.value  = 0       # Propogated back from successors
        self.next     = None  # Set by func chooseMove
        self.bestMove = None  # Set by func chooseMove
        self.legalMoves()
        self.eval()
        TicTacToe.nextTag += 1

    def move(self, which) :
        # make move, switch players, reevaluate board
        self.board = self.board[:which]+self.player+self.board[which+1:]
        if self.player =='X': self.player = 'O'
        else                : self.player = 'X'
        self.legalMoves()
        self.eval()

    def over(self) :
        # It's over with a win or no move possible
        return abs(self.value) == 100 or not self.moves

    def eval(self) :
        board = self.board
        for player in ('X','O') :
            val = 0
            for start,inc in self.winPats :
                n = 0
                for p in (start,start+inc,start+inc+inc) :
                    if board[p] == '.' : continue
                    if board[p] == player : n +=1
                    else : n = 0; break    # opponents piece here
                if n == 3 : val  = 100     # a win !!
                if n == 2 : val +=  30     # one move shy
            if player == 'X' :
                xval = val
                if xval >= 100 : xval=100; oval=0; break
            else :
                oval = val
                if oval >= 100 : xval=0; oval= 100; break
        self.ivalue = self.value = xval-oval # just who's ahead by how much

    def legalMoves(self) :
        # return list of empty positions
        moves = []
        for m in range(9) :
            if self.board[m] == '.' : moves.append(m)
        #random.shuffle(moves)      # uncomment to add some variete
        self.moves = tuple(moves)

    def maximizing(self) :
        # Want to maximize value if X, else minimize
        return (self.player == 'X') 

    def printMe(self, mesg="") :
        b = self.board
        print " %s" % (mesg)
        print " |%-3s|  tag=%s depth=%s   %s to play" % (
              b[0:3],self.tag,self.depth,self.player)
        print " |%-3s|  moves %s"   % (b[3:6],self.moves)
        print " |%-3s|  ival=%s fval=%s A=%s B=%s"   % (b[6:9],
                           self.ivalue, self.value,self.alpha,self.beta)
        print
        nxt = self.next
        if nxt : nxt.printMe("Next move is %s giving us..." % self.bestMove)

def test() :
   import timeSearch, sys
   args = sys.argv
   if len(args) == 3 : args.append("Y")  # default Alpha/beta on
   if len(args) == 4 : args.append(10)   # default max depth
   
   #                   class    board     Player    AlphaBeta      maxDepth
   timeSearch.timeSearch(TicTacToe, args[1], args[2], args[3]=='Y', int(args[4]))

if __name__ == "__main__" : test()

