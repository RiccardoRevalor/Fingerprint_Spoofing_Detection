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



