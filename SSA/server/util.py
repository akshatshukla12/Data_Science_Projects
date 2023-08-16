from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import sklearn
import pickle
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

__model = None
__score = None
__df = None
__df1 = None
__avgscore = None


def get_estimated_sentiments(ticker):
    print('Calculating Sentiments start')
    global __df
    global __df1
    global __avgscore
    global __model
    finviz_url = 'https://finviz.com/quote.ashx?t='
    parsed_data = []
    url = finviz_url + ticker
    req = Request(url=url, headers={'user-agent':'my-app'})
    response = urlopen(req)
    html = BeautifulSoup(response,'html')
    news_table = html.find(id="news-table")

    for row in news_table.findAll('tr'):
        title = row.a.text
        date_data = row.td.text.strip().split(' ')

        if len(date_data) == 1:
            time = date_data[0]
        else: 
            date = date_data[0]
            time = date_data[1]
        parsed_data.append([ticker,date,time,title])
    
    __df = pd.DataFrame(parsed_data, columns=['ticker','date','time','title'])

    def remove_common_words(text):
        common_words = ['Amazon','Microsoft','META','Oracle','Google','AMD','IBM','Apple']
        words = text.split(' ')
        new_words = [word for word in words if word not in common_words]
        return ' '.join(new_words)

    __df['title'] = __df['title'].apply(lambda x:remove_common_words(x))
    __df['score'] = __df['title'].apply(lambda titles:str(__model.predict([titles])[0]))
    __df['score'] = __df['score'].apply(lambda x:int(x.replace('0','-1')))

    __df1 = __df[['score','date']].groupby('date').mean()['score']

    __avgscore = sum(__df['score'])/len(__df['score'])

    print('Calculating Sentiments done')

    return __df1, __avgscore

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        with open('./artifacts/Sentimental_Analyzer.pickle','rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print("Sentimental Analysis Done")
    print(get_estimated_sentiments('GOOG'))

