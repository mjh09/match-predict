import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load
from ipywidgets import interact, fixed
from app import app

app_model = load('assets/alig_predict_app_model.joblib')
X_test = load('assets/X_test.joblib')
y_test = load('assets/y_test.joblib')
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
        
            ## Predict StarCraft2 match results
            This app can help you predict the outcome of a 1v1 SC2 match. 

            You can follow your favorite player and watch them crush the odds.

            If gambling is your thing, you can use this as a resource to adjust your betting strategy and maximize returns.

            Or, you can simply create your own values for the model and see the predicted outcome.
            
            Don't forget to check out the Process and Results page to discover what's going on behind the scenes!

            """
        ),
        dcc.Link(dbc.Button('Start Predicting!', color='primary'), href='/predictions')
    ],
    md=4,
)

y_pred_proba = app_model.predict_proba(X_test)[:, 1]

def set_threshold(y_true, y_pred_proba, threshold=0.5):
    class_0, class_1 = unique_labels(y_true)
    y_pred = np.full_like(y_true, fill_value=class_0)
    y_pred[y_pred_proba > threshold] = class_1
    
    ax = sns.distplot(y_pred_proba)
    ax.axvline(threshold, color='red')
    plt.title('Distribution of predicted probabilities')

interact(set_threshold, 
         y_true=fixed(y_test), 
         y_pred_proba=fixed(y_pred_proba), 
         threshold=(0,1,0.05));


column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])