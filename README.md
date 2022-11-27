Predicting Types of Cyberbullying from Tweets
==============================

Summary

This project aims to build a predictive model by comparing accuracy of a machine learning model (random forest), deep learning algorithms (CNN, LSTM and Pretrained Transformer) to categorize tweets into cyber bullying classes and  non-cyberbullying classes. 

Steps to Reproducing the Project

Create a google account.

Navigate to google drive and create a folder named `NLP`.

Download data from [kaggle](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification) on your PC and upload it in the newly created folder `NLP`.

Download the notebook `cleaning_notebook.ipynb` on your PC. Navigate to `File>Upload notebook`. Navigate to the location of the downloaded notebook `cleaning_notebook.ipynb` then upload it

Create a new cell in the begining of the notebook

Install the list of packages used to create the project by copying the code below on the cell in colab. The `requirements.txt` file can be found here : [link](https://github.com/thayeylolu/cyberbullying/blob/main/requirements.txt). Download it form github, then upload it to colab as a file.
```python
!pip install -r requirements.txt
```
After copying the command, navigate to `Runtime>Run all`

Navigate to `Runtime>Change runtime type>` select GPU as the hardware accelerator


