import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18146532"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b8d542b5487e2faf26828a52845b2e1")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://yogeshshahareias:bot1234@cluster0.237ghgl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
