import matplotlib.pyplot as plt

def showcartesian(titikterdekat,titik) :
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
            if(j == 0) :
                x.append(titik[i][j])
            elif(j == 1) :
                y.append(titik[i][j])
            elif(j == 2) :
                z.append(titik[i][j])
                
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    for i in range(len(titik)) :
        ax.plot(x[i], y[i], z[i], 'ok')

    for i in range(len(titikterdekat)) :
        ax.plot(xclose[i], yclose[i], zclose[i], 'or')

    

    ax.set_title('Diagram kartesian')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')

    plt.show()