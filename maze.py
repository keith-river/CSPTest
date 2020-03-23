class maze:
    "mz=maze();mz.find(0,0,0,0)"
    moves=[[0,1],[1,0]]
    counter=[]
    
    def __init__(self):
        p=self
        p.H,p.W=map(int,input().split())
        p.board=['' for h in range(p.H)]
        for h in range(p.H):
            s=input()
            p.board[h]=[s[w] for w in range(p.W)]
    def __del__(self):
      print(min(self.counter))
        
    def on_white(self,x,y):
        p=self
        return 0<=x<p.W and 0<=y<p.H and p.board[x][y]=='.'
    def set_white(self,x,y,n,c):
        p=self
        p.board[x][y]=str(n)
        return c
    def reset_white(self,x,y,c):
        p=self
        p.board[x][y]='.'
        return c            
    def on_black(self,x,y):
        p=self
        return 0<=x<p.W and 0<=y<p.H and p.board[x][y]=='#'
    def set_black(self,x,y,n,c):
        p=self
        p.board[x][y]=str(n)
        return c+1
    def reset_black(self,x,y,c):
        p=self
        p.board[x][y]='#'
        return c-1
    def is_goal(self,x,y):
        return x==self.W-1 and y==self.H-1
    
    def find(self,x,y,n,c):
        p=self
        if (p.on_white(x,y)):
            c=p.set_white(x,y,n,c)
            if p.is_goal(x,y):
                p.result(c)
            else:
                for k in range(len(p.moves)):
                    dx,dy = p.moves[k]
                    p.find(x+dx,y+dy,n+1,c)
            c=p.reset_white(x,y,c)
        elif (p.on_black(x,y)):
            c=p.set_black(x,y,n,c)
            if p.is_goal(x,y):
                p.result(c)
            else:
                for k in range(len(p.moves)):
                    dx,dy = p.moves[k]
                    p.find(x+dx,y+dy,n+1,c)
            c=p.reset_black(x,y,c)            
    def result(self,c):
        #for h in range(self.H):
        #    print(self.board[h]) 
        self.counter+=[c]

mz=maze();
mz.find(0,0,0,0)
