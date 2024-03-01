import os
from dotenv import load_dotenv
from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

# Load environment variables from .env file
load_dotenv()

class SolanaManager:
    def __init__(self):
        url = os.getenv('SOLANA_URL')
        self.client = Client(url)
        self.__sender_scecret_key = os.getenv('SOLANA_SENDER_SECRET_KEY')

    def send_transaction(self, wallet_address: str, amount: int):
        sender = Keypair().from_private_key(self.__sender_scecret_key)
        receiver = PublicKey(wallet_address)

        instruction = transfer(
            from_public_key=sender.public_key,
            to_public_key=receiver, 
            lamports=amount
        )
        transaction = Transaction(instructions=[instruction], signers=[sender])

        result = self.client.send_transaction(transaction)
        return result