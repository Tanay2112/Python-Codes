rook = (int(input('x = ')),int(input('y = ')))
queen = (int(input('x = ')),int(input('y = ')))

rpsp = {(i,rook[1]) for i in range(1,9) if i != rook[0]} \
    | {(rook[0],i) for i in range(1,9) if i != rook[1]}

qpsp = {(i,queen[1]) for i in range(1,9) if i != queen[0]} \
    | {(queen[0],i) for i in range(1,9) if i != queen[1]} \
    | {(i,j) for i,j in zip(range(queen[0]-1,0,-1),range(queen[1]-1,0,-1))} \
    | {(i,j) for i,j in zip(range(queen[0]-1,0,-1),range(queen[1]+1,9))} \
    | {(i,j) for i,j in zip(range(queen[0]+1,9),range(queen[1]+1,9))} \
    | {(i,j) for i,j in zip(range(queen[0]+1,9),range(queen[1]-1,0,-1))}

for i in sorted(rpsp & qpsp):
    print(i)
