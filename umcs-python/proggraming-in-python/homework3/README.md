# Password Cracking Time Analysis

This project provides tools to measure and analyze the time it takes to crack passwords of various lengths using different character sets. It includes features for generating password combinations, timing the cracking process, and visualizing the results through charts.

## Features

- Generate and test password cracking times for user-selected character sets.
- Save cracking time results to a CSV file.
- Dynamically generate charts based on the results.
- Flexible character set selection using an interactive menu (curses-based or fallback text-based).

## Requirements

- Python 3.7+
- Installed Python libraries:
  - `matplotlib`

To install the required library, run:

```bash
pip install matplotlib
```

## Usage

### 1. Run the Password Cracking Script

The main script allows you to:

- Select a maximum password length.
- Specify the number of runs for better accuracy.
- Choose a character set interactively.
- Save cracking time results in a CSV file.

Example:

```bash
python main.py
```

### 2. Generate and Save Charts

Once the cracking time results are saved in a CSV file, the `ChartDrawer` class can be used to generate and save charts:

- It creates a line chart of "Password Length vs Average Cracking Time."
- Prompts you to save the chart as a PNG file.

### Example Workflow

1. Run the password cracking script:

   ```
   Enter the maximum password length: 6
   Enter the number of runs for better accuracy: 3
   Select a character set: (e.g., Digits, Lowercase Letters, etc.)
   ```

2. Generate and save the chart:

   ```
   Do you want to save the chart? (Y/N): Y
   ```

   The chart will be saved as a PNG file (e.g., `cracking_time_chart_digits.png`).

## File Structure

- `main.py`: Entry point to run the password cracking script.
- `chart_drawer.py`: Contains the `ChartDrawer` class for drawing charts.
- `cracking_times.csv`: CSV file storing the cracking time results.
- `README.md`: Documentation for the project.

## Example Output

- CSV file: Contains columns for password length and average cracking times.

  ```
  Length,Time (s)
  1,0.0012
  2,0.0034
  3,0.0156
  ```

- Chart: Line chart visualizing the relationship between password length and cracking time.
