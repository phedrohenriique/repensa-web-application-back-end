import os
import dotenv as de

## load_dotenv() searches for .env file with environment variables
## os.getenv() get the variables names

de.load_dotenv()

PORT=os.getenv("PORT")
DB_NAME=1