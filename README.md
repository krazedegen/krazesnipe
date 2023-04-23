# Krazesnipe
Krazesnipe is a single account token sniping bot for PancakeSwap, built with Python and Web3. The bot monitors a specific token and buys it automatically when liquidity is added to the pair on PancakeSwap. This README will guide you through the setup and usage of Krazesnipe.

Prerequisites
Before using Krazesnipe, make sure you have the following prerequisites installed:
Python 3.7 or higher: [Download](https://www.python.org/downloads/)
Pip: [Installation Guide](https://pip.pypa.io/en/stable/installation/)

Installation
1. Clone the Krazesnipe repository to your local machine.
git clone https://github.com/krazedegen/krazesnipe.git

2. Change the current directory to the Krazesnipe folder.
cd krazesnipe

3. Install the required Python packages.
pip install -r requirements.txt

4. Create a .env file to store your sensitive information. Replace ENTER_YOUR_... with your actual information.
API_KEY=ENTER_YOUR_API_KEY
NODE_URL=ENTER_YOUR_NODE_URL
SENDER_ADDRESS=ENTER_ADDRESS_YOU_WANT_TO_USE_TO_SNIPE_TOKEN
PRIVATE_KEY=ENTER_YOUR_PRIVATE_KEY

Usage


Open the krazesnipe.py file in your favorite code editor and update the following variables with the appropriate token addresses:

tokenA = web3.toChecksumAddress('0x20e7256Db0e517E387b494457e4Df67A624f1968') # Token to snipe
tokenB = wbnbTestnet # Token to buy with (e.g., WBNB, BUSD)

Set the amount of tokens you want to buy and the gas price by updating the following line in the buy() function:

'value': web3.toWei(0.01, 'ether'), # Change 0.01 to the amount you want to buy
'gasPrice': web3.toWei('5', 'gwei'), # Change '5' to your desired gas price

Run Krazesnipe.

python krazesnipe.py

The bot will now monitor the token pair for liquidity. When liquidity is detected, Krazesnipe will attempt to buy the specified token.



DISCLAIMER:

The use of this script comes with no guarantees or warranties, express or implied.
The user assumes all risk, including but not limited to the risk of financial loss,
associated with the use of this script. The author is not responsible for any losses
or damages, direct or indirect, that may result from the use of this script.

By using this script, you acknowledge that you have read and understood this disclaimer,
and you agree to indemnify and hold harmless the author for any liability or claims that
may arise from the use of this script.
