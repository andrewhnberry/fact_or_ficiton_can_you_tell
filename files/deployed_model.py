#Import required plugins
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)
api = Api(app) #Wrapping our app into a REST API framework

#text preprocessor
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#load model
loaded_model = load_model("models/LSTM_classifier_V1/")

class predict(Resource):

    def post(self):
        params = request.get_json()

        #preprocess for model
        sequence = tokenizer.texts_to_sequences(params)
        sequence = pad_sequences(sequence, maxlen=100)
        #predict
        prediction = loaded_model.predict(sequence)

        data = {"text":params,
                "prediction": str(prediction[0])}

        return (jsonify(data))



#Assigning endpoints
api.add_resource(predict, '/predict')

#Run our api
if __name__ == '__main__':
    app.run(debug=True)

