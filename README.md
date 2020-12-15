# LoL-Game-Predictor-and-Improver

By Hubert Ye & Caitlin-Dawn Sangcap

Final Project for CSCI 353
 
## Description

The purpose of our project is to see how much of the champion selection comes into play in deciding which team will be the victor. 

Then using that information, implement a recommendation system, to help a team choose their champions depending on what has been chosen and banned.

## Algorithms

For the predictor, we are using k-Nearest Neighbors and Logistic Regression

For the recommender, we are using Genetic Algorithm and Collaborative Filtering using SVD

## Dataset

We will be building the following datasets ourselves using the Riot API:

### For the predictors:

We gathered 2825 ranked game information of the top league of legends players. Each one contains the champions used by each team and whether the team won or lost.

### For the recommenders:

For the Collaborative Filtering, we gathered 1167 account ID from the top of the North American leaderboard during the month of December 2020 with their mastery points for each champion normalized to a whole number between 0 and 100.

For the Genetic Algorithm, we got the official champion documentation from the Riot API to get all the base statistics of a champion. Using that information, teams would be generated at random and then passed to the genetic algorithm and attempt to create the best team for a specific strategy (hard engage, team fight and poke).

## Conclusion

Comparing the predictors, the result appears to be no better than random guessing using the both algorithms. Further testing with an alternative training set is required to see if improvements can be made.

For collaborative filtering, the recommended champions appear to be biased towards half the pool of champions. Further training and testing data is required to find the actual distribution. 

For the genetic algorithm, the fitness of the recommended teams was generally above 80% with the exception of the poke strategy. A bug occurred and the fitness for any team under the “Poke” strategy is given a fitness value of zero. Due to missing information and data from Costa, L.’s original work, not all functions could be replicated. Further testing and information is needed to make a better team composition.

## How to Use

The respective algorithms are stored in their respective folders and can be viewed via the jupyter notebook, using each program in order. However, using the notebook for Collaborative Filtering requires a working Riot API key.

The programs used to gather the data are the .py files and require a working Riot API key to be edited into the program.
