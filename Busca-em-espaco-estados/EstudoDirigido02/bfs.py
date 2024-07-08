import random

def bfs(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    
    bfsPath={}

    while fronteira !=[]:
        vertice=fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("objetivo encontrado")
            break

        movimentos=["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]==True:
                if d=='E':
                    vizinho=(vertice[0],vertice[1]+1)
                if d=='W':
                    vizinho=(vertice[0],vertice[1]-1)
                if d=='N':
                    vizinho=(vertice[0]-1,vertice[1])
                if d=='S':
                    vizinho=(vertice[0]+1,vertice[1])
                
                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    bfsPath[vizinho]=vertice
                

    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath