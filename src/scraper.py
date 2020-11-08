from urllib import request
from urllib import error
from urllib import parse
import re
import unicodedata
import config.domain as cnf
from bs4 import BeautifulSoup

class FinancialScraper():

    def __init__(self):
        self.domain = cnf.domain
        self.subdomains = cnf.subdomains
        self.attributes = cnf.attributes
        self.info = []
        
    def downloadHtml(self, url):
        try:
            html = request.urlopen(url)
            return html
        except error.HTTPError as e:
            return None

    def getUrlByCompany(self, nameCompany):
        urlCompany = []
        url = self.domain+self.subdomains.get("searchCompanies")+"?"+self.attributes.get("search")+nameCompany
        html = self.downloadHtml(url)
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find(id="ctl00_Contenido_tblEmisoras")
        for tr in table.findAll("tr"):
            children = tr.findChildren("td")
            for td in children:
                relative = td.find("a").get("href")
                urlCompany.append(self.domain + relative)
        return urlCompany
    
    def getInfoByUrl(self, urls):
        for url in urls:
            html = self.downloadHtml(url)
            parsed = parse.urlparse(url)
            reQuery = parse.parse_qs(parsed.query)["ISIN"]
            regex = re.match("^ES*", reQuery[0])
            if regex is not None:
                dic = {"isin" : "", "data" : {}}
                soup = BeautifulSoup(html, "lxml")
                label = soup.find(attrs={"class" : re.compile(r"TituloPag")})
                if label is not None:
                    dic["data"]["name"] = label.next_element.replace("\xa0", "")
                    table = soup.find(id="ctl00_Contenido_tblValor")
                    for tr in table.findAll("tr"):
                        children = tr.findChildren("td")
                        dic["isin"] = children[1].next_element.replace("\xa0", "")
                        dic["data"]["ticker"] = children[3].next_element.replace("\xa0", "")
                        dic["data"]["nominal"] = children[5].next_element.replace("\xa0", "")
                        dic["data"]["market"] = children[7].next_element.replace("\xa0", "")
                        dic["data"]["capital"] = children[9].next_element.replace("\xa0", "")
                    self.info.append(dic)
        return self.info

    def data_to_csv(self):
        file = open("ourput.csv", "w+")
        
        for row in self.info:
            file.write(row["isin"])
            for col in row["data"]:
                file.write(";"+col)
            file.write("\n")

    