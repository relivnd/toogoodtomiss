from tgtg import TgtgClient
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

client = TgtgClient(email="")
credentials = client.get_credentials()

print(credentials)