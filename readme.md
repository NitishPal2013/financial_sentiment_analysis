## Financial News Sentiment Analysis

This is a Machine learning Neural Network which uses Transformers based, very popular model BERT, as the middle layer which performs text classification. This Model takes a sentence / financial news and predict its sentiment as negative, postive or neutral.

### Dataset Link:

I used open source available Dataset [financial_phrasebank](https://huggingface.co/datasets/financial_phrasebank)

## Project setup

This project can easily be setup with appropriate environment.

I have trained my model with my own small GPU in my local environment. This results in not so good predictions, but yes, with enough text data and more computation power, It can easily break the barriers. 

Run the Fin_news_sentiment_analysis.ipynb file in colab or any other platform.

req.txt file contains modules with their appropriate versions which can make you notebook run without any errors.

Below is the list of some important modules, their versions and useful links to setup things.

tensorflow==2.10.1

transformers==4.39.0

It will install both tensorflows cpu and gpu module.

#### Tensorflow installation

Read carefully this official page of installation: [install tensorflow with pip](https://www.tensorflow.org/install/pip)

You can also setup the latest environment if you use docker [insatll tensorflow with docker](https://www.tensorflow.org/install/docker)

#### Transformers installation

```
pip install transformers
```

### Docker setup.

* Fork this repo and then clone it.
```
git clone <REPO_URL>
``` 
* Then run the .ipynb file which will create a folder name `fine_tuned_model`. This folder will save the essential files of your model to rebuild it.

* Open the project folder in terminal.

* build the docker image by
```
docker build -t fin_sent .

```

* And after completing this setup you will be having a running model in a docker container. This can easily be upload to any cloud platform.

#### NOTE: This model is serving as fastapi server. Please feel free to make changes in the `main.py` to add additional features. To Test things out, go to `'/docs'` route of the model url . FastAPI provide a very productive UI for testing api and for the relevant docs.