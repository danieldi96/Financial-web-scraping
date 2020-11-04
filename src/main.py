from scraper import FinancialScraper
#
# Dependencies: 
# lxml
# BeautifulSoup

def main():
    scraper = FinancialScraper()
    urls = scraper.getUrlByCompany("acs")
    info = scraper.getInfoByUrl(urls)
    scraper.data_to_csv()
    print(info)


if __name__ == "__main__":
    main()