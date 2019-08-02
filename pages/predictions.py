import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from joblib import load
import pandas as pd

app_model = load('assets/alig_predict_app_model.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-6'),
        dcc.Markdown(
            """
            The outcome is produced in real-time from a trained classifaction model using gradient-boosted trees.
            Features here were chosen from the model via permutation importance. Sliders scale by 0.1 per minor tick. 
            Typical matches involve players of near ratings. Anything but will almost certainly result in the highest
            rated player winning. 
            
            Download the data from [Aligulac](http://aligulac.com/db/about/), find your favorite
            player's ratings, and test them against another! __*Disclaimer*__: it's a bit more involed. See how I did it in the
            Process page. **Credit** to Aligulac for hosting the data from which this was produced. The full model can be
            found in my github repo linked below.
            """
        ),
        dcc.Markdown(
            """
            #### Army Race

            """
        ),
        dcc.Markdown('Player A'),
        dcc.Dropdown(
            id='player_a_race',
            options = [
                {'label': 'Random', 'value': 4},
                {'label': 'Protoss', 'value': 3},
                {'label': 'Terran', 'value': 2},
                {'label': 'Zerg', 'value': 1}
            ],
            value = 4,
            className='mb-4',
        ),
        dcc.Markdown('Player B'),
        dcc.Dropdown(
            id='player_b_race',
            options = [
                {'label': 'Random', 'value': 4},
                {'label': 'Protoss', 'value': 3},
                {'label': 'Terran', 'value': 2},
                {'label': 'Zerg', 'value': 1}
            ],
            value = 4,
            className='mb-4',
        ),
        dcc.Markdown(
            """
            #### Smoothed Rating

            """
        ),
        dcc.Markdown('Player A'),
        dcc.Slider(
            id='player_a_sRating',
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,3,1)},
            className='mb-4',
        ),
        dcc.Markdown('Player B'),
        dcc.Slider(
            id='player_b_sRating',
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,3,1)},
            className='mb-4',
        ),
        dcc.Markdown(
            """
            #### Current Rating
            """
        ),
        dcc.Markdown('Player A'),
        dcc.Slider(
            id='player_a_rating',
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,3,1)},
            className='mb-4',
        ),
        dcc.Markdown('Player B'),
        dcc.Slider(
            id='player_b_rating',
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,3,1)},
            className='mb-4',
        ),
    ],
    md=6,
)

column2 = dbc.Col(
    [
       html.H2('Predicted Winner', className='mb-4'),
       html.Div(id='prediction-content', className='lead') 
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('player_a_race', 'value'), Input('player_b_race', 'value'),
     Input('player_a_sRating', 'value'), Input('player_b_sRating', 'value'),
     Input('player_a_rating', 'value'), Input('player_b_rating', 'value')],
)

def predict(player_a_race, player_b_race, player_a_sRating, player_b_sRating, player_a_rating, player_b_rating):
    df = pd.DataFrame(
        columns=['player_a_race', 'player_b_race', 'player_a_sRating', 'player_b_sRating', 'player_a_rating', 'player_b_rating'],
        data=[[player_a_race, player_b_race, player_a_sRating, player_b_sRating, player_a_rating, player_b_rating]],
    )
    y_pred = app_model.predict(df)[0]
    print(f'{y_pred} won!')