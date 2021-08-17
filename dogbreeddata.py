
import plotly.express as px
import pandas as pd

dogbreed_df = pd.read_csv('datasets/dogbreeds.csv')

fig = px.bar(data_frame = dogbreed_df, 
        x = dogbreed_df['BREED'], 
        y = dogbreed_df['LICENSE'], 
        color = 'BREED',
            labels = {
                'BREED': 'Dog Breed',
                'LICENSE': 'Number of Licenses'})

fig.update_layout(
    title={
        'text': "Licenses by Breed in Calgary",
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})




fig.show()


