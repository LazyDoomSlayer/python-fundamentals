import csv
import itertools
import time
from typing import List, Tuple

from chart import ChartDrawer
from menu import CharsetSetSelector, CharacterSet


class PasswordCracker:
    """
    A class for generating password combinations, hashing them, and measuring
    the time required to crack passwords of varying lengths.
    """

    def __init__(self) -> None:
        """
        Initialize the PasswordCracker class.

        Attributes:
            times (List[Tuple[int, float]]):
                A list to store the elapsed time for each password length.
        """
        self.times: List[Tuple[int, float]] = []

    def _generate_combination(self, character_set: str, length: int) -> None:
        """
        Generate and print all combinations of a given character set and length.

        Args:
            character_set (str): The set of characters to use for generating combinations.
            length (int): The length of the combinations to generate.

        Returns:
            None
        """
        for combination in itertools.product(character_set, repeat=length):
            password = "".join(combination)
            # print(combination)
            # print(password)

    def measure_cracking_time(
        self, character_set: str, max_length: int, runs: int
    ) -> None:
        """
        Measure the average time taken to generate all combinations for each password length
        from 1 up to the specified maximum length.

        Args:
            character_set (str): The set of characters to use for generating combinations.
            max_length (int): The maximum length of combinations to measure.
            runs (int): Number of repetitions for each length to calculate the average time.

        Returns:
            None
        """
        for length in range(1, max_length + 1):
            run_times = []
            for _ in range(runs):
                start_time = time.time()

                print(f"Measuring cracking time for length {length}, run {_ + 1}...")
                self._generate_combination(character_set, length)

                end_time = time.time()
                elapsed_time = round(end_time - start_time, 4)
                run_times.append(elapsed_time)

            average_time = round(sum(run_times) / runs, 4)
            self.times.append((length, average_time))

    def save_times_to_csv(self, filename: str) -> None:
        """
        Save the recorded elapsed times to a CSV file.

        Args:
            filename (str): The name of the CSV file to save the data.

        Returns:
            None
        """
        with open(filename, mode="w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Length", "Time (s)"])
            csv_writer.writerows(self.times)
        print(f"Times saved to {filename}")

    def get_user_input(self) -> Tuple[int, int, CharacterSet]:
        """
        Get user input for the maximum password length, the number of runs, and character set selection.

        Returns:
            Tuple[int, int, CharacterSet]: Maximum password length, number of runs, and selected character set.
        """
        user_input_max_length = int(input("Enter the maximum password length: "))
        user_input_runs = int(input("Enter the number of runs for better accuracy: "))

        user_input_selector = CharsetSetSelector()
        user_input_selected_character_set = user_input_selector.get_selection()

        return user_input_max_length, user_input_runs, user_input_selected_character_set


if __name__ == "__main__":
    csv_file_name = "cracking_times.csv"
    chart_image_name = "cracking_times_chart.png"

    cracker = PasswordCracker()
    max_length, runs, character_set = cracker.get_user_input()

    cracker.measure_cracking_time(character_set.value[0], max_length, runs)
    cracker.save_times_to_csv(csv_file_name)

    title = (f"Average Cracking Time for {character_set.value[0]} vs Password Length",)
    drawer = ChartDrawer(csv_file=csv_file_name)
    drawer.load_data_from_csv()
    drawer.draw_and_save_chart(output_file=chart_image_name, title=title)
