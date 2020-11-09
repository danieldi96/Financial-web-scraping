# Info about the domain to get the data
domain = "https://www.bolsamadrid.es"

subdomains = { "searchCompanies":"/esp/aspx/Empresas/BusqEmpresas.aspx",
                    "getCompany":"/esp/aspx/Empresas/FichaValor.aspx",
                    "getHistoricInfo":"/esp/aspx/Empresas/InfHistorica.aspx"}

attributes = {
            "search":"busq=",
            "isin":"ISIN=",
            "clv":"ClvEmis="
        }

tags = {
    "name": "name",
    "isin": "ISIN",
    "ticker": "ticker",
    "nominal": "nominal",
    "market": "market",
    "capital": "capital",
    "stocks" :"stocks"
}

historic = {
    "date" : "Date",
    "close": "Close",
    "ref" : "Reference",
    "vol": "Volume",
    "turnover": "Turnover",
    "last": "Last",
    "high": "High",
    "low": "Low",
    "avg": "Average",
}
