

def main():
    R  = int(raw_input())
    gridm = []
    grid = []
    for i in xrange(R):
        gridm.append(raw_input())
    print gridm
    for mc in gridm:
        kk = map(int,list(mc))
        grid.append(kk)
    print grid
    for j in range(R):
      for i in range(R):
        move(i,j,grid,R)
 
def move(i,j,grid,R):
    if i>0 and j>0:
        if i < (R-1) and j < (R-1):
         print "cccccccccccord",i,j
         print grid
         sumc = 0
         dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
         for d in dire:
            if grid[i][j] < grid[i+d[0]][j+d[1]] :
                sumc += 1
                print "sssssssssssss",sumc
            if sumc == 4:
                print grid[i][j]

if __name__ == '__main__':
    main()


