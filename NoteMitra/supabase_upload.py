import os
from supabase import create_client
from django.core.files.storage import default_storage

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_to_supabase(file_obj, filename):
    res = supabase.storage.from_(SUPABASE_BUCKET).upload(filename, file_obj, {"content-type": "application/pdf"})
    if res.get("error"):
        raise Exception("Upload failed: " + str(res["error"]))
    return f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"
