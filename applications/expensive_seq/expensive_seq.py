# Your code here


def expensive_seq(x, y, z):
    # Your code here
    cache = {}

    def nest_expseq(x, y, z):
        if x <= 0:
            return y + z
        
        if (x, y, z) not in cache:
            cache[(x, y, z)] = nest_expseq(x-1,y+1,z) + nest_expseq(x-2,y+2,z*2) + nest_expseq(x-3,y+3,z*3)

        return cache[(x, y, z)]
        
    return nest_expseq(x, y, z)
    
if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
