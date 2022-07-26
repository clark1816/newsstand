import streamlit as st
from requests_html import HTMLSession
session = HTMLSession()

option = 'News'
if option == 'News':
    news_option = st.sidebar.selectbox("What Type of News?", ('Business', 'Technology', 'Covid','Russo-Ukrainian War','Sports', 'Health','World News', 'Entertainment'), 0)

    if news_option == 'Business':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?gl=US&hl=en-US&ceid=US:en'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Technology':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Covid':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Covid':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass
        
    if news_option == 'Russo-Ukrainian War':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqJAgKIh5DQkFTRUFvS0wyMHZNRjk0Tm1RMWVCSUNaVzRvQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Sports':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Health':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'World News':
        st.title(news_option)
        url = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'US News':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass

    if news_option == 'Entertainment News':
        st.title(news_option)
        url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
        r = session.get(url)
        articles = r.html.find('article')
        for item in articles:
            try:
                newsitem = item.find('h3', first = True)
                title = newsitem.text
                link = newsitem.absolute_links
                st.write(title)
                text='check out this [link]({link})'.format(link=link)
                st.markdown(link,unsafe_allow_html=True)
            except:
                pass









