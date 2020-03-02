# Match Predict
Making win/loss predictions from [Aligulac's](http://aligulac.com/) dataset<br/>
<br/>
### App delpoyed at [Heroku](https://sc2predict.herokuapp.com/) <br>
<br/>
### Tech Stack: <br/>
Python <br/>
Pandas<br/>
Scikit-Learn<br/>
XGBoost<br/>
Dash<br/>
<br/>
### Notebook(s):<br/>
[ipynb notebook](https://github.com/mjh09/match-predict/blob/master/notebooks/alig_predict.ipynb)<br/>
<br/>
#### The Data:<br/>
Trimmed to include games from the start of LOTV expansion to date of database dump(June 2019)<br/>
Reshaped to aggregate wanted stats<br/>
Train/Test split at 75/25<br/>
<br/>
#### The Model:<br/>
XGBoost Classification algorithm<br/>
Hyper-Parameterized with scikit-learns's RandomizedSearchCV<br/>
Features decided via permutation importance<br/>
Evaluted with the accuracy scoring metric<br/>
<br/>
#### Front-End:<br/>
Boilerplate Dash framework<br/>
