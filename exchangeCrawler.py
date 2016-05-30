from lib.Crawler import *

def main():
    url = "https://www.ctbcbank.com/CTCBPortalWeb/toPage?id=TW_RB_CM_ebank_018001"
    crawler = ContentPsr(url)
    contentDict = dict()
    title = []

    mainTable = crawler.parseTagContent2List('#mainTable')
    content = crawler.extractSpecificContent2List(mainTable[0], 'tr')

    FD = crawler.extractSpecificContent2List(content[0], 'td')
    USD = crawler.extractSpecificContent2List(content[1], 'td')
    JPY = crawler.extractSpecificContent2List(content[2], 'td')
    EUR = crawler.extractSpecificContent2List(content[15], 'td')
    CNY = crawler.extractSpecificContent2List(content[20], 'td')

    contentDict['FD'] = []
    contentDict['USD'] = []
    contentDict['JPY'] = []
    contentDict['EUR'] = []
    contentDict['CNY'] = []
    contentDict['exchange_index'] = ['USD','JPY','EUR','CNY']


    for fd in FD:
        contentDict['FD'].append(fd.text)

    for usd in USD:
        contentDict['USD'].append(usd.text)

    for jpy in JPY:
        contentDict['JPY'].append(jpy.text)

    for eur in EUR:
        contentDict['EUR'].append(eur.text)

    for cny in CNY:
        contentDict['CNY'].append(cny.text)

    for fd_list in contentDict['FD']:
        print fd_list,

    print


    for index in contentDict['exchange_index']:
        for item in contentDict[index]:
            item = item.replace("\n",'').replace('/ '+index, '').strip()
            print item,
        print

if __name__ == '__main__':
    main()
