import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from joblib import load
import pandas as pd

model = load('assets/alig_predict_model.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Player A Rating'),
        dcc.Slider(
            id='player_a_sRating'
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,2,1)},
            className='mb-5',
        ),
        dcc.Markdown('#### Player B Rating'),
        dcc.Slider(
            id='player_b_sRating'
            min=-1.1,
            max=2.1,
            step=0.1,
            value=0,
            marks={n: str(n) for n in range(-1,2,1)},
            className='mb-5',
        ),
        dcc.Markdown('#### Player A Race'),
        dcc.Dropdown(
            id='player_a_race',
            options = [
                {'label': 'Random', 'value': '4'},
                {'label': 'Protoss', 'value': '3'},
                {'label': 'Terran', 'value': '2'},
                {'label': 'Zerg', 'value': '1'}
            ],
            value = '4',
            className='mb-5',
        ),
        dcc.Markdown('#### Player B Race'),
        dcc.Dropdown(
            id='player_b_race',
            options = [
                {'label': 'Random', 'value': '4'},
                {'label': 'Protoss', 'value': '3'},
                {'label': 'Terran', 'value': '2'},
                {'label': 'Zerg', 'value': '1'}
            ],
            value = '4',
            className='mb-5',

    ],
    md=4,
)

column2 = dbc.Col(
    [
       html.H2('Predicted Winner', className='mb-5'),
       html.Div(id='prediction-content', className='lead') 
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children')
    [Input('player_a_sRating', 'value'), Input('player_a_race')],
)
def predict(player_a_sRating, player_a_race):
    df = pd.Dataframe(
        columns=['player_a_sRating', 'player_a_race'],
        data=[[player_a_sRating, player_a_race]]
    )
    y_pred = model.predict(df)[0]
    return f'{y_pred: .0f} Wins!'