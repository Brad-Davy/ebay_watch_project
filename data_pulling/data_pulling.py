import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup


class data_puller:
    def __init__(
        self,
        query: str,
        box: str = "Yes",
        papers: str = "Yes",
        movement: str = "Mechanical",
    ):
        self.query = query
        self.output_file_save_tag = False
        self.completed_search_df = None
        self.current_search_df = None
        self.box = "Yes"
        self.papers = "Yes"
        self.movement = "Mechanical"
        self.movements = ["Quartz", "Mechanical"]

    def search_current_listings(self) -> None:
        url = f"https://www.ebay.co.uk/sch/i.html?_nkw={self.query}&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313"
        # url = f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={self.query}&_sacat=0"
        raw_output = self.make_soup(url)
        parsed_output = self.current_search_parse(raw_output)
        df = pd.DataFrame(parsed_output, columns=["title", "price", "link"])

        if self.output_file_save_tag:
            print("Saving to output.xml...", end="")
            df.to_xml(f"xml/{self.query}_current_listing.xml", index=False)

        else:
            print("The file did nto save.")

        self.current_search_df = df

    def search_completed_listings(self) -> None:
        url = f"https://www.ebay.co.uk/sch/i.html?_oaa=1&_dcat=31387&_fsrp=1&rt=nc&_from=R40&Movement={self.movement}&LH_Complete=1&LH_ItemCondition=4&LH_Sold=1&_nkw={self.query}&_sacat=0&Year%2520Manufactured=2020%252DNow&With%2520Manual%252FBooklet={self.papers}&With%2520Original%2520Box%252FPackaging={self.box}"
        raw_output = self.make_soup(url)
        parsed_output = self.completed_search_parse(raw_output)
        df = pd.DataFrame(
            parsed_output,
            columns=["title", "price", "link", "box", "papers", "movement"],
        )

        if self.output_file_save_tag:
            print("Saving to output.xml...", end="")
            df.to_xml(f"xml/{self.query}_completed_listing.xml", index=False)

        else:
            print("The file did nto save.")

        self.completed_search_df = df

    def current_search_parse(self, soup: BeautifulSoup) -> list[list[str]]:
        result = []
        items = soup.select(".srp-main--isLarge .srp-grid .s-item")
        for item in items:
            title = item.select_one(".s-item__title").getText(strip=True)
            price = item.select_one(".s-item__price").getText(strip=True)
            link = item.select_one(".s-item__link")["href"]
            result.append([title, price, link])
        return result

    def completed_search_parse(self, soup: BeautifulSoup) -> list[list[str]]:
        result = []
        titles = soup.select(".s-item__title")
        prices = soup.select(".s-item__price")
        links = soup.select(".s-item__link")

        for idx, title in enumerate(titles):
            result.append(
                [
                    title.getText(strip=True),
                    prices[idx].getText(strip=True),
                    links[idx]["href"],
                    self.box,
                    self.papers,
                    self.movement,
                ]
            )

        return result

    def make_soup(self, url: str) -> BeautifulSoup:
        r = requests.get(url)
        if r.status_code != 200:
            print("Failed to get data: ", r.status_code)
            sys.exit(1)
        return BeautifulSoup(r.text, "html.parser")


if __name__ == "__main__":
    dp = data_puller("Tag Huer Formula 1")
    dp.search_completed_listings()
