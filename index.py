from src.Crawler import Crawler


try:

	c = Crawler
	c.crawl()
except Exception as error:
    print("Oops! Error Caught:", error)
    exit(0)
