from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np
from k_means import K_means
from scipy.spatial import Voronoi, voronoi_plot_2d

diabetes = datasets.load_diabetes()
x_real = diabetes.data
y_real = diabetes.target

KMemes = K_means(100, [], 7)
KMemes.lloyd_clustering()

vor = Voronoi(KMemes.C)
for i in range (KMemes.k):
    array = np.asarray(KMemes.clusters[i])
    tr_array = np.transpose(array)
    plt.scatter(tr_array[0], tr_array[1], s=20)
    plt.plot(KMemes.C[i][0],KMemes.C[i][1],  marker='^')

#for vpair in vor.ridge_vertices:
    #if vpair[0] >= 0 and vpair[1] >= 0:
        #v0 = vor.vertices[vpair[0]]
        #v1 = vor.vertices[vpair[1]]
        # Draw a line from v0 to v1.
        #plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k', linewidth=2)

plt.show()
