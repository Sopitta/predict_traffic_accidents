# Import libraries
import numpy as np
from flask import Flask, request
from flask_restful import Api, Resource
import pickle


#Load the model
model = pickle.load(open('model.pkl','rb'))
#load the encoder
enc = pickle.load(open('encoder.pickle','rb'))

app = Flask(__name__)
api = Api(app)

#@app.route('/api',methods=['POST'])
class PredictValue(Resource):
    def get(self):
        # get request : returns the JSON format for API request
        return {"JSON data format": {'Category':'Alkoholunfälle','Type':'insgesamt','Year':'2021','Month':'01'}}
    def post(self):
        # Get the data from the POST request.
        data = request.get_json(force=True)
        try:
            cat = data['Category']
            type = data['Type']
            year = int(data['Year']) - 2000
            month = int(data['Month'])
            
            #create array from Category and Type
            arr_ct = enc.transform(np.array([cat,type]).reshape(-1,2)).toarray()
            #create array from Year and Month
            arr_ym = np.array([year,month]).reshape(-1,2)
            #create array for prediction
            data_in = np.concatenate([arr_ct,arr_ym],axis = 1)
            

            prediction = np.floor(model.predict(data_in))
            output = {'prediction': prediction[0]}
            return output
        except:
            return {"Use thus JSON format": {'Category':'Alkoholunfälle','Type':'insgesamt','Year':'2021','Month':'01'}}
        

api.add_resource(PredictValue, '/')
# comment for deploying/uncomment when testing locally
#if __name__ == '__main__':
#    app.run(debug=True)