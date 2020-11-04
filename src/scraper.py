from urllib import request
from urllib import error
from urllib import parse
import re
import unicodedata
from bs4 import BeautifulSoup

class FinancialScraper():

    def __init__(self):
        self.domain = "https://www.bolsamadrid.es"
        self.subdomains = {
            "searchCompanies":"/esp/aspx/Empresas/BusqEmpresas.aspx",
            "getCompany":"/esp/aspx/Empresas/FichaValor.aspx"
        }
        self.attributes = {
            "search":"busq=",
            "isin":"ISIN=",
            "clv":"ClvEmis="
        }
        self.info = []

    def getUrlByCompany(self, nameCompany):
        url = []
        try:
            html = request.urlopen(self.domain+self.subdomains.get("searchCompanies")+"?"+self.attributes.get("search")+nameCompany)
        except error.HTTPError as e:
            print("HTTPERROR =", str(e.code))
        finally:
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find(id="ctl00_Contenido_tblEmisoras")
            for tr in table.findAll("tr"):
                children = tr.findChildren("td")
                for td in children:
                    urlCompany = td.find("a").get("href")
                    url.append(self.domain + urlCompany)
        return url
    
    def getInfoByUrl(self, urls):
        for url in urls:
            try:
                html = request.urlopen(url)
            except error.HTTPError as e:
                print("HTTPERROR =", str(e.code))
            finally:
                parsed = parse.urlparse(url)
                a = parse.parse_qs(parsed.query)["ISIN"]
                x = re.match("^ES*", a[0])
                if x is not None:
                    dic = {"isin" : "", "data" : {}}
                    soup = BeautifulSoup(html, "lxml")
                    label = soup.find(attrs={"class" : re.compile(r"TituloPag")})
                    if label is not None:
                        dic["data"]["name"] = label.next_element
                        table = soup.find(id="ctl00_Contenido_tblValor")
                        for tr in table.findAll("tr"):
                            children = tr.findChildren("td")
                            dic["isin"] = children[1].next_element
                            dic["data"]["ticker"] = children[3].next_element
                            dic["data"]["nominal"] = children[5].next_element
                            dic["data"]["market"] = children[7].next_element
                            dic["data"]["capital"] = children[9].next_element
                        self.info.append(dic)
        return self.info

    def data_to_csv(self):
        print("")

    