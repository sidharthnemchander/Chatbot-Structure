from scraping import scrape_website
from indexing import Embeddings

"""This is just a scraping example """
print("--- Scraping Wikipedia ---")
wiki_url = "https://en.wikipedia.org/wiki/Large_language_model"
wiki_docs = scrape_website(url=wiki_url, site_key="wikipedia")

if wiki_docs:
    # print(wiki_docs[0].page_content[:500])
    pass
else:
    print("Failed to scrape Wikipedia page.")

#Enter the blog url u want to scrap from and check the site_key to find the correct format of html tag scraping

print("--- Scraping Lilian Weng's Blog ---")
blog_url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
blog_docs = scrape_website(url=blog_url, site_key="lilianweng")
embeddings_db = Embeddings(blog_docs)


if blog_docs:
    # print(blog_docs[0].page_content[:500])
    pass
else:
    print("Failed to scrape blog post.")