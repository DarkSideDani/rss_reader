import feedparser


rss_url = "https://www.mmafighting.com/rss/current"
feed = feedparser.parse(rss_url)

if feed.status == 200:
    for entry in feed.entries:
        print(entry.title)
        print(entry.link)
else:
    print("Failed to get RSS feed. Status code: ", feed.status)
    
