import os
from dotenv import load_dotenv
from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

# Load environment variables from .env file
load_dotenv()

class SolanaManager:
    def __init__(self):
        self.__url = os.getenv('SOLANA_URL', '')
        self.__client = Client(self.__url)
        sender_scecret_key = os.getenv('SOLANA_SENDER_SECRET_KEY', '')
        self.__sender = Keypair().from_private_key(sender_scecret_key)

    @property
    def url(self):
        return self.__url
    
    @property
    def sender(self):
        return self.__sender
    
    def send_transaction(self, receiver_wallet_address: str, amount: int):
        receiver = PublicKey(receiver_wallet_address)

        instruction = transfer(
            from_public_key=self.__sender.public_key,
            to_public_key=receiver, 
            lamports=amount
        )
        transaction = Transaction(instructions=[instruction], signers=[self.__sender])

        result = self.__client.send_transaction(transaction)
        return result