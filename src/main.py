from scraper import FinancialScraper
#
# Dependencies: 
# lxml
# BeautifulSoup

def main():
    scraper = FinancialScraper()
    urls = scraper.getUrlByCompany("acs")
    info = scraper.getInfoByUrl(urls)
    print(info)
    scraper.data_to_csv()


if __name__ == "__main__":
    main()