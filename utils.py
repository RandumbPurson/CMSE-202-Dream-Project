import pandas as pd
import numpy as np
import h5py
import os

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