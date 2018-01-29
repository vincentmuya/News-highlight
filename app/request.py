import urllib.request
import json
from .models import News
# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news_source(country,category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_source_url = base_url.format(country,category,api_key)

    with urllib.request.urlopen(get_news_source_url)as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)
        print(get_news_source_response)
        source_result = None

        if get_news_source_response['articles']:
          source_result_list = get_news_source_response['articles']
          source_result = process_result(source_result_list)

    return source_result

def process_result(source_list):
    '''
    this function processes the results and converts them into a list
    the source list is  a list of dictionaries containing news results
    '''
    source_result= []

    for source_item in source_list:
       source = source_item.get('source')
       author = source_item.get('author')
       title = source_item.get('title')
       description = source_item.get('description')
       url = source_item.get('url')
       urlToImage = source_item.get('urlToImage')
       publishedAt = source_item.get('publishedAt')

       if urlToImage:
           source_object = News(source,author,title,description,url,urlToImage,publishedAt)
           source_result.append(source_object)

    return source_result


def get_news(source):
    get_news_details_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            source = news_details_response.get('source')
            author = news_details_response.get('original_author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            urlToImage = news_details_response.get('urlToImage')

            news_object = news(source,author,title,description,url,urlToImage,publishedAt)

    return news_object
