from flask import render_template
from app import app
from .request import get_news_source


#views
@app.route('/')
def index():

    '''
    Views root page function that returns the index page and its data
    '''
    #getting technology news
    sport = get_news_source('ca','sport')
    science = get_news_source('ca','science')
    health = get_news_source('ca','health')
    entertainment = get_news_source('ca','entertainment')
    business = get_news_source('ca','business')
    technology_source = get_news_source('ca','science')
    print(sport)

    title = "Welcome to News HighLight"
    return render_template('index.html', title = title, technology_source = technology_source, sport=sport,science=science,health=health,business=business,entertainment=entertainment)

@app.route('/news/<int:totalResults>')
def news(totalResults):
   '''
   page function that returns books data

   '''
   return render_template('news.html', id = totalResults)
