import streamlit as st
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
    sequence = pad_sequences(sequence, maxlen=22)
    prediction = loaded_model.predict(sequence)
    
    return st.write(prediction)




#-----------------------
# Site Design
#-----------------------

st.title('Are we living in the twilight zone? Have the worlds of the onion and real journalism coverged?')
st.write("Let's find out my testing out a real headline.")

user_input = st.text_input("add headline....")

if st.button("Predict your headline!"):
    with st.spinner("computin...."):
        st.write(f'User input is: {str(user_input)}')
        predict_hard([str(user_input)])
        






