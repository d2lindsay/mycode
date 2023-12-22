#!/usr/bin/python3
"""News Headline Pull with the News API"""

from pprint import pprint 

import requests

from random import randint
from random import shuffle

base_url = "https://newsapi.org/v2/top-headlines?"

def main():

    with open("/home/student/mycode/news_project/news.creds") as mycreds:
        newscreds = mycreds.read()

    newscreds = "apiKey=" + newscreds.strip("\n")

    print("Top 10 Headlines from Tech Crunch Right Now:")
    
    news = requests.get(base_url + f"country=us&{newscreds}").json()
    
    news_dict = news.get("articles")
    total_articles = news.get("totalResults")
    
    
    print(f"Total articles: {total_articles}")
    
    count = 1
    for n in news_dict:
        if count > 10:
            break
        else:
            print(f"{count}) {n['title']}")
         
        count += 1
    
    while True:
        print("\n")
        user_select = input("Would you like to view a specific article (y/n)?" + "\n>>>")
    
        if user_select == "y":
            article_select = input("Enter the number of the article you'd like to view (1-10)" + "\n>>>")
            article_select = int(article_select) - 1
            print(f"\n{news_dict[article_select]['title']}")
            print(f"Source: {news_dict[article_select]['source']['name']}")
            print(f"Author: {news_dict[article_select]['author']}")
            print(f"Preview:\n{news_dict[article_select]['description']}")
            print(f"\n{news_dict[article_select]['url']}")
        else:
            break

if __name__ == "__main__":
    main()
