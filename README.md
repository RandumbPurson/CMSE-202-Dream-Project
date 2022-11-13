# CMSE-202-Dream-Project

A project to classify dreams using fMRI data from Horikawa Et. Al - [dream classification dataset](http://brainliner.jp/data/brainliner/Human_Dream_Decoding)

> If you need to get the dataset, please read the section at the bottom of this file so that we all have the same file structure!

## TODO
- [x] Data Exploration
    - [x] Initial Exploration
    - [x] Create Pandas df
    - [ ] graphs 
        - [ ] pie charts, show different label distributions
- [ ] Preprocessing
    - [ ] train-test-val split
- [ ] Extra Research on Brian areas?
- [ ] Create Model
    - [ ] Logistic Regression - maybe switch to SVM once we learn about it?
- [ ] Train Model
- [ ] Test Model
- [ ] Format Results
- [ ] Write Draft
- [ ] Make Presentation
    - [ ] Slides


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
