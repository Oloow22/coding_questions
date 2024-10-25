import requests
import json

#import the requests library to make the API call and the json library to parse the response

class PostFetcher:
    #fetch the posts from the api
    
    def __init__(self, api_url, per_page):
        #initialize the api url and per page
        self.api_url = api_url
        self.per_page = per_page

    def fetch_posts(self, page):
        #fetch the posts from the api
        params = {'_page': page, '_limit': self.per_page}
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def display_posts(self, posts):
        #display the title of a post
        if posts is not None:
            for post in posts:
                print(post['title'])

    def paginate_posts(self):
    
        page = 1
        while True:
            posts = self.fetch_posts(page)
            self.display_posts(posts)
            cont = input("Do you want to see the next page? (yes/no): ")
            if cont.lower() != 'yes':
                break
            page += 1


api_url = 'https://jsonplaceholder.typicode.com/posts'
per_page = 5

post_fetcher = PostFetcher(api_url, per_page)
post_fetcher.paginate_posts()