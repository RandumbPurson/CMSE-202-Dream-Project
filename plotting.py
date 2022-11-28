import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, multilabel_confusion_matrix

def plot_cf(mcf, label_name, ax):
	sb.heatmap(mcf, annot=True, ax = ax, cbar = False, xticklabels = ["F", "T"], yticklabels=["F", "T"], cmap="Greens")
	ax.set_title(label_name)
	ax.set_xlabel("prediction")
	ax.set_ylabel("true label")

def plot_confusion_matrix(labels, predictions, label_names, **kwargs):
    """
    Plot and return the confusion matrices for a set of labels and predictions
    
    Parameters:
        labels: an array of the true labels, should have shape (n,) for single
            label classification or (n, n classes) for multilabel
        predictions: an array of the predictions from the features corresponding
            to the labels, should have the same shape as labels
        label_names: either the name of the class for single classification, or
            a list of class names with shape (n classes) for multilabel. Should
            be in the same order as the labels and predictions.
    """
    if labels.ndim == 2:
        nrow = np.sqrt(labels.shape[-1]).astype(int)
        fig, ax = plt.subplots(
            nrow + 1, nrow, 
            figsize = ((nrow + 1) *2, nrow*2)
        )
        ax = ax.flatten()
        ml_conf_matrix = multilabel_confusion_matrix(labels, predictions, **kwargs)
        for i in range(ml_conf_matrix.shape[0]):
            plot_cf(ml_conf_matrix[i], label_names[i], ax[i])
        fig.tight_layout()
        return fig
    else:
        fig, ax = plt.subplots(1)
        conf_matrix = confusion_matrix(labels, predictions, **kwargs)
        plot_cf(conf_matrix, label_names, ax)
        
        return fig