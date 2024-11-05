# Split Bill App

A simple command-line application that helps users split a bill among friends, with the option to randomly select one friend as "lucky" who doesn't have to pay.

## Features

- Input the number of friends joining (including yourself).
- Enter names of friends.
- Specify the total bill amount.
- Randomly select one lucky friend who doesn't have to pay.
- Calculate and display how much each friend owes.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/split-bill-app.git
   cd split-bill-app
2. Run the application:
  python split_bill.py
  Follow the prompts in the terminal to enter the required information.

## Example Usage
  plaintext
  Enter the number of friends joining (including you): 3
  Enter the name of every friend (including you), each on a new line:
  Alice
  Bob
  Charlie
  Enter the total bill value:
  150
  Do you want to use the "Who is lucky?" feature? (Yes/No)
  Yes
  Charlie is the lucky one!
  {'Alice': 75.0, 'Bob': 75.0, 'Charlie': 0}
## License
This project is licensed under the MIT License. See the LICENSE file for details.
