import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            
            #### Get the Data
            To start with, we have to gather the data. If you would like to do this yourself,
            head on over to [Aligulac](http://aligulac.com/about/db/) to find out how!(all credit to them for hosting the data)
            My process involved downloading the dump file and restoring it to a local PostgreSQL database.
            From there, it's as simple as exporting to a csv file. The tables used here are the rating table and match table.
            
            #### Read-in and organize the data
            For this, the pandas library in python can handle it easily. I chose to filter the data by matches played 
            in the Legacy of the Void expansion of StarCraft2, i.e., the latest iteration. This filter was chosen to minimize 
            the model size and better represent the most recent results. There is much more data to use if you are so inclined!

            Given that the match table doesn't have a column for who won, only the score for the series, I made a new column 
            to represent the winner. From there, the data was split by player, A & B, then both merged with the rating table 
            on player ID. I then merged the tables back together and again to the match table on ID. I encoded the race columns
            to numeric representations: 1 to 4. This potentially isn't necessary if you'd rather use a specific encoder in your 
            pipeline, or if the model has a built-in to deal with categoricals.

            The end goal here for me was to have the race, ratings, and match results for each match and player represented.

            #### Decide what we are predicting
            The new column, `winning_player`, is now populated with which player won: A or B. Therefore, this will be a classification
            prediction since we are trying to predict who won.

            #### Start with a baseline!
            This is pretty important! For a classification model especially, knowing your majority classification value
            can help you infer how well your model is doing. We can see that in this data set, _*in Results*_, about 63 percent of the time
            player A wins. So if the model does roughly the same, then it's only as good as guessing player A every
            time. In other words, the model is near useless.

            #### Split the data for training and testing.
            Scikit-learn has a package that can do this easily. I chose to stratify across the `winning_player` category
            so that both samples had near equal representation of the category. This can help the accuracy of the model
            with imbalanced class representation.

            #### Feature matrix and Target vector
            We split the target from the features in both train and test so that the model does not learn the actual value 
            it is trying to predict from the sample. Doing so helps the model generalize to unseen data. In our case, since we 
            are predicting who won, the target is represented by the `winning_player` column and the rest we can use for features
            to train and predict from.

            #### Choose a model and decide on hyper-parameters
            I used XGBoost's classifer model. There was no particular reason why, other than it tends to perform 
            well compared to other tree based models in my experience. The parameters for this model were chosen via scikit-learn's 
            `RandomizedSearchCV()` function. This allows the user to decided on a range of parameter values to try, and outputs
            the best values based on a scoring metric. In this case, accuracy was used.

            #### Model metrics
            After the model has been fit to the training data, we can look at how well it's doing. This can be done using
            the models built in `predict()` function with the unseen test feature matrix. The predicted classification values
            can then be compared to the actual target values from the test data. 
            
            For a classification problem, recall and precision of the model's predictions can be a solid metric. Precision is the
            amount of times the model predicted a value correctly, and recall refers to how much of the true category was captured.
            I used scikit-learn's `classification_report()` function to see the results. These scores can be combined into what's called
            an f1 score, which is the average of both. 0 being the worst score, 1 being the absolute best. Cross validation can then
            be performed to ensure that the results are not due to mere chance.

            """
        ),

    ],
)

layout = dbc.Row([column1])