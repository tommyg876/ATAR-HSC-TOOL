from dotenv import load_dotenv 
load_dotenv()

import os
from supabase import create_client, Client
from gotrue import SyncGoTrueClient  # ← Changed this line

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_ANON_KEY") 

supabase = create_client(url, key)

email: str = "tommygregory360@gmail.com"
password: str = "Cokezero9"

session = None

data = supabase.table("students_real").select("*").execute()
print ("Data before sign in: ", data)

try:
    session = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })
    print("User:", session.user)
except Exception as e:
    print(f"Error: {e}")
print (session.session.access_token)

data = supabase.table("students_real").select("*").execute()
print ("Data before sign in: ", data)