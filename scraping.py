# scraping.py

import bs4
from langchain_community.document_loaders import WebBaseLoader
from typing import List

SCRAPER_CONFIGS = {
    "lilianweng": {
        "parse_only": bs4.SoupStrainer(
            class_=("post-content", "post-header")
        )
    },
    "bbc": {
        "parse_only": bs4.SoupStrainer(
            class_=("main-content",) # class must be in a tuple or list
        )
    },
    "wikipedia": {
        "parse_only": bs4.SoupStrainer(
            class_=("mw-parser-output",)
        )
    }
}

def scrape_website(url: str, site_key: str) -> List:
    """
    Scrapes a website using a predefined configuration.

    Args:
        url (str): The URL of the webpage to scrape.
        site_key (str): The key corresponding to the website's configuration
                        in SCRAPER_CONFIGS (e.g., "wikipedia").

    Returns:
        List: A list of LangChain Document objects, or an empty list if scraping fails.
        
    Raises:
        ValueError: If the site_key is not found in SCRAPER_CONFIGS.
    """
    if site_key not in SCRAPER_CONFIGS:
        raise ValueError(f"Unknown site key: '{site_key}'. Please add it to SCRAPER_CONFIGS.")

    bs_kwargs_config = SCRAPER_CONFIGS[site_key]

    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=bs_kwargs_config,
    )

    try:
        docs = loader.load()
        return docs
    
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
        return []