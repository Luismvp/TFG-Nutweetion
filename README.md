#Nutweetion

Food  and  nutrition  in  general  are  important  aspects  of everybody’s life. The way you eat determines how you feel, 
what illnesses you might suffer in the future and it even talks about your social background.

In this study, we use Twitter as a source of nutritional information, capturing tweets that talk about food. The goals of this
project are designing and developing a tool capable of performing nutritional analysis over the population, as well as developing a classifier that distinguishes between healthy and unhealthy dishes. 

The project consists of the following stages: capture, classifier development and nutrition analysis system building.


In the first stage we collected tweets 19773 in Spanish and Catalan containing meta data such as geographic locations and user names, and conformed a corpus for our research.

In the second stage we built a system to preprocess these tweets transforming them into a source of information for predictive models and visualizations. With that purpose we extracted features as nutrients contained by the food mentioned in those tweets. This features were used as input for different classifiers which were evaluated using various metrics.

The classifier had to determine if the food mentioned in the tweet was healthy or not. The classifier that gave the best performance was the one implemented with the K Nearest Neighbors algorithm, reaching an accuracy and f1-score of 0,93 and 0,93 respectively.

In the final stage we developed a nutrition analysis service that allows you to visualize the analysis of the nutrition of a certain population being capable of filtering the tweets between Autonomous Communities, gender, the health label given by the classifier and the hour of creation.

In this repository there are available two folders.

One that includes the code related to the dataset capture preprocessing and feature extraction as well as the classifier. 
This code is written in jupyter notebooks so everybody can learn the process followed.

The other folder contains the code of the visualization system used to analyze nutrition in a glance.
