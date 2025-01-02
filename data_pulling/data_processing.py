import numpy as np
from data_pulling import data_puller


class data_processor:
    def __init__(self, query: str):
        self.data_puller = data_puller(query)
        self.data_puller.search_current_listings()
        self.data_puller.search_completed_listings()

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

    def create_reccomendation(self):
        current_prices = self.convert_to_list(self.data_puller.current_search_df)
        completed_prices = self.convert_to_list(self.data_puller.completed_search_df)
        average_completed_price = np.mean(completed_prices)
        bin_size = 50
        counts, bin_edges = np.histogram(
            completed_prices,
            bins=np.arange(0, np.array(completed_prices).max() + bin_size, bin_size),
        )
        most_common_bin_index = np.argmax(counts)
        most_common_range = (
            bin_edges[most_common_bin_index],
            bin_edges[most_common_bin_index + 1],
        )
        std = np.std(completed_prices)
        print("/n")
        print("-" * 60)
        print(
            f"The average price for a completed listing is: \033[32m£{average_completed_price:.2f}\033[0m"
        )
        print(
            f"The median price for a completed listing is: \033[32m£{most_common_range}\033[0m"
        )
        print(
            f"The standard deviation for a completed listing is: \033[32m£{std:.2f}\033[0m"
        )
        print(
            f"Buy for under \033[32m£{average_completed_price - (std/2):.2f}\033[0m and sell over \033[32m£{average_completed_price + (std/2):.2f}\033[0m"
        )

        total_under_target_price = 0

        for items in current_prices:
            if items < average_completed_price - (std / 2):
                total_under_target_price += 1

        print(f"Total items under target price: {total_under_target_price}")

        print("-" * 60)


if __name__ == "__main__":
    dp = data_processor("Tag Huer Formula 1")
    dp.create_reccomendation()
