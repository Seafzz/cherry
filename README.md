# Cherry Leaves Disease Detection

## Project Overview
This project utilizes machine learning to detect powdery mildew in cherry leaves through a streamlit web application.

## Dataset Information
The dataset is sourced from Kaggle, containing over 4.000 images from healthy leaves and those affected by powdery mildew, a fungal disease.

## Business Requirements
Farmy & Foods faces a challenge with powder mildew on their plantations. The current method of manually checking each tree for the disease is time-consuming and not so scalabe. As employee spends about 30 minutes inspecting each tree and applying a fungicide if needed. With thousand of cherry trees this process is inefficient.

The IT team proposed an ML system that can detect powder mildrew instantly in leaf images.

### Goals
1. Conduct a study to visually differentiate healthy cherry leaves from those with the powdery mildew.
2. Predict whether a cherry leaf is healthy or has powdery mildew.

## Hypothesis and Validation
The hypothesis is that infected leaves show a powdery white layer on their surface. This will be validated by:
- collecting an image dataset from the client
- Creating an image montage for healthy and infected leaves.
- Performing average image analysis

## Mapping Business Requirements to Tasks 
### Requirement 1
- Analysis of average images and variablility images for each class.
- Different between average healthy and powdery mildew-affected leaves.
- an image montage for each class.

## Requirements 2
- An ML system to predict the health of a cherry leaf.
- A dashboard with an image montage prediciton feature.


## machine Learning Business Case
### Business Requirements
The clien needs a tool to indentify healthy leaves from those who with powedery mildew. ML can distinguish between these images if trained to an acceptable level.

### Dashboard or API Endpoint?
The client requires a dashboard.


### Privacy Concerns
The data is provided under an NDA and should be shared only with authorized personnel.

### Project Outcome
The client needs to visually differentiate healthy leaves from infected ones and predict the health status of leaves through the dashboard.

### Model Inputs and Outputs
- Input: Cherry leaf image
- Output: Prediction of leaf health (healthy or powdery mildew)

### Model Criteria
The model should achieve an accuracy of 97%, though it has been trained to 98%.


### Client Benefits
The client will avoid supplying compromised products and can scale up operations by minimizing manual work.

## Dashboard Design
- **Project Summary**: Overview and client requirements.
- **Findings**: Study differentiating healthy and infected leaves.
- **Live Prediction**: Upload images to get health predictions and probability.
- **Hypothesis**: Project hypothesis and validation.
- **Model Performance**: Technical details and performance metrics.


#### Deployment Steps:
1. Log in to Heroku and create an app.
2. Select GitHub as the deployment method.
3. Connect to your repository and deploy the branch.
4. Click "Open App" to access your 

## Credits
- Data modeling and visualization by Code Institute lessons. 
- Code along lessons with by Code insititute lessons.
- co-pilot for help with debuging when necesary.

## Acknowledgements
Thanks to my mentor for the support and guidance.
Fernando Doreto - for the walktrough that made it possible to use quite alot of steps to get through the project.
lots of step will be similar and I have followed alot of the code to take the necessary steps to go through the project.