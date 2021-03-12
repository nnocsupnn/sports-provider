from src.Crawler import Crawler


try:
	cx = Crawler()
	cx.crawl("https://www.oddsportal.com/basketball/argentina/liga-a/libertad-penarol-hKnyF3Nl/")
except Exception as error:
    print("Oops! Error Caught:", error)
    exit(0)
