from bs4 import BeautifulSoup
import requests
import ast
import os
from io import BytesIO
import json
from mxvie import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mxvie.settings")
import django
django.setup()

from review_data.models import Movie
from review_data.models import Review

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_movies(): #영화 리스트 가져오기
    with open("C:\\mymovie\\movie_list.txt","r",encoding='utf-8') as f:
        data = f.read()
    data = ast.literal_eval(data)
    return data

def get_reviews(m_title): #영화 한 개의 리뷰리스트 생성
    title = m_title
    review_list = []
    for i in range(1,11):
        URL1 = f"https://www.rottentomatoes.com/m/{title}/"
        URL2 = f"reviews/?page={i}&sort="
        URL="".join([URL1,URL2])
        content = requests.get(URL).text
        soup = BeautifulSoup(content,'html.parser')
        Data_list = soup.find_all("div","the_review")
        for i in Data_list:
            review_list.append(i.text)
    sentiments = []
    for i in review_list:
        sentiments.append(sid.polarity_scores(i))
    zipped_result = []
    for i in zip(review_list,sentiments):
        zipped_result.append(i)
    return zipped_result

def get_movieSrc(m_title):
    title = m_title
    URL = f"https://www.rottentomatoes.com/m/{title}/"
    content = requests.get(URL).text
    soup = BeautifulSoup(content,'html.parser')
    a_tags = soup.find('div',{'class':'center'})
    img_tag = a_tags.find('img',{"src":True})
    if img_tag == None:
        img_tag = a_tags.find('img',{"data-src":True})
    result = img_tag.get('src')
    if result == "/assets/pizza-pie/images/poster_default.c8c896e70c3.gif":
        result = img_tag.get('data-src')
    elif result == None:
        result = img_tag.get('data-src')
    return result

def get_movieSynopsis(m_title):
    title = m_title
    URL = f"https://www.rottentomatoes.com/m/{title}/"
    content = requests.get(URL).text
    soup = BeautifulSoup(content,'html.parser')
    movieSynopsis = soup.find('div',{'id':'movieSynopsis'})
    ms = movieSynopsis.get_text()
    return ms

def get_movietitle(m_title):
    title = m_title
    URL = f"https://www.rottentomatoes.com/m/{title}/"
    content = requests.get(URL).text
    soup = BeautifulSoup(content,'html.parser')
    mt = soup.find('h1',{'id':'movie-title'})
    movietitle = mt.get_text()
    return movietitle

"""
def get_movieInfo(m_title):  #genre,director,released_date,runtime
    title = m_title
    URL = f"https://www.rottentomatoes.com/m/{title}/"
    content = requests.get(URL).text
    soup = BeautifulSoup(content,'html.parser')



def get_sentiments(m_title): #영화 한 개의 리뷰 리스트를 가져와서 감성분석
    reviews = get_reviews(m_title)
    sentiments = []
    for i in reviews:
        sentiments.append(sid.polarity_scores(i))
    return sentiments

def get_result(): #영화 한 개의 리뷰 리스트와 감성분석 결과를 튜플로 리턴
    review_result = get_reviews()
    sentiment_result = get_sentiments()
    zipped_result = []
    for i in zip(review_result,sentiment_result):
        zipped_result.append(i)
    return zipped_result
"""

if __name__ == '__main__':
    movies = get_movies()
    for idx,val in enumerate(movies):
        result = get_reviews(val)
        srcs = get_movieSrc(val)
        synps = get_movieSynopsis(val)
        titleofmovie = get_movietitle(val)
        movie = Movie.objects.create(no=idx,title=titleofmovie,src=srcs,synp=synps)
        movie.save()
        xindx = []
        yindx = []
        for i,j in result: #i == contents, j = sentiments
            pos_val = j['pos']
            neg_val = j['neg']
            neu_val = j['neu']
            comp_val = j['compound']
            sum = pos_val - neg_val
            xindx.append(sum)
            yindx.append(comp_val)
            review = Review.objects.create(movie=movie, contents=i, sentiments = j, sentiments_pos=pos_val, sentiments_neg=neg_val, sentiments_neu=neu_val, sentiments_comp=comp_val)
            review.save()
        sns.jointplot(x=xindx,y=yindx,kind='hex')
        path = os.path.join(settings.MEDIA_ROOT, '{}'.format(idx))
        plt.savefig(path)
