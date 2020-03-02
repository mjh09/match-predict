# Match Predict
Making win/loss predictions from [Aligulac's](http://aligulac.com/) dataset<br/>
<br/>
## App delpoyed at [Heroku](https://sc2predict.herokuapp.com/) 
<br/>
## Tech Stack: 
Python <br/>
Pandas<br/>
Scikit-Learn<br/>
XGBoost<br/>
Dash<br/>
<br/>
## Notebook(s):
[ipynb notebook](https://github.com/mjh09/match-predict/blob/master/notebooks/alig_predict.ipynb)<br/>
<br/>
## The Data:
Trimmed to include games from the start of LOTV expansion to date of database dump(June 2019)<br/>
Reshaped to aggregate wanted stats<br/>
Train/Test split at 75/25<br/>
<br/>
## The Model:
XGBoost Classification algorithm<br/>
Hyper-Parameterized with scikit-learns's RandomizedSearchCV<br/>
Features decided via permutation importance<br/>
Evaluted with the accuracy scoring metric<br/>
<br/>
## Front-End:
Boilerplate Dash framework<br/>
