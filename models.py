from sklearn.linear_model import LogisticRegression

from utils import DataHandler
from plotting import plot_pr_curve

class DreamLR:

    def __init__(self, masks, data, test_size=0.2):
        self.data_handler = DataHandler(masks, data, test_size=test_size)

    def run(self, class_name, feature_name, savefig=None, **kwargs):
        """
        Runs the model to predict "class_name" using "feature_name"

        Parameters:
            class_name: one of the names in self.label_names
            feature_name: one of the feature region names eg;
                ["FFA", "HVC", "LOC", "LVC", "PPA", "V1", "V2", "V3"]
            savefig (opt): the filename to save the precision-recall
                figure at. If none provided, does not save.
            **kwargs: any additional keyword arguments are passed to
                sklearn.linear_model.LogisticRegression
        """
        print(f"running for class:{class_name}...")
        trainx = self.data_handler.get_feature(feature_name)
        trainy = self.data_handler.get_label(class_name)

        testx = self.data_handler.get_feature(feature_name, split_set="test")
        testy = self.data_handler.get_label(class_name, split_set="test")
        
        model = LogisticRegression(
            solver="lbfgs", max_iter=1000, **kwargs
        ).fit(trainx, trainy)

        plot_pr_curve(model, testx, testy, savefig=savefig)