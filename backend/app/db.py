from databases import Database
import os
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql: //pf_user:pf_pass@localhost:5432/personnel_fraud")
database = Database(DATABASE_URL)