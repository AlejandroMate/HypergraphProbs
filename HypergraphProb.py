

# Ejemplo

N = 1000
V = np.arange(N)

T = 100

HG = []
for t in range(T):

    sample = []
    for i in V:
        elem = np.random.choice([0,1], p=[0.5, 0.5])
        sample.append(elem)

    HG.append(sample)

c=np.zeros(N)
for ha in HG:
    for i,e in enumerate(ha):
        if e==1:
            c[i]+=1


u, cnts = np.unique(c , return_counts=True)

prob = cnts.astype(np.float64)/np.sum(cnts)



########
# Codigo optimizado 1.

# Ejemplo

N = 5000
V = np.arange(N)

T = 100

HG = []
for t in range(T):

    sample = np.random.choice([0,1],
                                 size=N,
                                 p=[0.5, 0.5])
    HG.append(sample)

c=np.zeros(N)
for ha in HG:
    for i,e in enumerate(ha):
        if e==1:
            c[i]+=1


u, cnts = np.unique(c , return_counts=True)

prob = cnts.astype(np.float64)/np.sum(cnts)

