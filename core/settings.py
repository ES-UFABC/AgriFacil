import os
from dotenv import load_dotenv

# load .env with increased verbosity:
load_dotenv(verbose = True)

PORT = os.getenv("PORT")
