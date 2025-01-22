import csv
from typing import List, Tuple

import matplotlib.pyplot as plt


class ChartDrawer:
    """
    A class for drawing charts from CSV data and saving them as PNG files.
    """

    def __init__(self, csv_file: str):
        """
        Initialize the ChartDrawer with the CSV file path.

        Args:
            csv_file (str): Path to the CSV file containing chart data.
        """
        self.csv_file = csv_file
        self.data: List[Tuple[int, float]] = []

    def load_data_from_csv(self) -> None:
        """
        Load data from the CSV file.

        The CSV should have two columns: 'Length' and 'Time (s)'.
        """
        with open(self.csv_file, mode="r") as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                self.data.append((int(row[0]), float(row[1])))

    def draw_and_save_chart(
        self,
        output_file: str = "chart.png",
        title="Average Cracking Time vs Password Length",
    ) -> None:
        """
        Draw the chart from the loaded data and save it as a PNG file.

        Args:
            output_file (str): The file name to save the chart. Defaults to 'chart.png'.
        """
        if not self.data:
            raise ValueError(
                "No data available. Please load data from a CSV file first."
            )

        lengths, times = zip(*self.data)

        plt.figure(figsize=(8, 6))
        plt.plot(lengths, times, marker="o", label="Cracking Time")
        plt.title(title)
        plt.xlabel("Password Length")
        plt.ylabel("Average Time (s)")
        plt.grid(True)
        plt.legend()

        save_chart = input("Do you want to save the chart? (Y/N): ").strip().lower()
        if save_chart == "y":
            plt.tight_layout()
            plt.savefig(output_file)
            print(f"Chart saved as {output_file}")
        else:
            print("Chart not saved.")
        plt.close()
