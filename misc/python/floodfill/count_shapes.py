#!/usr/bin/env python

grid=[
 [ 0 , 0 ,  0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],
 [ 0 , 1 ,  1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 ],
 [ 0 , 1 ,  1 , 0 , 0 , 0 , 1 , 0 , 1 , 0 ],
 [ 1 , 1 ,  0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 ],
 [ 0 , 0 ,  0 , 1 , 1 , 0 , 0 , 0 , 1 , 0 ],
 [ 0 , 0 ,  1 , 1 , 1 , 0 , 1 , 0 , 0 , 0 ],
 [ 0 , 0 ,  0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ],
 [ 0 , 0 ,  0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 ],
 [ 0 , 1 ,  0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ],
 [ 0 , 1 ,  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
]


class Bitmap(object):
    def __init__(self,grid):
        self.grid=grid
        self.width=len(grid[0])
        self.height=len(grid)
        self.visited=[[0 for i in range(self.width)] for j in range(self.height)]

        self.visited[5][5]=1

    def trace_shape(self,x,y):
        matrix=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
        queue=[]
        queue.append((x,y))
        while len(queue):
            dx,dy=queue.pop()
            for coord in matrix:
                cur_x= dx+coord[0]
                cur_y=dy+coord[1]
                if cur_x>-1 and cur_y>-1 and cur_x<self.width and cur_y<self.height:
                    if not self.visited[cur_x][cur_y] :
                        if self.grid[cur_x][cur_y]:
                            self.visited[cur_x][cur_y]=1
                            queue.append((cur_x,cur_y))
                        else:
                            self.visited[cur_x][cur_y]=2

    def count(self):
        cur_count=0
        for x in range(self.width):
            for y in range(self.height):
                if not self.visited[x][y]:
                    if self.grid[x][y]:
                        self.trace_shape(x,y)
                        cur_count +=1
                
                #self.visited[x][y]=1
                #else:
                #    print "skipping (%i, %i), visited" % (x,y)
        return cur_count

if __name__ ==  "__main__":
    bitcount = Bitmap(grid)
    print "Total Shapes: %i" % bitcount.count()
    for row in grid:
        print row
