from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from utils import get_features_arr, get_onehot_labels_df, encode_labels
from plotting import plot_pr_curve

class DreamLR:

    def __init__(self, masks, data, test_size=0.2):
        """
        Initialize the DreamLR model

        Parameters:
            masks: a dataframe of region masks generated by utils.load_data
            data: an np array of the data generated by utils.load_data
        """
        self.train_data, self.test_data = train_test_split(data, test_size=test_size)

        self.label_names, self.label_indices = encode_labels(masks)
        
        self.feature_names = ["FFA", "HVC", "LOC", "LVC", "PPA", "V1", "V2", "V3"]
        self.feature_df = masks[self.feature_names]

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
        class_idx = self.label_names.index(class_name)
        trainy = get_onehot_labels_df(
            self.train_data, 
            self.label_indices, 
            self.label_names
        ).to_numpy()[:, class_idx]
        trainx = get_features_arr(
            self.train_data, 
            self.feature_df, 
            feature_name
        )
        testy = get_onehot_labels_df(
            self.test_data, 
            self.label_indices, 
            self.label_names
        ).to_numpy()[:, class_idx]
        testx = get_features_arr(
            self.test_data, 
            self.feature_df, 
            feature_name
        )


        model = LogisticRegression(
            solver="lbfgs", max_iter=1000, **kwargs
        ).fit(trainx, trainy)

        plot_pr_curve(model, testx, testy, savefig=savefig)