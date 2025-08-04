from dotenv import load_dotenv 
load_dotenv()

import os
from datetime import datetime, timezone
from supabase import create_client 

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_ANON_KEY")

supabase = create_client(url, key)

created_at = datetime.now(timezone.utc)
# data = supabase.table("students_real").insert({"name": "Gerald", "school": "St Ignatius", "created_at": str(created_at)}).execute()
# data = supabase.table("students_real").update({"name": "Gerald"}).eq("id", 1).execute()

email: str = "tommygregory02@gmail.com"
password: str = "Cokezero9"

response = supabase.auth.sign_up({
    "email": email,
    "password": password
})