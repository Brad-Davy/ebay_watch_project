import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup


class data_puller:
    def __init__(self, query: str):
        self.query = query
        self.output_file_save_tag = True
        self.output_file_name = f"{self.query}_output.xml"

    def search_current_listings(self) -> None:
        url = f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={self.query}&_sacat=0"
        raw_output = self.make_soup(url)
        parsed_output = self.parse(raw_output)
        df = pd.DataFrame(parsed_output, columns=["title", "price", "link"])

        if self.output_file_save_tag:
            print("Saving to output.xml...", end="")
            df.to_xml(self.output_file_name, index=False)

        else:
            print(df)

    def search_completed_listings(self) -> None:
        url = f"https://www.ebay.co.uk/sch/i.html?_fsrp=1&rt=nc&_from=R40&_nkw={self.query}&_sacat=0&LH_Sold=1"

        raw_output = self.make_soup(url)
        parsed_output = self.parse(raw_output)

        df = pd.DataFrame(parsed_output, columns=["title", "price", "link"])

        if self.output_file_save_tag:
            print("Saving to output.xml...", end="")
            df.to_xml(self.output_file_name, index=False)

        else:
            print(df)

    def make_soup(self, url: str) -> BeautifulSoup:
        r = requests.get(url)
        if r.status_code != 200:
            print("Failed to get data: ", r.status_code)
            sys.exit(1)
        return BeautifulSoup(r.text, "html.parser")

    def parse(self, soup: BeautifulSoup) -> list[list[str]]:
        result = []
        items = soup.select(".srp-main--isLarge .srp-grid .s-item")
        for item in items:
            title = item.select_one(".s-item__title").getText(strip=True)
            price = item.select_one(".s-item__price").getText(strip=True)
            link = item.select_one(".s-item__link")["href"]
            result.append([title, price, link])
        return result


if __name__ == "__main__":
    dp = data_puller("Tag Huer Formula 1")
    dp.search_current_listings()
