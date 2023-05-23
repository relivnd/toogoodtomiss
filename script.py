import os
from tgtg import TgtgClient
from dotenv import load_dotenv

load_dotenv()

TGTG_EMAIL = os.getenv('TGTG_EMAIL')

client = TgtgClient(email=TGTG_EMAIL)
credentials = client.get_credentials()

print(credentials)