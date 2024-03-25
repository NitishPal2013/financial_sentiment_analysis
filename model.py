from transformers import BertTokenizer
import numpy as np
import tensorflow as tf


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = tf.saved_model.load('fine_tuned_model')
prediction_func = model.signatures['serving_default']