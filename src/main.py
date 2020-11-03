from scraper import FinancialScraper
#
# Dependencies: 
# lxml
# BeautifulSoup

def main():
    scraper = FinancialScraper()
    urls = scraper.getUrlByCompany("bbva")
    info = scraper.getInfoByUrl(urls)
    print(info)


if __name__ == "__main__":
    main()