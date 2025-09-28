# main.py

from scraping import scrape_website # Import our new function

# --- Project 1: Scrape a Wikipedia Article ---
print("--- Scraping Wikipedia ---")
wiki_url = "https://en.wikipedia.org/wiki/Large_language_model"
# Call the function with the URL and the key for the Wikipedia config
wiki_docs = scrape_website(url=wiki_url, site_key="wikipedia")

if wiki_docs:
    # Print the first 500 characters of the scraped content
    print(wiki_docs[0].page_content[:500])
else:
    print("Failed to scrape Wikipedia page.")


print("\n" + "="*50 + "\n")


# --- Project 2: Scrape Lilian Weng's Blog ---
print("--- Scraping Lilian Weng's Blog ---")
blog_url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
# Reuse the exact same function with a different URL and site_key
blog_docs = scrape_website(url=blog_url, site_key="lilianweng")

if blog_docs:
    print(blog_docs[0].page_content[:500])
else:
    print("Failed to scrape blog post.")