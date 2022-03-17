import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

#text preprocessor
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#load model
loaded_model = load_model("models/LSTM_classifier_V1/")

## Site Functions

def predict_hard(text):
    ''' 
    Best used one headline at a time
    '''
    
    sequence = tokenizer.texts_to_sequences(text)
    sequence = pad_sequences(sequence, maxlen=22) ###why is this??
    prediction = loaded_model.predict(sequence)
    
    return print(prediction)


predict_hard(["Russia moves to seize hundreds of planes from foreign owners."])