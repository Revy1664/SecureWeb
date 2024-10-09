import os
from dotenv import load_dotenv


# load environment variables
load_dotenv()

# database configuration
db_config = {
	"host": os.environ.get("host"),
	"user": os.environ.get("user"),
	"password": os.environ.get("password"),
	"database": os.environ.get("database"),
}
