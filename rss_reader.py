import feedparser
import html2text
import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def main():
    all_entries = []
    
    while True:
        rss_input = input("Please provide the RSS feed URL's and once you are ready to read them all, write Q: ")
        
        if rss_input.strip().upper() == "Q":
            print("Exiting the RSS reader.")
            break
        
        feed = feedparser.parse(rss_input)

        if feed.status == 200:
            for entry in feed.entries:
                all_entries.append({
                    'title': entry.title,
                    'description': entry.description,
                    'link': entry.link
                })
        else:
            print("Failed to get RSS feed. Status code: ", feed.status)

    # Display all fetched entries
    if all_entries:
        for entry in all_entries:
            print("---------------")
            print(f"Title: {entry['title']}")
            plain_description = html2text.html2text(entry['description'])  # Convert HTML to plain text
            print(f"Description: {remove_html_tags(plain_description)}")  # Remove any remaining HTML tags
            print(f"Source: {entry['link']}\n")

if __name__ == "__main__":
    main()
