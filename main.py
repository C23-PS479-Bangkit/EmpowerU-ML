from fastapi import FastAPI
import uvicorn
import pickle
import tensorflow as tf
from transformers import BertTokenizer
from fastapi.responses import JSONResponse
import numpy as np

from pydantic import BaseModel


class Comment(BaseModel):
    comment: str

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {"model" : "Sentiment Analysis"}

@app.post('/predict')
async def predict(comment: Comment):
    # tokenize comments using IndoBERT tokenizer
    tokens = bert_tokenizer([str(comment)], truncation=True, max_length=100, padding=True, return_tensors="tf")
    tokenized_input = tokens.input_ids.numpy()

    # prediction
    input_data = tokenized_input[0]
    input_data = input_data.reshape(1, -1)
    if input_data.shape[1] < 100:
        # padding if text data too short
        padding = np.zeros((1, 100 - input_data.shape[1]), dtype=np.int32)
        input_data = np.concatenate([input_data, padding], axis=1)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    result = output_data[0][0]

    # return result
    result = int(result > 0.5)
    return {"impression" : result}


@app.on_event("startup")
async def startup():
    # Load the TFLite model
    global interpreter
    interpreter = tf.lite.Interpreter(model_path="./model/model.tflite")
    interpreter.allocate_tensors()

    # Download the IndoBERT tokenizer
    global bert_tokenizer
    bert_tokenizer = BertTokenizer.from_pretrained('cahya/bert-base-indonesian-522M')

    # Get the input and output details
    global input_details
    global output_details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()


if __name__ == "__main__":
    uvicorn.run(app, on_startup=startup)