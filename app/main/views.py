from flask import render_template
from . import main
from ..request import get_news_source,get_news
# ,get_news

#views
@main.route('/')
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
    technology = get_news_source('ca','science')
    # print(sport)

    title = "Welcome to News HighLight"
    return render_template('index.html', title = title, technology = technology, sport=sport,science=science,health=health,business=business,entertainment=entertainment)

@main.route('/news/<int:source_id>')
def news(source_id):
   '''
   page function that returns books data
   '''
   news = get_news_source(source)
   title = f'{tite.source}'

   return render_template('news.html',title = title, id = source_id)
