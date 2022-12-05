# CMSE-202-Dream-Project

A project to classify dreams using fMRI data from Horikawa Et. Al - [dream classification dataset](http://brainliner.jp/data/brainliner/Human_Dream_Decoding)

> If you need to get the dataset, please read the section at the bottom of this file so that we all have the same file structure!

## TODO
- [x] Data Exploration
    - [x] Initial Exploration
    - [x] Create Pandas df
    - [x] graphs
        - [x] bar charts
- [x] Preprocessing - See DataHandler class
    - [x] train-test-val split
- [x] Extra Research on Brain areas?
- [x] Create Model
    - [x] Logistic Regression
    - [x] SVM
        - [x] RBF Kernel
        - [x] Multiclass Regression
- [x] Test Model
    - [x] Accuracy
    - [x] Precision
    - [x] Recall
    - [x] F1-score
    - [x] Confusion Matrix
- [x] Format Results
- [x] Write Draft
- [x] Make Presentation
    - [x] Slides


## How to run our code:
1. Download the h5 files.
2. Survey and analyze the functions made and imported into our notebooks in the files: utils.py, plotting.py, and models.py.
3. Run "Data Exploration" notebook for introduction to our data and how we are thinking of completing our tasks.
4. Run "Dream Bar Charts" for some initial visualizations on the features.
5. Run "Logistic Regression" for results to be analyzed for why we then went to SVMs!
6. Run "SVM_Dream_Project" notebook for results on our SMV models for this project with an accuracy score of 94%!
7. Check our this README.md file to see our checklist of what we did, resources we used, contributions each member made, and more information.
#### Option B for our Project Code: Run the "Final Notebook Dreams" for all of these steps included in one notebook!


## Useful Links
- [original paper](https://www.researchgate.net/profile/Masako-Tamaki/publication/236113471_Neural_Decoding_of_Visual_Imagery_During_Sleep/links/02e7e53a5e1eba1005000000/Neural-Decoding-of-Visual-Imagery-During-Sleep.pdf)
- [paper supplement](https://www.science.org/doi/suppl/10.1126/science.1234330/suppl_file/horikawa.sm.pdf)

## Alternative Datasets
- [visualizations](https://www.datatobiz.com/blog/brain-waves-data-using-python/)
- [mammal sleep dataset](https://www.kaggle.com/datasets/mathurinache/sleep-dataset?resource=download)
- [sleep state dataset](https://zenodo.org/record/2650142#.Y2bG8C2B0Ut)

## Link to Presentation Google Slides
- https://docs.google.com/presentation/d/12pSqdrO2Vww2gJfNwfyR0YUEXY6oC9be72cOLrxb6dU/edit?usp=sharing 

### Dataset Info
To get the dataset, go to the [dream classification dataset](http://brainliner.jp/data/brainliner/Human_Dream_Decoding) and download the file `preproc.zip`. Unzip it into a folder called `preproc` so that we all have uniform file structures.

### Git Workflow
We plan to use feature branches for development.
When working on some new feature eg pie charts, create a new branch `pie-charts` from master and commit to that branch until whatever you are doing works as intended. Then we can create a new pull request on github and merge it into the master branch. 

Merging on github instead of locally will help isolate the different parts of our project so that we can work on them in parallel even if some parts aren't fully working.

Also, we should use a couple different jupyter notebooks to develop eg; one for data exploration, one for visualizations, one for the models etc. At the end we can combine these into a single final notebook.

### Contributions:
- Emma: Logistic Regression, helped with GitHub merging, helped with slideshow, attended meetings
- Sam: SVM, helped with GitHub, helped with slideshow, attended meetings
- Holly: Made slideshow, background research, helped with SVM, attended meetings
- Myles: Initial data visualization
