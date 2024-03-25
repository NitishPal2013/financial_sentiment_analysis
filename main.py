from fastapi import FastAPI
from model import prediction_func, tokenizer
import numpy as np
from pydantic import BaseModel


class Text(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Application working Perfectly."}


@app.put("/predict")
async def get_prediction(text_body: Text):
        
    label_desc = {
    0:'negative',
    1:'neutral',
    2:'positive'
    }

    text = text_body.text
    
    encoding =  tokenizer.encode_plus(text, max_length=400, truncation=True, padding='max_length', return_tensors='tf')
    
    predictions =  prediction_func(input_ids = encoding['input_ids'], attention_mask = encoding['attention_mask'])["dense_9"].numpy()
    
    prediction = np.argmax(predictions)

    label = label_desc[prediction]
    
    return {'text': text, 'label': label}