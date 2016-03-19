class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def make_grid(grid_x, grid_y):
    grid = [[Tile(x,y) for x in xrange(grid_x)] for y in xrange(grid_y)]
    return grid
    
    
def traverse(grid):
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            print x,y

def factorial(n):
    if n <= 1:
        return 1
    else: return n * factorial(n-1) 
    
## http://mathworld.wolfram.com/BinomialCoefficient.html
#binomial coefficient
# (n; k) = (a+b; a) where (x,y) = (a,b)
#_nC_k=(n; k)=(n!)/((n-k)!k!), 
def bin_coef(x_len, y_len):
    n = x_len+y_len
    k = x_len
    fac_n = factorial(n)
    fac_n_minus_k = factorial(n-k)
    fac_k = factorial(k)

    return fac_n/(fac_n_minus_k*fac_k)
    


if __name__ == "__main__":
    #grid = make_grid(2,2)
    #traverse(grid)

    print bin_coef(2,2)#6
    print bin_coef(20,20)#137846528820
    print bin_coef(100,100)#90548514656103281165404177077484163874504589675413336841320
    

    
