from urllib import request
from urllib import error
from urllib import parse
import re
import unicodedata
import config.domain as cnf
from bs4 import BeautifulSoup

class FinancialScraper():

    def __init__(self):
        self.info = {}
        
    def downloadHtml(self, url):
        try:
            html = request.urlopen(url)
            return html
        except error.HTTPError as e:
            return None

    def cleanData(self, string):
        return string.replace(",", ".").replace("\xa0", "")

    def createUrl(self, domain, attributes):
        return domain+"?"+attributes

    def getUrlByCompany(self, nameCompany):
        urlCompany = []
        url = self.createUrl(cnf.domain+cnf.subdomains.get("searchCompanies"), cnf.attributes.get("search")+nameCompany)
        html = self.downloadHtml(url)
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find(id="ctl00_Contenido_tblEmisoras")
        for tr in table.findAll("tr"):
            children = tr.findChildren("td")
            for td in children:
                relative = td.find("a").get("href")
                urlCompany.append(cnf.domain + relative)
        return urlCompany
    
    def getInfoByUrl(self, urls):
        for url in urls:
            parsed = parse.urlparse(url)
            reQuery = parse.parse_qs(parsed.query)["ISIN"]
            regex = re.match("^ES*", reQuery[0])
            if regex is not None:
                self.getFinancialInfo(url)
                self.getHistoricInfo(regex.string)
        return self.info

    def getFinancialInfo(self, url):
        html = self.downloadHtml(url)
        dic = {}
        soup = BeautifulSoup(html, "lxml")
        label = soup.find(attrs={"class" : re.compile(r"TituloPag")})
        assert (label != None)
        dic[cnf.tags.get("name")] = self.cleanData(label.next_element)
        table = soup.find(id="ctl00_Contenido_tblValor")
        for tr in table.findAll("tr"):
            children = tr.findChildren("td")
            dic[cnf.tags.get("isin")] = self.cleanData(children[1].next_element)
            dic[cnf.tags.get("ticker")] = self.cleanData(children[3].next_element)
            dic[cnf.tags.get("nominal")] = self.cleanData(children[5].next_element)
            dic[cnf.tags.get("market")] = self.cleanData(children[7].next_element)
            dic[cnf.tags.get("capital")] = self.cleanData(children[9].next_element)
        if dic[cnf.tags.get("market")] == "Mercado Continuo":
            self.info = dic

    def getHistoricInfo(self, isin):
        url = self.createUrl(cnf.domain+cnf.subdomains.get("getHistoricInfo"), cnf.attributes.get("isin")+isin)
        html = self.downloadHtml(url)
        soup = BeautifulSoup(html, "lxml")
        table = soup.find(id="ctl00_Contenido_tblDatos")
        if (table != None):
            res = []
            for tr in table.findAll("tr"):
                children = tr.findChildren("td")
                dic = {}
                if len(children) > 0:
                    dic[cnf.historic.get("date")] = self.cleanData(children[0].next_element)
                    dic[cnf.historic.get("close")] = self.cleanData(children[1].next_element)
                    dic[cnf.historic.get("ref")] = self.cleanData(children[2].next_element)
                    dic[cnf.historic.get("vol")] = self.cleanData(children[3].next_element)
                    dic[cnf.historic.get("turnover")] = self.cleanData(children[4].next_element)
                    dic[cnf.historic.get("last")] = self.cleanData(children[5].next_element)
                    dic[cnf.historic.get("high")] = self.cleanData(children[6].next_element)
                    dic[cnf.historic.get("lww")] = self.cleanData(children[7].next_element)
                    dic[cnf.historic.get("avg")] = self.cleanData(children[8].next_element)
                    res.append(dic)
            self.info[cnf.tags.get("stocks")] = res

    def data_to_csv(self, filename):
        file = open("../results/"+filename, "w+")
        
        for key in self.info:
            if key == "stocks":
                file.write("\n")
                for i in self.info[key]:
                    for j in i:
                        file.write(i[j]+",")
                    file.write("\n")
            else:
                file.write(self.info[key]+",")

    