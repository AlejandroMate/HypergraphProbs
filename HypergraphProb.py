#!/usr/bin/python3

from scipy.sparse import rand
import matplotlib.pyplot as plt
import numpy as np
import click

@click.command()
@click.option("--nelems", type=int, default=10000, help="Number of elements in set V.")
@click.option("--tsteps", type=int, default=10000, help="Number of time steps.")
def main(nelems, tsteps):

    # Chunk size to split the whole process duration into smaller processes
    # This is for memory reasons. In the limit chunk_sz -> 1 we are memory efficient but slow.
    # In 8GB, n*chunk_sz = 1e8 works in the limit
    chunk_sz = 100             

    deg_cum = np.zeros((1,nelems))   # Array to accumulate degree counts
    n_chunks = tsteps//chunk_sz + 1
    for i in range(n_chunks):    # Divide t steps, into chunks of chunk_sz steps.
        print(f"{i}/{n_chunks}")
        process = rand(chunk_sz , nelems , 0.5, format='csc') > 0.5
        deg_cum += process.sum(axis=0)

    dist = np.unique(np.array(deg_cum), return_counts=True)[1]

    plt.plot(dist)
    plt.show()


if __init__ == "__main__":
    main()



