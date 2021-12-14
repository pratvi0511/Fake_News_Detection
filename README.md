# Fake-News-Detection
This is a project which can detect all types of fake news including ClickBait.

![Python](https://img.shields.io/badge/python%20-%23323330.svg?&style=for-the-badge&logo=python&logoColor=%23F7DF1E) ![Django](https://img.shields.io/badge/flask%20-%23092E20.svg?&style=for-the-badge&logo=flask&logoColor=white) ![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white") 


### Problem Statement
Fake news is fake or misleading information presented as news or say Fake News may be a spread of disinformation and hoaxes through any news platform.The approaching threat of such widespread misinformation is clear.
The two types can be classified as follows:

- Fake-News: are those news stories/articles that are false: the story/article itself is fabricated, with no verifiable facts, sources or quotes.

- Clickbait News: is defined as content whose main purpose is to draw attention and encourage visitors to click on a link to a specific website. 

# Models
## Fake News Model:

## LSTM:
LSTM is a variant of Recurrent Neural Network (RNN) which has a memory cell. It performs better than vanilla RNN on long sequential data. LSTM was designed to overcome the vanishing gradient problem in RNN.

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer.

![Repeating-module](https://miro.medium.com/max/875/0*qvrpDiiTCMKFRQNd)

LSTM cells are composed of several gates like input, output and forget gates to preserve memory to a certain extent. At each timestep, LSTM cell can choose to read, write or reset the cell by using an explicit gating mechanism.

We’ve trained our simple LSTM model on a fake news dataset and got an accuracy of 92.7%.

## ClickBait Model:
For the clickbait model, We worked on 4 different models and the model with highest accuracy was implemented in the website.

## 1. Multinomial Naive Bayes
Naïve Bayes, which is computationally very efficient and easy to implement, is a learning algorithm frequently used in text classification problems. Two event models are commonly used: 
1.Multivariate Bernoulli Event Model
2.Multivariate Event Model

The Multivariate Event model is referred to as Multinomial Naive Bayes.
Naive Bayes is based on Bayes’ theorem, where the adjective Naïve says that features in the dataset are mutually independent.Being relatively robust, easy to implement, fast, and accurate, it is used in many different fields.

Multinomial Naïve Bayes consider a feature vector where a given term represents the number of times it appears or very often i.e. frequency.

The main advantages are:
<br/>
-> Low computation cost.
<br/>
-> It can effectively work with large datasets.
<br/>
-> For small sample sizes, Naive Bayes can outperform the most powerful alternatives.

## 2. Logistic Regression:  
Logistic regression is a classification algorithm used to predict the probability of a target variable. It is a predictive analysis algorithm and based on the concept of probability. 

Logistic Regression uses a more complex cost function as compared to linear regression, this cost function can be defined as the ‘Sigmoid function’.

The sigmoid function maps any real value into another value between 0 and 1. In ML, sigmoid function is used to map predictions to probabilities.The hypothesis of logistic regression tends it to limit the cost function between 0 and 1. 

Hypothesis representation of Logistic Regression :
> hΘ(x) = 1/(1 + e^-(β₀ + β₁X).

## 3.Random Forest
Random forest is a supervised learning algorithm.Random forest can be used for both classification and regression problems, which form the majority of current machine learning systems.

Random forests (RF) are basically a bag containing n Decision Trees (DT) having a different set of hyper-parameters and trained on different subsets of data.

Instead of relying on one decision tree, random forest builds multiple decision trees and merges them together to get a more accurate and stable prediction.  

The detailed Working of Random Forest can be described as below:
The detailed Working of Random Forest can be described as below:
- First, select random samples from a given dataset.
- Then this algorithm will construct a decision tree for every sample. Then it will get the prediction result from every decision tree.
- In the next step, voting will be performed for every predicted result.
- At last, select the most voted prediction result as the final prediction result.
The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting.

## 4. Passive Aggressive model

Passive-Aggressive Algorithms are generally used for large-scale learning. It's one among the few 'online-learning algorithms'. 
It works by responding as passive for proper classifications and responding as aggressive for any miscalculation.

Passive-Aggressive Algorithms are somewhat almost like a Perceptron model, within the sense that they are doing not require a learning rate. However, they are doing include a regularization parameter.

Passive Aggressive Classifier is where you'll train a system incrementally by feeding it instances sequentially, individually, or in small groups called mini-batches and thus, it ​is best for systems that receive data during a continuous stream.

Passive-Aggressive Algorithms are called so because:-
<br/>
--> Passive: If the prediction is correct, keep the model and don't make any changes. i.e., the data within the example isn't enough to cause any changes within the model. 
<br/>
--> Aggressive: If the prediction is wrong/incorrect, make changes to the model. i.e., some change to the model may correct it.

# Accuracy
The Accuracy of the models is as follows:

**LSTM model**
> 92.7%

**Multinomial NB model**
> 96.7%

**Logistic Regression model**
> 94.9%
   
**Random Forest model**
> 92.1%

**Passive Aggressive model**
> 96.1%

**So, For Fake News we used LSTM and for clickbait we used Multinomial NB model as it has the highest accuracy**

## Dataset:
- The clickbait dataset contains, only two attributes: 
    - Tagline: The main heading of the content
    - ClickBait: (0 or 1) weather the given news in clickbaited or not.


- The Fake news articles contains 6 attributes, the main attributes are:
    - Title: Title of the article.
    - Text: Content of the news article
    - Label: Indicates news article is fake or not



# How to Run?

Just run the following commands:
```
$ pip install -r requirements.txt
$ python app.py
```
Just this and you are good to go

# Website

We also made a GUI in the form of the website for the detector. The Backend is made using Flask, whereas the frontend is normal HTML and CSS.

### Fake News Detector
![Fake-News-Detector](./demo_assets/fakenews.jpg)

### Clickbait Detector
![Clickbait-Detector](./demo_assets/clickbait.jpg)

### Short Demo (Please Give it sometime to Load 😃)
![Demo_Video](./demo_assets/demo.gif)


## References
> Dataset and Features: 

- https://www.kaggle.com/c/fake-news/data?select=train.csv (Fake-News-Dataset)
- https://www.kaggle.com/amananandrai/clickbait-dataset (Clickbait Dataset)

> Research Papers:

- For FakeNews:
    - https://www.ijitee.org/wp-content/uploads/papers/v8i11/K18290981119.pdf
    - https://link.springer.com/chapter/10.1007%2F978-981-15-8354-4_26
- For Clickbait:
    - https://link.springer.com/chapter/10.1007/978-3-319-30671-1_72
    - https://cutt.ly/2bdhA9p


# Contribution
For contribtuion please refer to the contribution guideline.

# Future Scope
- Integration of this service in a form of plugin in social media website/apps to prevent spreading of misinformation and changing people views during election.
- Implementing this with Fake Indian Political News so that there is less misinformation.

Happy coding !
