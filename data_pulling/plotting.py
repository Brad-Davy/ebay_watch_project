import matplotlib.pyplot as plt
from data_pulling import data_puller
import numpy as np


class data_plotter(data_puller):
    def __init__(self, query: str):
        super().__init__(query)
        self.search_current_listings()
        self.search_completed_listings()

    def try_float(self, value) -> float:
        can_float = True
        try:
            float(value)
        except:
            can_float = False

        return can_float

    def convert_to_list(self, data_frame) -> list:
        prices = data_frame["price"].str.replace("£", "").str.replace("$", "")
        prices_string = (prices.str.replace(",", "")).to_list()
        prices_float = []
        for price in prices_string:
            if self.try_float(price):
                prices_float.append(float(price))

        return prices_float

    def plot_current_listings(self) -> None:
        current_prices = self.convert_to_list(self.current_search_df)
        plt.scatter(range(0, len(current_prices)), current_prices)
        plt.title(f"Current listings for {self.query}")
        plt.ylabel("Price (£)")
        plt.show()

    def plot_completed_listings(self) -> None:
        completed_prices_float = self.convert_to_list(self.completed_search_df)
        average_price = np.mean(completed_prices_float)
        std = np.std(completed_prices_float)
        plt.scatter(range(0, len(completed_prices_float)), completed_prices_float)
        plt.axhline(y=average_price, color="r", linestyle="--")
        plt.fill_between(
            range(0, len(completed_prices_float)),
            average_price - std,
            average_price + std,
            color="r",
            alpha=0.2,
        )
        plt.title(f"Completed listings for {self.query}")
        plt.ylabel("Price (£)")
        plt.show()

    def bar_chart(self) -> None:
        completed_prices_float = self.convert_to_list(self.completed_search_df)
        plt.hist(completed_prices_float, bins=20, color="b", alpha=0.7)
        plt.show()


data_plotter("Tag Huer Formula One").bar_chart()
# Print text in different colors
