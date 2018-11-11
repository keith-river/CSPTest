# coding: shift-jis 
# vanish? 

N=7
board=[[-1,-1, 1, 1, 1,-1,-1],
       [-1,-1, 1, 1, 1,-1,-1],
       [ 1, 1, 1, 1, 1, 1, 1],
       [ 1, 1, 1, 0, 1, 1, 1],
       [ 1, 1, 1, 1, 1, 1, 1],
       [-1,-1, 1, 1, 1,-1,-1],
       [-1,-1, 1, 1, 1,-1,-1]]
import copy
init_board=copy.deepcopy(board)
direct = [[0,1],[1,0],[0,-1],[-1,0]] # East,South,West,North
def ds(d): return "ESWN"[d]

def count_rest():
   def count_positive(l): return sum([i for i in l if i>0])
   return sum([count_positive(l) for l in board])

def with_in_board(x,y):
  return x in range(N) and y in range(N) # >=0

def exists(x,y):
  return with_in_board(x,y) and board[x][y]>0

def get_tupple(opt):
  x,y,d = opt
  dx,dy = x+direct[d][0],y+direct[d][1]
  jx,jy = dx+direct[d][0],dy+direct[d][1]
  return x,y,dx,dy,jx,jy

def can_do(opt): 
  x,y,dx,dy,jx,jy = get_tupple(opt)
  return exists(x,y) and exists(dx,dy) and with_in_board(jx,jy) and board[jx][jy]==0

def do(opt): 
  x,y,dx,dy,jx,jy = get_tupple(opt)
  board[x][y],board[dx][dy],board[jx][jy]=0,0,1

def cancel_do(opt): 
  x,y,dx,dy,jx,jy = get_tupple(opt)
  board[x][y],board[dx][dy],board[jx][jy]=1,1,0

def find_option():
  return [(x,y,d) for x in range(N) for y in range(N) \
                        for d in range(4) if can_do((x,y,d))]

def print_board(opt,board):
  def xyo(x,y):
     if x==opt[0] and y==opt[1]: return "[%s]" % ds(opt[2])
     elif board[x][y]>0: return "[o]"
     else: return "[ ]" 
  for x in range(N):
      line = [ xyo(x,y) for y in range(N) ]
      print ''.join(line)
  print "try to move [%d,%d] for %s\n" % (opt[0],opt[1],ds(opt[2]))

def print_solution(route):
    replay = copy.deepcopy(init_board)
    def do(opt): 
      x,y,dx,dy,jx,jy = get_tupple(opt)
      replay[x][y],replay[dx][dy],replay[jx][jy]=0,0,1
    line = ["[%d,%d,%s]" % (r[0],r[1],ds(r[2])) for r in route]
    print "[sequence]:" + "".join(line)
    print ":::::::::::::::::::::start replaying"
    for r in route:
        print_board(r,replay)
        do(r)
    print ":::::::::::::::::::::finish replaying."

def find(route):
  if count_rest()>1:
    for opt in find_option():
      do(opt)
      route.append(opt);
      find(route)
      route.pop()
      cancel_do(opt)
  else:
     print "*** I've just find it ***"
     print_solution(route)

if __name__ == '__main__':
   find([])
 
