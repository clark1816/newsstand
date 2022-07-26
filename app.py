from pygooglenews import GoogleNews
import streamlit as st
option = 'News'
if option == 'News':
    news_option = st.sidebar.selectbox("What Type of News?", ('Business', 'Technology', 'Science','Russo-Ukrainian War','Covid','Sports', 'Health','World News', 'Entertainment'), 0)
    gn = GoogleNews()
    
    if news_option == 'Russo-Ukrainian War':
        st.title(news_option)
        world = gn.topic_headlines('CAAqJAgKIh5DQkFTRUFvS0wyMHZNRjk0Tm1RMWVCSUNaVzRvQUFQAQ')
        newsitem = world['entries']
        for item in newsitem:
            st.write(item.title)
            st.write(item.link)
    if news_option == 'Covid':
        covid_topic = st.sidebar.selectbox("What Type of Covid News?", ('Latest','Americas', 'Africa', 'Europe', 'Western Pacific', 'South-East Asia' ), 0)
        if covid_topic == 'Latest':
            st.title(news_option + " " + covid_topic)
            tech = gn.topic_headlines('CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if covid_topic == 'Western Pacific':
            st.title(news_option + " " + covid_topic)
            tech = gn.topic_headlines('CAAqBwgKMKC5lwsw6eKuAw')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if covid_topic == 'Americas':
            st.title(news_option + " " + covid_topic)
            tech = gn.topic_headlines('CAAqBwgKMJ65lwsw5-KuAw')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if covid_topic == 'Africa':
            st.title(news_option + " " + covid_topic)
            tech = gn.topic_headlines('CAAqBwgKMJ25lwsw5uKuAw')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if covid_topic == 'South-East Asia':
            st.title(news_option + " " + covid_topic)
            tech = gn.topic_headlines('CAAqBwgKMPO5lwsw6OKuAw')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

    if news_option == 'Health':
        health_topic = st.sidebar.selectbox("What Type of Science News?", ('Latest', 'Environment','Outer space', 'Physics', 'Wildlife'), 0)
        
        if health_topic == 'Latest':
            st.title(news_option + " " + health_topic)
            tech = gn.topic_headlines('CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if health_topic == 'Fitness':
            st.title(news_option + " " + health_topic)
            tech = gn.topic_headlines('CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiV0NCQVNPd29JTDIwdk1HdDBOVEVTQW1WdUlnOElCQm9MQ2drdmJTOHdNamQ0TjI0cUdnb1lDaFJHU1ZST1JWTlRYMU5GUTFSSlQwNWZUa0ZOUlNBQktBQSolCAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if health_topic == 'Mental health':
            st.title(news_option + " " + health_topic)
            tech = gn.topic_headlines('CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiQ0NCQVNMQW9JTDIwdk1HdDBOVEVTQW1WdUlnOElCQm9MQ2drdmJTOHdNM2cyT1djcUN4SUpMMjB2TURONE5qbG5LQUEqJQgAKiEICiIbQ0JBU0Rnb0lMMjB2TUd0ME5URVNBbVZ1S0FBUAFQAQ')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if health_topic == 'Medicine':
            st.title(news_option + " " + health_topic)
            tech = gn.topic_headlines('CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ/sections/CAQiQENCQVNLZ29JTDIwdk1HdDBOVEVTQW1WdUlnNElCQm9LQ2dndmJTOHdOSE5vTXlvS0VnZ3ZiUzh3TkhOb015Z0EqJQgAKiEICiIbQ0JBU0Rnb0lMMjB2TUd0ME5URVNBbVZ1S0FBUAFQAQ')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
    if news_option == 'Science':
        science_topic = st.sidebar.selectbox("What Type of Science News?", ('Latest', 'Environment','Outer space', 'Physics', 'Wildlife'), 0)
        
        if science_topic == 'Latest':
            st.title(news_option + " " + science_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if science_topic == 'Environment':
            st.title(news_option + " " + science_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiS0NCQVNNZ29JTDIwdk1EWnRjVGNTQW1WdUdnSlZVeUlRQ0FRYURBb0tMMjB2TURRMk5qTXljeW9NRWdvdmJTOHdORFkyTXpKektBQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if science_topic == 'Outer space':
            st.title(news_option + " " + science_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiSENCQVNNQW9JTDIwdk1EWnRjVGNTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURFNE16TjNLZ3NTQ1M5dEx6QXhPRE16ZHlnQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if science_topic == 'Physics':
            st.title(news_option + " " + science_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EWnRjVGNTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURWeGFuUXFDaElJTDIwdk1EVnhhblFvQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURadGNUY1NBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if science_topic == 'Wildlife':
            st.title(news_option + " " + science_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB/sections/CAQiSENCQVNNQW9JTDIwdk1EWnRjVGNTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURFeU9EQm5LZ3NTQ1M5dEx6QXhNamd3WnlnQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

    if news_option == 'Sports':
        sport_topic = st.sidebar.selectbox("What Type of Sports News?", ('Latest', 'NFL','NBA', 'MLB', 'Golf'), 0)
        
        if sport_topic == 'Latest':
            st.title(news_option + " " + sport_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if sport_topic == 'NFL':
            st.title(news_option + " " + sport_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB/sections/CAQiQkNCQVNLd29JTDIwdk1EWnVkR29TQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURVNWVXb3FCd29GRWdOT1Jrd29BQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if sport_topic == 'NBA':
            st.title(news_option + " " + sport_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB/sections/CAQiQkNCQVNLd29JTDIwdk1EWnVkR29TQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURWcWRuZ3FCd29GRWdOT1FrRW9BQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if sport_topic == 'MLB':
            st.title(news_option + " " + sport_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB/sections/CAQiQkNCQVNLd29JTDIwdk1EWnVkR29TQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURsd01UUXFCd29GRWdOTlRFSW9BQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        if sport_topic == 'Golf':
            st.title(news_option + " " + sport_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB/sections/CAQiQ0NCQVNMQW9JTDIwdk1EWnVkR29TQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURNM2FIb3FDQW9HRWdSSGIyeG1LQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURadWRHb1NBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
    if news_option == 'Technology':
        tech_topic = st.sidebar.selectbox("What Type of Technology News?", ('Latest', 'Mobile','Gadgets', 'Internet', 'Virtual reality','Artifical intelligence', 'Computing'), 0)
        
        if tech_topic == 'Latest':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

        if tech_topic == 'Gadgets':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiW0NCQVNQZ29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURKdFpqRnVLaGtLRndvVFIwRkVSMFZVWDFORlExUkpUMDVmVGtGTlJTQUJLQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURkak1YWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

        if tech_topic == 'Mobile':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiYkNCQVNRd29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURVd2F6Z3FId29kQ2hsTlQwSkpURVZmVUVoUFRrVmZVMFZEVkVsUFRsOU9RVTFGSUFFb0FBKioIAComCAoiIENCQVNFZ29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeWdBUAFQAQ')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
        if tech_topic == 'Internet':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TUROeWJIUXFDaElJTDIwdk1ETnliSFFvQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURkak1YWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
        if tech_topic == 'Virtual reality':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURkZmJua3FDaElJTDIwdk1EZGZibmtvQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURkak1YWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

        if tech_topic == 'Artifical intelligence':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiQ0NCQVNMQW9JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlOQ0FRYUNRb0hMMjB2TUcxcmVpb0pFZ2N2YlM4d2JXdDZLQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURkak1YWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
        if tech_topic == 'Computing':
            st.title(news_option + " " + tech_topic)
            tech = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EZGpNWFlTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURGc2NITXFDaElJTDIwdk1ERnNjSE1vQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURkak1YWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = tech['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

    if news_option == 'World News':
        st.title(news_option)
        world = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB')
        newsitem = world['entries']
        for item in newsitem:
            st.write(item.title)
            st.write(item.link)
    if news_option == 'Entertainment':
        st.title(news_option)
        world = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB')
        newsitem = world['entries']
        for item in newsitem:
            st.write(item.title)
            st.write(item.link)
    
    if news_option == 'Business':
        business_topic = st.sidebar.selectbox("What Type of Business News?", ('Latest','Economy', 'Markets', 'Jobs','Personal finance', 'Entrepreneurship'), 0)
        
        if business_topic == 'Latest':
            st.title(news_option + " " + business_topic)
            business = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB')
            newsitem = business['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
        if business_topic == 'Economy':
            st.title(news_option + " " + business_topic)
            business = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiSENCQVNNQW9JTDIwdk1EbHpNV1lTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TUdkbWNITXpLZ3NTQ1M5dEx6Qm5abkJ6TXlnQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = business['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
                

        if business_topic == 'Markets':
            st.title(news_option + " " + business_topic)
            business = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiXENCQVNQd29JTDIwdk1EbHpNV1lTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURsNU5IQnRLaG9LR0FvVVRVRlNTMFZVVTE5VFJVTlVTVTlPWDA1QlRVVWdBU2dBKioIAComCAoiIENCQVNFZ29JTDIwdk1EbHpNV1lTQW1WdUdnSlZVeWdBUAFQAQ')
            newsitem = business['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
        
        if business_topic == 'Personal finance':
            st.title(news_option + " " + business_topic)
            business = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiSENCQVNNQW9JTDIwdk1EbHpNV1lTQW1WdUdnSlZVeUlQQ0FRYUN3b0pMMjB2TURGNU5tTnhLZ3NTQ1M5dEx6QXhlVFpqY1NnQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVABUAE')
            newsitem = business['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)

        if business_topic == 'Entrepreneurship':
            st.title(news_option + " " + business_topic)
            business = gn.topic_headlines('CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB/sections/CAQiRkNCQVNMZ29JTDIwdk1EbHpNV1lTQW1WdUdnSlZVeUlPQ0FRYUNnb0lMMjB2TURKdWQzRXFDaElJTDIwdk1ESnVkM0VvQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURsek1XWVNBbVZ1R2dKVlV5Z0FQAVAB')
            newsitem = business['entries']
            for item in newsitem:
                st.write(item.title)
                st.write(item.link)
