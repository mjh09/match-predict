import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load

from app import app


app_df = load('assets/app_df.joblib')

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Predict StarCraft2 match results







            #### This app can help you predict the outcome of a 1v1 SC2 match. 






            #### You can follow your favorite player and watch them crush the odds.






            #### If gambling is your thing, you can use this as a resource to adjust your betting strategy and maximize returns.






            #### Or, you can simply create your own values for the model and see the predicted outcome.






            #### Take note of the graph distributions for predicting!






            ####  Don't forget to check out the Process and Results page to discover what's going on behind the scenes!

            """
        ),
        dcc.Link(dbc.Button('Start Predicting!', color='primary'), href='/predictions')
    ],
    md=4,
)


fig = px.scatter(app_df, x="player_a_sRating", y="player_a_rating", color="player_a_race",)

fig2 =px.scatter(app_df,x="player_b_sRating", y="player_b_rating", color='player_b_race',)



column2 = dbc.Col(
    [
        dcc.Markdown("## Player A rating correlation"),
    
        dcc.Graph(figure=fig),

        dcc.Markdown("## Player B rating correlation"),

        dcc.Graph(figure=fig2),
        
    ]
)

layout = dbc.Row([column1, column2])