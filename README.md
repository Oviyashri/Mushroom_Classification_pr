# Mushroom Classification
The Audubon Society Field Guide to North American Mushrooms contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy. The main goal is to predict which mushroom is poisonous & which is edible.

## About Dataset
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.

URL: https://www.kaggle.com/uciml/mushroom-classification

## Approach
**Data Description:**

We will be using Mushroom Prediction Data Set present in Kaggle  Repository. This Data set is satisfying our data requirement. Total 8120 instances present in different batches of data. 

**Data Splitting:**

We split the data here for our train and test data for further uses.

**Data Preprocessing:**

We will be exploring our data set here and perform data preprocessing depending on the data set. We first explore our data set in Jupyter Notebook and decide what pre-processing and validation we have to convert all those to numerical values by label encoding and then we have to write separate modules according to our analysis, so that we can implement that for training as well as prediction data.
	
**Model Training:**

We trained various model in our notebook and SVC was good on it. We trained with our processed data.

**Model Evaluation:**

Model evaluation done by classification and report was saved.

**Model Saving:**

We will save our models so that we can use them for prediction purpose. 

**Push to app:**

Here we will do cloud setup for model deployment. We also create our streamlit app and user interface and integrate our model with streamlit app and UI.

**Data from client side for prediction purpose:**

Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side. 

**Data processing:**

Client data will also go along the same process Data pre-processing and according to that we will predict those data.

**Export Prediction to CSV:**

Finally when we get all the prediction for client data, then our final task is to export prediction to csv file and hand over it to client. 

## Web Deployment
Mushroom Classification Web App: https://mushrooms-prediction-api.herokuapp.com

## Screenshots
## UI:
![1](https://user-images.githubusercontent.com/92749977/155966428-2f76d818-175b-46c4-8076-4e86e0ac0499.jpg)

## Prediction
![4](https://user-images.githubusercontent.com/92749977/155973037-35997ceb-6d15-47e4-99cc-9437bd7e03e5.jpg)

## Project Documents

## High Level Design 

URL: https://drive.google.com/file/d/1ycIXy5C-phpsdnSUPOVa5reipHLX8DMQ/view?usp=sharing

## Low Level Design

URL: https://drive.google.com/file/d/1KI-HObtzjQ3b_nT0cQLGUG9RBycaNC2O/view?usp=sharing

## Architecture

URL: https://drive.google.com/file/d/1Oq0VZPdqubsr58CTklx0kEDOorl1Zyz-/view?usp=sharing

## Detailed Project Report

URL: https://drive.google.com/file/d/1pJ0TXhnTd1oTUK2I3f6lABgLDJtVLCaL/view?usp=sharing

## Wireframe

URL: https://drive.google.com/file/d/1sHfHHWeXKSWucoBYrOdSry9mrsCCwNFd/view?usp=sharing

## Demo Video

URL: https://drive.google.com/file/d/1kS3CS4udq70z_7JobRU6cR1LvMhLgTUD/view?usp=sharing

https://user-images.githubusercontent.com/92749977/156380212-d77ac684-46a1-4102-9f5e-8f6b91f91812.mp4

## Author

Oviyashri B [LinkedIn](https://www.linkedin.com/in/oviyashri-balasubramaniam)

