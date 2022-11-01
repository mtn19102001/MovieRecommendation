# IT4242E_MovieRSystem

A Movie Recommendation System.

Machine Learning and Data Mining Project **IT4242E**

Class **131082**.

## Notes


In this project, there is a **strictly** order to run the project. Please **run** in the **guided order** so as not to see any error.

## Libraries and Packages use
We use **Anacoda** Environment to install packages, libraries when use on Anacoda.

Working in Google Colaboratory is recommended.

The libraries, packages are :
- `kaggle` important!
- `pandas`
- `numpy`
- `ast` for `literal_eval`
- `sklearn`
- `torchmetrics`
- `torch` known as `pytorch`
- `matplotlib.pyplot`

If you also have Anacoda Environment, use following commands to install libraries missing:
```
pip install <library_name>
# For example: pip install kaggle 
# pip install torch
```
## How to run on VSCode Window

We use **Anacoda** Environment to install packages, libraries.

The files we will work on and also the order to execute is:

- `downloader.ipynb`
- `cleaning_data.ipynb`
- `FeatureExtractor.py`
- `profiles.ipynb`
- `Content_Based.ipynb`
- `recommender.ipynb`
- `Content_Based_Classification.ipynb`
- `recommender_classification.ipynb`

### 1. Download Dataset
Open `downloader.ipynb` and run choose run all. 

If the kaggle key doesn't work any more please download [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) directly from Kaggle and extract to \Dataset folder.

Downloaded files will be in folder `Dataset`
### 2. Cleaning Dataset
Open `Cleaning Data\cleaning_data.ipynb` and run choose run all. 

Cleaned files will be in folder `Dataset\CleanedData`

### 3. Create Profiles for Movies
Open `Profiles\profiles.ipynb` and run choose run all. 

Featured Extracted files will be in folder `Dataset\FeatureExtracted`

### 4. Learning Users' Models
- For A Straight-Forward Regression Model
Open `Machine Learning\Content_Based.ipynb` and run choose run all. 
- For A Classification Models
Open `Machine Learning\Content_Based_Classification.ipynb` and run choose run all. 

Models related files will be in folder `Dataset\ModelStorage`

### 5. Recommend User with Movies
- For A Straight-Forward Regression Model
Open `Machine Learning\recommender.ipynb` and run choose run all. 
- For A Classification Models
Open `Machine Learning\recommender_classification.ipynb` on colab and run choose run all. 

In those ipynb file, there are a variable `user` to specify id of user to recommend for.

`Content_Based.ipynb` and `recommender.ipynb` should be run by pair and so for `Content_Based_Classification.ipynb` and `recommender_classification.ipynb`

## How to run on Google Colab

The files we will work on and also the order to execute is:

- `downloader_colab.ipynb`
- `cleaning_data_colab.ipynb`
- `profiles_colab.ipynb` and `FeatureExtracted.py`
- `Content_Based_Colab.ipynb`
- `recommender_colab.ipynb`
- `Content_Based_Classification_Colab.ipynb`
- `recommender_classification_colab.ipynb`

### 1. Download Dataset
Open `downloader_colab.ipynb` on colab and run choose run all. 

Downloaded files will be in path `/content/drive/MyDrive/MovieRSystem` in your drive

If the kaggle key doesn't work any more please download [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) directly from Kaggle and extract to /content/drive/MyDrive/MovieRSystem folder.

### 2. Cleaning Dataset
Open `Cleaning Data\cleaning_data_colab.ipynb` on colab and run choose run all. 

Cleaned files will be in folder `/content/drive/MyDrive/MovieRSystem/CleanedData`

### 3. Create Profiles for Movies
Open `Profiles\profiles_colab.ipynb` on colab and upload `Profiles\FeatureExtractor.py` file to current directory of colab.

Featured Extracted files will be in folder `/content/drive/MyDrive/MovieRSystem/FeatureExtracted`

### 4. Learning Users' Models
- For A Straight-Forward Regression Model
Open `Machine Learning\Content_Based_Colab.ipynb` on colab and run choose run all. 
- For A Classification Models
Open `Machine Learning\Content_Based_Classification_Colab.ipynb` on colab and run choose run all. 

Models related files will be in folder `/content/drive/MyDrive/MovieRSystem/ModelStorage`

### 5. Recommend User with Movies

- For A Straight-Forward Regression Model
Open `Machine Learning\recommender_colab.ipynb` on colab and run choose run all. 
- For A Classification Models
Open `Machine Learning\recommender_classification_colab.ipynb` on colab and run choose run all. 

In that ipynb file, there are a variable `user` to specify id of user to recommend for.

`Content_Based_Colab.ipynb` and `recommender_colab.ipynb` should be run by pair and so for `Content_Based_Classification_Colab.ipynb` and `recommender_classification_colab.ipynb`






