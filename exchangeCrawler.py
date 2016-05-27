from lib.Crawler import *

def main():
    url = "https://www.ctbcbank.com/CTCBPortalWeb/toPage?id=TW_RB_CM_ebank_018001"
    crawler = ContentPsr(url)

    mainTable = crawler.parseTag('#mainTable')

    for item in mainTable:
        for item2 in item.select('tr'):
            for item3 in item2.select('td'):
                print item3.text.strip()


if __name__ == '__main__':
    main()
