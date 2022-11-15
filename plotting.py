import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc


def plot_pr_curve(model, testx, testy, savefig=None):
    pos_probas = model.predict_proba(testx)[:, 1]
    precision, recall, thresh = precision_recall_curve(testy, pos_probas)
    ap = auc(recall, precision)
    print(f"average precision: {ap}")

    plt.figure()
    plt.plot(recall, precision)
    plt.xlabel("recall")
    plt.ylabel("precision")

    if savefig is not None:
        plt.savefig(savefig)