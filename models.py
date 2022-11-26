from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

from utils import DataHandler

class DreamLR:

    def __init__(self, masks, data, test_size=0.2):
        self.data_handler = DataHandler(masks, data, test_size=test_size)
        self.get_label_names = self.data_handler.get_label_names

    def run(self, feature_name, class_name = None, **kwargs):
        """
        Runs the model to predict "class_name" using "feature_name"

        Parameters:
            feature_name: one of the feature region names eg;
                ["FFA", "HVC", "LOC", "LVC", "PPA", "V1", "V2", "V3"]
            class_name: one of the names in self.label_names, if None, do multiclass
            **kwargs: any additional keyword arguments are passed to
                sklearn.linear_model.LogisticRegression
        
        Returns:
            model: the fitted model object
            testx: the features for the chosen feature group
            testy: the labels for the chosen class

        """
        print(f"running for class:{class_name}...")
        trainx = self.data_handler.get_feature(feature_name)
        testx = self.data_handler.get_feature(feature_name, split_set="test")
        
        model = LogisticRegression(
            solver="lbfgs", max_iter=1000, class_weight="balanced",**kwargs
        )

        if class_name is not None:
            trainy = self.data_handler.get_label(class_name)
            testy = self.data_handler.get_label(class_name, split_set="test")
        else:
            trainy = self.data_handler.get_multi_labels()
            testy = self.data_handler.get_multi_labels(split_set="test")
            model = MultiOutputClassifier(model)
        
        fit_model = model.fit(trainx, trainy)

        return fit_model, testx, testy