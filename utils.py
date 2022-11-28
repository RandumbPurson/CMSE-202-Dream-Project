import pandas as pd
import numpy as np
import h5py
import os

from sklearn.model_selection import train_test_split

def get_subject_path(subject):
    """
    Convenience function to get the filename for a particular
    subject

    Parameters:
        subject: An int (1-3) corresponding to the subject number
    
    Returns:
        The filename for the sleep data for the subject

    """

    return "".join(["PreprocessedSleepDataSubject", str(subject), ".h5"])

def cvt_h5_dict(data):
    """
    Converts an h5 group into a dictionary of np arrays

    Parameters:
        data: the h5 group to be converted
    
    Returns:
        new_dict: the converted dictionary populated with
            np arrays of the data within the original h5
            group
    """

    new_dict = {}
    for key, val in data.items():
        proc_val = np.squeeze(np.array(val))
        new_dict[key] = proc_val
    return new_dict

def load_data(subject, root="preproc"):
    """
    Gets the mask dataframe and data for a subject
    
    Parameters:
        subject: the subject number (1-3)
        root (optional): the root directory where the subject
            data is stored, default="preproc"
    
    Returns:
        A tuple of...
        [0] mask_df: A pd dataframe object where the columns are 
            the features and each the content of the rows are masks 
            describing the locations of each feature within the data
        [1] data_arr: A np array providing the raw data, it must be
            masked using the various masks in `mask_df` to make any
            sense

    """
    fname = get_subject_path(subject)
    path = os.path.join(root, fname)
    
    dfile = h5py.File(path, "r")
    data = dfile["data"]
    mdata = dfile["metaData"]
    
    mdata_dict_arr = cvt_h5_dict(mdata)
    meta_df = pd.DataFrame.from_dict(mdata_dict_arr)
    data_arr = np.array(data)

    return meta_df, data_arr


def trim_front_back(instring, fstring, bstring):
    """Helper function to format class labels"""
    fpos = instring.find(fstring) + len(fstring)
    bpos = instring.find(bstring)
    return instring[fpos:bpos]


def encode_labels(masks):
    """
    Convert masks into a list of class names and array of indices

    Parameters:
        masks: a dataframe of masks such as the one returned 
            by `data_loader`
    
    Returns:
        label_names: a list of class names
        label_indices: the indices of the class value in a data
            array corresponding to the name at the same position
            in `label_names`
    """
    label_columns_mask = ["Synset" in colname for colname in masks.columns]
    label_colnames = masks.columns[label_columns_mask]
    label_names = [trim_front_back(name, "Synset_", "_ID") for name in label_colnames]
    label_indices = np.stack([masks[name].to_numpy().nonzero() for name in label_colnames]).squeeze()
    return label_names, label_indices

def get_onehot_labels_df(data, label_indices, label_names):
    """
    Convert a list of class names and array of indices into a
        dataframe with rows corresponding to samples and columns
        corresponding to classes
    
    Parameters:
        data: a data array such as the one returned by `load_data`
        label_names: a list of class names
        label_indices: the indices of the class value in a data
            array corresponding to the name at the same position
            in `label_names`
    
    Returns:
        label_df: a pd.DataFrame with rows being samples, columns
            being classes, and elements being class values
    """
    label_data = data[:, label_indices]
    label_df = pd.DataFrame(label_data, columns = label_names)
    return label_df

def get_features_arr(data, feature_df, feature):
    """
    Helper function to get data from a dataframe of masks

    Parameters:
        feature_df: an array of feature masks where the column
            is the name of the corresponding feature area
        feature: a string corresponding to one of the feature
            areas
    
    Returns:
        feature_data: a np.ndarray of the data corresponding to
            `feature`
    """
    feature_mask = feature_df[feature].to_numpy().astype(bool)
    feature_data = data[:, feature_mask]
    return feature_data

class DataHandler:
    
    def __init__(self, masks, data, test_size=0.2):  
        """
        Initialize the DataHandler 

        Parameters:
            masks: a dataframe of region masks generated by utils.load_data
            data: an np array of the data generated by utils.load_data
            test_size (0.2): the percent of the data for the test set
        """
        if test_size == 0:
            train_data, test_data = data, np.array([])
        else:
            train_data, test_data = train_test_split(data, test_size=test_size)
        self.data = {
            "train": train_data,
            "test": test_data
        }

        self.label_names, self.label_indices = encode_labels(masks)
        self.label_counts = data[:, self.label_indices].sum(1).astype(int)
        
        self.feature_names = ["FFA", "HVC", "LOC", "LVC", "PPA", "V1", "V2", "V3"]
        self.feature_df = masks[self.feature_names]
    
    def get_feature(self, feature_names, split_set="train"):
        """
        Get a feature area or a set of feature areas

        Parameters:
            feature_names: a string corresponding to a feature area
                or a list of these strings
            split_set ("train"): one of "train" or "test", depending on which
                set to pull from
        """
        if not isinstance(feature_names, list):
            feature_names = [feature_names]

        features = []
        for feature_name in feature_names:
            feature = get_features_arr(
                self.data[split_set], 
                self.feature_df, 
                feature_name
            )
            features.append(feature)
        
        return np.concatenate(features, 1)
    
    def get_labels(self, label_name = None, split_set="train"):
        """
        Get the data for a single class label

        Parameters:
            label_name (None): the class to get, if none get all classes
            split_set ("train"): one of "train" or "test", depending on which
                set to pull from
        
        Returns:
            label: the train or test data for the appropriate class
        """
        labels = get_onehot_labels_df(
            self.data[split_set],
            self.label_indices,
            self.label_names
        ).to_numpy()
        if label_name is not None:
            class_idx = self.label_names.index(label_name)
            labels = labels[:, class_idx]
        return labels
    
    def get_label_names(self, counts = False):
        """
        Get the class names

        Parameters:
            counts (False): whether to return the number of
                each class that appears
        """
        if counts:
            return dict(zip(self.label_names, self.label_counts))
        else:
            return self.label_names