from scraper import FinancialScraper
#
# Dependencies: 
# lxml
# BeautifulSoup

# Parameter to define
Company = "santander"

def main():
    scraper = FinancialScraper()
    urls = scraper.getUrlByCompany(Company)
    info = scraper.getInfoByUrl(urls)
    scraper.data_to_csv(Company+".csv")



if __name__ == "__main__":
    main()