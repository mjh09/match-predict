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

            Lets start with the majority classifier. This can be helpful in determining how effective
            the classifier is. PLayer A won roughly 63 percent of the time. The model should do better than that.

            """
        ),
        html.Img(src='/assets/newBL.PNG', style={'width':'25%','hieght':'25%'}),
        dcc.Markdown(
            """

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