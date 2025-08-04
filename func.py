import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)
func = supabase.functions  # 🔥 No parentheses

# ✅ Invoke edge function synchronously
resp = func.invoke("hello-world", invoke_options={"body": {}})
print(resp)
