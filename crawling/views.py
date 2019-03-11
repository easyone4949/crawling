from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

def home(request):
    html = urlopen(
        'http://computer.cnu.ac.kr/index.php?mid=notice')
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    recent_blog_post = []
    crawled_data = bsObj.find_all('td', {"class": "title"})

    for post in crawled_data:
        if post.a.strong is not None:
            recent_blog_post.append(post.a.strong.get_text())
        
    return render(request, 'home.html', {"posts": recent_blog_post})
    