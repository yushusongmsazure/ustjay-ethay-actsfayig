'''
Yushu Song
Assignment 5
'''

import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    '''
    Get a fact from unkno
    '''

    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()

def query_pig_latin(fact):
    '''
    Query pig latin using a fact
    '''

    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data={"input_text":fact},
                             allow_redirects=False)

    return response.headers['Location']


@app.route('/')
def home():
    fact = get_fact()
    link = query_pig_latin(fact)
    return f'<a href={link}>{link}</a>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)