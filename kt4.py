#
#
#
class kt:
    "k=kt(8);k.find(0,0,0)"
    moves=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    
    def __init__(self,n):
        self.count,self.N=0,n
        self.board=[[-1 for i in range(self.N)] for j in range(self.N)] 

    def safe(self,x,y):
        return 0<=x<self.N and 0<=y<self.N and self.board[x][y]<0

    def find(self,n,x,y):
        if (self.safe(x,y)):
            self.board[x][y]=n
            if (n>=self.N*self.N-1):
                self.printResult()
            else:
                for k in range(len(self.moves)):
                    dx,dy = self.moves[k]
                    self.find(n+1,x+dx,y+dy)
                    self.count += 1
            self.board[x][y]=-1

    def printResult(self):
        for x in range(self.N):
            line = [ "[%2d]" % self.board[x][y] for y in range(self.N)]
            print "".join(line) 
        print "Count=[%d]" % self.count
        self.count=0
