
# Stock Sentimental Analysis

Generally that the sentiment of financial news articles reflects and directs the performance of the stock market. Therefore, by applying Natural Language Processing (NLP) through these headlines, we can see how the positivity/negativity of the score through each day correlate to the stock market's gains/losses.

The objective of this project is to build a machine learning model that can predict the sentiments of the U.S stocks as we are taking the U.S news headlines data. This is a binary classification task where the model will need to predict one of two labels: "1" for positive sentiment, and "0" for negative/neutral sentiment.
## Data Set

Data Set is taken from Kaggle. Data is Scraped from CNBC, the Guardian, and Reuters official websites, the headlines in these datasets reflects the overview of the U.S. economy and stock market every day from 2018 to 2020. 

Link- https://www.kaggle.com/datasets/notlucasp/financial-news-headlines
## Methodology

The methodology for this project will involve the following steps:

Data cleaning and preprocessing Text processing and feature extraction Model selection and training Model evaluation and optimization Conclusion and future work. To tackle the text data, the Natural Language Toolkit (nltk) library in Python will be utilized for text processing and feature extraction. A variety of machine learning algorithms will be trained and evaluated to find the best performing model for this classification task.
## Documentation

[NLTK library](https://www.nltk.org/)

[VADER Sentimental Analysis](https://www.nltk.org/_modules/nltk/sentiment/vader.html)

## Tools & Technology
Text processing is one of the most important part of a Sentimental Analysis project. Here are the tools and techniques used for text processing in this project-

1. Lowercase - This step is important because, in NLP, it's common to convert all words to lowercase before processing the text data to ensure consistency and reduce the size of the vocabulary.

2. Removing punctuation - This step is often performed as part of text preprocessing, as punctuation when attached to any word, will create a problem in differentiating with other words.

3. Removing non-textual data - The purpose of removing non-textual data is to clean and pre-process the text data before further analysis. This step helps to eliminate irrelevant and unnecessary information that may not add value to the analysis.

4. Removing stopwords - The aim of this step is to remove common words that do not carry much meaning, such as "is", "an", "the", etc. These words are called stopwords and are often removed from the text data before further processing. By removing stopwords, we can reduce the dimensionality of the data and focus on the words that carry more meaning.

5. Stemming - A technique that takes the word to its root form. It just removes suffixes from the words. The stemmed word might not be part of the dictionary, i.e it will not necessarily give meaning.

6. lemmatizing - Lemmatization, reduces words to their base form using morphological analysis, which results in a meaningful word. For example, the word "running" may be reduced to "run". Lemmatization is more accurate but slower and more resource-intensive compared to stemming.

Python nltk library is used for most of the text processing work. 
1. From nltk.tokenize Import word_tokenize- For word tokenization.
2. From nltk.corpus Import stopwords- To remove common words. 
3. From nltk.stem Import PorterStemmer- For Stemming.
4. From nltk.stem Import WordNetLemmatizer- For Lemmatization.
## User Interface

![App Screenshot](https://github.com/akshatshukla12/ML_Projects/blob/SSA/SSA.png?raw=true)


## Working

Web Interface  - The user will select the Company from the provided list.

Rest API- The name of the company selected from the user interface is a Ticker which will be used by our backend server to scrap data. The ticker will go to the backend server through an rest API using reverse proxy setting in our Nginx web server.

Web Scrapping- The backend flask server will scrap the latest news headlines about the company from the finviz website. Extracting the news heablines and structuring it into a dataframe for further analysis.

Data Analysis- The backend flask server will predict the sentiment for all the news headlines using our model (1 for positive/ -1 for negative) and it will group by the sentiment per day.

Results - Model will outpot a bar graph of sentiment along with the average(overall) sentiment of the company which will be displayed in the results page.
## API Reference

#### Predict Sentiments

```http
  GET /api/predict_sentiment
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

To get the predicted sentiment of the text from our model.




## Deployment

To deploy this project run the following

Install Python Virtualenv

```bash
  sudo apt-get update
  sudo apt-get install python3-venv
```
Create directory

```bash
  mkdir SSA
  cd SSA
```

Create the virtual environment
```bash
  python3 -m venv venv
  source venv/bin/activate
```
Install Requirment
```bash
  pip install requirment.txt
```
Run Gunicorn:
```bash
  gunicorn -b 0.0.0.0:8000 server:app 
```
Gunicorn is running (Ctrl + C to exit gunicorn)!

Use systemd to manage Gunicorn Systemd is a boot manager for Linux. We are using it to restart gunicorn if the EC2 restarts or reboots for some reason. We create a .service file in the /etc/systemd/system folder, and specify what would happen to gunicorn when the system reboots. We will be adding 3 parts to systemd Unit file — Unit, Service, Install

Unit — This section is for description about the project and some dependencies Service — To specify user/group we want to run this service after. Also some information about the executables and the commands. Install — tells systemd at which moment during boot process this service should start. With that said, create an unit file in the /etc/systemd/system directory
```bash
  sudo nano /etc/systemd/system/ssa.service
```
Then add this into the file.
```bash
[Unit]
Description=Gunicorn instance for a simple hello world app
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/helloworld
ExecStart=/home/ubuntu/helloworld/venv/bin/gunicorn -b localhost:8000 app:app
Restart=always
[Install]
WantedBy=multi-user.target
```
Then enable the service:
```bash
  sudo systemctl daemon-reload
  sudo systemctl start helloworld
  sudo systemctl enable helloworld
```
Check if the app is running with
```bash
  curl localhost:8000
```
Run Nginx Webserver to accept and route request to Gunicorn Finally, we set up Nginx as a reverse-proxy to accept the requests from the user and route it to gunicorn.
Start the Nginx service and go to the Public IP address of your EC2 on the browser to see the default nginx landing page
```bash
  sudo systemctl start nginx
  sudo systemctl enable nginx
```
Edit the default file in the sites-available folder.
```bash
  sudo nano /etc/nginx/sites-available/default
```
Add the following code at the top of the file (below the default comments)
```bash
  upstream flaskhelloworld {
    server 127.0.0.1:5000;
}
```
Add a proxy_pass to flaskhelloworld atlocation /
```bash
  location / {
    proxy_pass http://flaskhelloworld;
}
```
Configurin reat API
```bash
  location /api/ {
                    rewrite ^/api(.*) $1 break;
                    proxy_pass http://127.0.0.1:5000;
        }
```
Starting Python Flask server
```bash
  python3 server.py
```
Restart Nginx
```bash
  sudo systemctl restart nginx
```
Tada! Our application is up!
## Tech Stack


**Client:** HTML, CSS, Nginx, 

**Server:** Flask, Gunicorn

**Deployment:** Amazon EC2

**Utility:** Jupyter Notebook, VS Code, Git. 


## Features

- Dynamic : Predict Sentiment based on the latest news headlines.
- Covers all the mazor U.S Tech Stocks.
- Display the complete analysis using bar graph



## Optimizations

Model performed better as compared to the most popular sentiment analysis model VADER for the finance news heading categorization. 


## Lessons Learned

Key learning from this project includes-
1. Text processing using NLTK.
2. Working with time series data.
3. Data cleaning, EDA, Feature Engineering.
4. Model Deployment on AWS.


# Hi, I'm Akshat Shukla! 👋


## 🚀 About Me
A dedicated and aspiring data scientist with 2 years of experience in oil & gas software industry. Proficient in Python, ML, SQL. Looking for an opportunity to utilize my technical and analytical skill to build models that can solve business problem. Enthusiast for learning new tools and technology.


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/akshatshukla12)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akshat-shukla-9890/)



## Other Common Github Profile Sections
👩‍💻 I'm currently working as a G&G Support analyst at Halliburton.

🧠 I'm currently learning Data Science, Machine Learning and AI.

👯‍♀️ I'm looking to collaborate on Machine Learning Projects

🤔 I'm looking for help with...

💬 Ask me about Geology, Geophysics, Data Science, Machine Learning. 

📫 How to reach me - email- akshatshuklanit06@gmail.Common, ph no. 9009067432

⚡️ Fun fact...


## 🛠 Skills
Python, SQL, Git, HTML, CSS, AWS, Numpy, Pandas, Matplotlib, Seaborn, scikit-learn, scipy, BS4, Flask, Deployment, Probability, Statistics, Linear algebra, calculus, Vector & Matrices, Distributions, Regression, Sampling. 


## Author

- [@AKSHAT SHUKLA](https://github.com/akshatshukla12)

