import matplotlib.pyplot as plt

euclideancount = 0


def showcartesian(titikterdekat,titik) :
    fig = plt.figure()
    x = []
    y = []
    z = []
    xclose = []
    yclose = []
    zclose = [] 

    # masukin yg pasangan terdekat
    for i in range(len(titikterdekat)) :
        for j in range(0,3) :
            if(j == 0) :
                xclose.append(titikterdekat[i][j])
            elif(j == 1) :
                yclose.append(titikterdekat[i][j])
            else :
                zclose.append(titikterdekat[i][j])

    # masukin yg lain
    for i in range(len(titik)) :
        for j in range(0,3) :
            if(j == 0 and titik[i][j] != xclose[0] and titik[i][j] != xclose[1]) :
                x.append(titik[i][j])
            elif(j == 1 and titik[i][j] != yclose[0] and titik[i][j] != yclose[1]) :
                y.append(titik[i][j])
            elif(j == 2 and titik[i][j] != zclose[0] and titik[i][j] != zclose[1]) :
                z.append(titik[i][j])
    ax = plt.axes(projection='3d')
    ax.scatter(x,y,z, c = 'k')
    ax.scatter(xclose,yclose,zclose, c = 'r')
    

    ax.set_title('Diagram kartesian')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')

    plt.show()