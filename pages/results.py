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
        
            ## Results

            Lets start with the **majority classifier**. This can be helpful in determining how effective
            the classifier is. Player A won roughly 63 percent of the time. The model should do better than that.

            """
        ),
        html.Img(src='/assets/newBL.PNG', style={'width':'25%',}),
        dcc.Markdown(
            """
            After training the model we can get the score from both the training set and test set.
            The **test score** can show us how well the model is generalizing to new data.     
            """
        ),
        html.Img(src='/assets/newscore.PNG', style={'width':'30%',}),
        dcc.Markdown(
            """
            Not bad, almost 82 percent accuracy. The model has given us a near *20 percent* increase from
            the baseline. Lets see how it's doing on **precision and recall**. See the Process page for an eli5 on these metrics.
            Or check [here](https://en.wikipedia.org/wiki/Precision_and_recall).
            """
        ),
        html.Img(src='assets/classreport.PNG', style={'width':'40%'}),
        dcc.Markdown(
            """
            It seems to be doing mariginally better with the majority class. Maybe because there was more instances 
            to learn from? Next, we'll take a look at **feature importances** and see if we can discover what is moving 
            the needle for the model. I'll decode some of the meaning after.
            """
        ),
        html.Img(src='assets/featureimportance.PNG', style={'width':'60%'}),
        dcc.Markdown(
            """
            You'll have to excuse me for the wonky column names. I'll explain. The top two are the smoothed rating
            for player A & B. As I understand it, smoothing is a statistical technique used to reduce the effect of
            noise in data. In other words, it helps models generalize by minimizing the effects of outliers and skewed data.
            I haven't taken the time to reverse engineer the values, so you'll have to make due with that explanation.
            [Here](https://en.wikipedia.org/wiki/Smoothing) is a wikipedia page that explains it better, albiet more technical.

            Moving on. `player_<x>_rating` is thier current rating. I believe this to be an average of their rating vs.
            all other races. As you can see, player A & B's smoothed rating and current rating are toping the chart.
            This is partly responsible for my decisioon to use them in the prediction page. 
            
            I should also explain the suffixes.
            Except for the four ratings I manually changed to A & B, all other columns have had a suffix added via the default
            merge function from pandas for handling identical column names. Player A's info has an `_x` added, and player B
            `_y`. Also, the `_vz` `_vp` `_vt` are vs. race respectively. Okay, now that we've de-mystified some of the columns names, 
            we should have a look at **permutation importances**. 
            """
        ),
        html.Img(src='assets/permimp.PNG', style={'width':'30%'}),
        dcc.Markdown(
            """
            This image was created using the `eli5` package for python. **Permutation importance** is decided by shuffling
            the data for each column one at a time and re-scoring to see the effect. Through this method, the model can 
            decide which features are the most important by which columns alter the scoring metric the most. This makes sense
            because if the column's values had a direct effect on the outcome, shuffling them would have a noticable effect. Conversely, if the
            column's values mattered naught to the model, shuffling them would have a negligible effect. Again, we see the four ratings 
            from the predictions page topping the chart here.

            That's all I have for you today. Again, credit to [Aligulac](http://aligulac.com) for hosting the data. The notebook
            for this model can be found in my github repo link below. Feel free to give it a look and see if you can do better!
            This model certainly has room for improvement.

            I'd love to hear back about any criticisms, advice, or questions about the project.
            """
        ),
    ],
    md=10,
)


column2 = dbc.Col(
    [
       
    ]
)

layout = dbc.Row([column1])