# Match Predict
Making win/loss predictions from [Aligulac's](http://aligulac.com/) dataset

#### App delpoyed at [Heroku](https://sc2predict.herokuapp.com/) <br>

#### Tech Stack: <br/>
Python
Pandas
Scikit-Learn
XGBoost
Dash
#### Notebook(s)
[ipynb notebook](https://github.com/mjh09/match-predict/blob/master/notebooks/alig_predict.ipynb)

#### The Data
Trimmed to include games from the start of LOTV expansion to date of database dump(June 2019)
Reshaped to aggregate wanted stats
Train/Test split at 75/25

#### The Model
XGBoost Classification algorithm
Hyper-Parameterized with scikit-learns's RandomizedSearchCV
Features decided via permutation importance
Evaluted with the accuracy scoring metric

#### Front-End
Boilerplate Dash framework
