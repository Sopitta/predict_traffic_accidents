# Predict Traffic Accidents

The project predict number of accidents from Category, Type (of accidents), Year and Month. The data is in traffic_accidents.csv 

## Data processing 

The data processing process can be found at model.ipynb

## Model
Since the predict values are non-negative and discrete. The selected model is a Generalized linear model like the Poisson Regressor.

## End point
the project endpoint is at https://predictaccidents.herokuapp.com/
The post request format is a json body shown below \\
`{'Category':'Alkoholunfälle','Type':'insgesamt','Year':'2021','Month':'01'}` 
