Predicting Types of Cyberbullying from Tweets
==============================

### Summary

This project aims to build a predictive model by comparing accuracy of a machine learning model (random forest), deep learning algorithms (CNN, LSTM and Pretrained Transformer) to categorize tweets into cyber bullying classes and  non-cyberbullying classes. 

### Steps to Reproducing the Project

#### Reproducing `cleaning_notebook.ipynb`

Create a repository on Github. See [here](https://docs.github.com/en/get-started/quickstart/create-a-repo) on how to do it

Create a google account.

Navigate to google drive and create a folder named `NLP`.

Download data from [kaggle](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification) on your PC and upload it in the newly created folder `NLP`.

Download the notebook `cleaning_notebook.ipynb` found [here](https://github.com/thayeylolu/cyberbullying/blob/main/notebooks/cleaning_notebook.ipynb) on your PC. Navigate to `File>Upload notebook`. Navigate to the location of the downloaded notebook `cleaning_notebook.ipynb` then upload it

Create a new cell in the begining of the notebook

Install the list of packages used to create the project by copying the code below on the cell in colab. The `requirements.txt` file can be found here : [link](https://github.com/thayeylolu/cyberbullying/blob/main/requirements.txt). Download it from github to your local PC, then upload it to colab as a file.
```python
!pip install -r requirements.txt
```
After copying the command, navigate to `Runtime>Run all`.

After all the cells in the notebook have been executed, download the two files `clean_df.cv` and 'train_data.csv` on your local PC. Upload the two files to your created `NLP` folder in google drive.

On colab, Navigate to `File>Save a copy on Github`. A pop up appears. On the pop-up,  select the name of the github repositiory you created earlier.

Add `notebooks/` to the begining of file path. Then, click ok.This saves your file to github.

#### Reproducing `eda.ipynb`

Download the notebook `eda.ipynb` found [here](https://github.com/thayeylolu/cyberbullying/blob/main/notebooks/eda.ipynb) on your PC. Navigate to `File>Upload notebook`. Navigate to the location of the downloaded notebook `eda.ipynb` then upload it. 

Create a new cell in the begining of the notebook

Install the list of packages used to create the project by copying the code below on the cell in colab. The `requirements.txt` file can be found here : [link](https://github.com/thayeylolu/cyberbullying/blob/main/requirements.txt). Upload it to colab as a file again.
```python
!pip install -r requirements.txt
```
After copying the command, navigate to `Runtime>Run all`.

On colab, Navigate to `File>Save a copy on Github`. A pop up appears. On the pop-up,  select the name of the github repositiory you created earlier.

Add `notebooks/` to the begining of file path. Then, click ok.This saves your file to github.

#### Reproducing `CountVectorizer_random forest.ipynb`
Download the notebook `CountVectorizer_random forest.ipynb` found [here](https://github.com/thayeylolu/cyberbullying/blob/main/notebooks/CountVectorizer_random%20forest.ipynb) on your PC. Navigate to `File>Upload notebook`. Navigate to the location of the downloaded notebook `CountVectorizer_random forest.ipynb` then upload it.

Create a new cell in the begining of the notebook.

Install the list of packages used to create the project by copying the code below on the cell in colab. The `requirements.txt` file can be found here : [link](https://github.com/thayeylolu/cyberbullying/blob/main/requirements.txt).Upload it to colab as a file again.
```python
!pip install -r requirements.txt
```
After copying the command, navigate to `Runtime>Run all`.

On colab, Navigate to `File>Save a copy on Github`. A pop up appears. On the pop-up,  select the name of the github repositiory you created earlier.

Add `notebooks/` to the begining of file path. Then, click ok.This saves your file to github.

#### Reproducing `the_multiclass_text_classification_pytorch.ipynb`
Download the notebook `the_multiclass_text_classification_pytorch.ipynb` found [here](https://github.com/thayeylolu/cyberbullying/blob/main/notebooks/the_multiclass_text_classification_pytorch.ipynb) on your PC. Navigate to `File>Upload notebook`. Navigate to the location of the downloaded notebook `CountVectorizer_random forest.ipynb` then upload it.

Create a new cell in the begining of the notebook.

Install the list of packages used to create the project by copying the code below on the cell in colab. The `requirements.txt` file can be found here : [link](https://github.com/thayeylolu/cyberbullying/blob/main/requirements.txt).Upload it to colab as a file again.
```python
!pip install -r requirements.txt
```
After copying the command, navigate to `Runtime>Run all`.

On colab, Navigate to `File>Save a copy on Github`. A pop up appears. On the pop-up,  select the name of the github repositiory you created earlier.

Add `notebooks/` to the begining of file path. Then, click ok.This saves your file to github.

Navigate to `Runtime>Change runtime type` select GPU as the hardware accelerator


