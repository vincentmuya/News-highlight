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
    technology_source = get_news_source('ca','science')
    print(technology_source)

    title = "Welcome to News HighLight"
    return render_template('index.html', title = title, technology_source = technology_source)

@app.route('/news/<int:totalResults>')
def news(totalResults):
   '''
   page function that returns books data

   '''
   return render_template('news.html', id = totalResults)
