from function import func
import random


def findMin(x1,x2,y1,y2,X,Y):
    x=X
    y=Y
    z=func(X,Y)
    
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if X+i < x1 or X+i > x2 or Y+j < y1 or Y+j > y2:
                continue


            if z > func(X+i,Y+j):
                x=X+i
                y=Y+j
                z=func(X+i,Y+j)
    return x,y,z


def main():
    file=open('input.txt','r')
    inputX=file.readline()
    inputY=file.readline()
    file.close()
    
    x1, x2= inputX.split(',')
    x1=int(x1)
    x2=int(x2)
    y1, y2= inputY.split(',')
    y1=int(y1)
    y2=int(y2)
    

    minX=x1
    minY=y1
    minZ=func(x1,y1)

    w=x2-x1+1
    h=y2-y1+1
    matrix=[[0.0 for x in range(w)] for y in range(h)]
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            data=func(i,j)
            matrix[j-y1][i-x1]=data
            if minZ > data:
                minX=i
                minY=j
                minZ=data

                
    print(minX)
    print(minY)
    print( round(minZ,3))



    k=y2-y1+1
    state=[]


    for i in range(k):
        x=random.randrange(x1, x2+1,1)
        y=i+y1#random.randrange(y1, y2+1,1)
        z=func(x,y)
        state.append((z,x,y)) 

    minX=x1
    minY=y1
    minZ=func(minX,minY)
    
    loop=100
    while  loop >0:
        loop=loop-1
        
        count=0
        for i in range(k):  
            ele=state[i]      
            x,y,z=findMin(x1, x2, y1, y2, ele[1], ele[2])
            #state.append((z,x,y))

            if x==ele[1] and y==ele[2]:
                x=random.randrange(x1, x2+1,1)
                y=random.randrange(y1, y2+1,1)
                z=func(x,y)
                count=count+1
                
            state.append((z,x,y))

            if minZ > z:
                minZ=z
                minX=x
                minY=y
            
        if count==k:
            break
            


        state.sort()


        for i in range(k):
            state.pop()


        

    print(minX)
    print(minY)
    print( round(minZ,3))



if __name__ == '__main__':
    main()