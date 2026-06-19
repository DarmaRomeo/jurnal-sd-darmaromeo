import os
from dotenv import load_dotenv

# Memuat variabel dari .env
load_dotenv()

# Memanggil DB_PASSWORD
db_password = os.getenv("DB_PASSWORD")
print(f"Password database terdeteksi: {db_password}")