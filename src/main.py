from scraper import FinancialScraper
#
# Dependencies: 
# lxml
# BeautifulSoup

def main():
    scraper = FinancialScraper()
    urls = scraper.getUrlByCompany("santander")
    info = scraper.getInfoByUrl(urls)
    scraper.data_to_csv("santander.csv")



if __name__ == "__main__":
    main()