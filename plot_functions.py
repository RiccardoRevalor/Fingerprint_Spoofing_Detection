import numpy as np
import matplotlib.pyplot as plt

def densityHistograms(X, n_components, y=None,labelColors=None, classNames=None, rows=2, cols=3, bins=30, title=None, xtitles=None, ytitles=None, subTitles=None):
    """
    
    Parametri:
    - X: array (n_samples, n_features), dataset delle feature.
    - n_components: int, numero di componenti principali da considerare.
    - y: array opzionale (n_samples,), etichette per colorare le classi (default: None).
    - labelColors: array of colors for each class
    - bins: int, numero di bin negli istogrammi (default: 30).
    
    Output:
    - Istogrammi delle prime n componenti principali.
    """
    if n_components == 1:
        plt.figure(figsize=(6, 4))
        
        if y is not None:
            for label in np.unique(y):
                color = labelColors[label] if labelColors else None
                class_label = f'Class {classNames[label]}' if classNames else f'Class {label}'
                plt.hist(X[0, y == label], bins=bins, alpha=0.5, color=color, label=class_label, density=True, edgecolor="black")
            plt.legend()
        else:
            plt.hist(X[0, :], bins=bins, alpha=0.7, color='b', edgecolor="black", density=True)
        
        plt.title(subTitles[0])
        plt.xlabel(xtitles[0])
        plt.ylabel(ytitles[0])
        plt.show()
        return
    

    # Crea i plot
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols*6, rows*4))  
    axes = axes.ravel()  # Per iterare facilmente sugli assi

    for i in range(n_components):
        ax = axes[i]
        if y is not None:
            # Istogramma colorato per classi
            for label in np.unique(y):
                if classNames is not None:
                    ax.hist(x=X[i, y == label], color=labelColors[label], bins=bins, alpha=0.5, label=f'Class {classNames[label]}', density=True, edgecolor="black")
                else:
                    ax.hist(x=X[i, y == label], color=labelColors[label], bins=bins, alpha=0.5, label=f'Class {label}', density=True, edgecolor="black")
            ax.legend()
        else:
            # Istogramma normale se non ci sono classi
            ax.hist(x=X[i, :], bins=bins, alpha=0.7, color='b', edgecolor="black", density =True)
        
        ax.set_title(subTitles[i])
        ax.set_xlabel(xtitles[i])
        ax.set_ylabel(ytitles[i])

    plt.tight_layout()
    if title is not None:
        fig.suptitle(title, fontsize=16)  # General title
    plt.show()




def densityPlots_TR_VAL(xTR, yTR, xVAL, yVAL, title1=None, bins1=None, title2=None, bins2=None, title=None, xlabel="LDA direction", labelColors=None, classLabels=None, rows=2, cols=1):
    #I select feature i and feature j, with i different from j and plot them on the 2 axis of every scatter plot chart


    #subplot creation
    fig, plots = plt.subplots(nrows=rows, ncols=cols, figsize=(cols*6, rows*4))
    plots = plots.flatten()   #the 2D axes array becomes a 1D array in order to access each ax in a more straighforward way during the loop

    subplot = plots[0]
    for label in labelColors:
        sample_with_that_class = xTR[0, yTR == label]
        subplot.hist(x=sample_with_that_class, color=labelColors[label], alpha= 0.7, density=True, label=f"{classLabels[label]}", edgecolor="black", bins=bins1)
        subplot.legend()
        if title1:
            subplot.set_title(title1)
        subplot.set_xlabel(xlabel)
        subplot.set_ylabel("Density")


    subplot = plots[1]
    for label in labelColors:
        sample_with_that_class = xVAL[0, yVAL == label]
        subplot.hist(x=sample_with_that_class, color=labelColors[label], alpha= 0.7, density=True, label=f"{classLabels[label]}", edgecolor="black", bins=bins2)
        subplot.legend()
        if title2:
            subplot.set_title(title2)
        subplot.set_xlabel(xlabel)
        subplot.set_ylabel("Density")

    plt.tight_layout(pad=3) #add padding between subplots to distance between eachother
    if title:
        fig.suptitle(title, fontsize=16)  # General title
    plt.show()




# m is the number of dimensions
def plotSingle(D, L, m):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]
    print(m)
    for i in range(m):
        plt.figure()
        plt.xlabel("Feature " + str(i))
        plt.ylabel("Number of elements")
        plt.hist(D0[i, :], bins=60,density=True, alpha=0.7, label="Spoofed fingerprint")
        plt.hist(D1[i, :], bins=60, density=True, alpha=0.7, label="Authentic fingerprint")
        plt.legend()
        plt.show()


def plotTot(D, L, m):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]

    plt.figure()
    plt.xlabel("Feature " )
    plt.ylabel("Number of elements")
    plt.hist(D0[:, :], density=True, alpha=0.7, label="Spoofed fingerprint")
    plt.hist(D1[:, :], density=True, alpha=0.7, label="Authentic fingerprint")
    plt.legend()
    plt.show()


# m is the number of dimensions
def plotCross(D, L,m):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]

    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            plt.figure()
            plt.xlabel("Feature " + str(i))
            plt.ylabel("Feature " + str(j))
            plt.scatter(D0[i, :], D0[j, :], label="Spoofed fingerprint")
            plt.scatter(D1[i, :], D1[j, :], label="Authentic fingerprint")
            plt.legend()
            plt.show()



