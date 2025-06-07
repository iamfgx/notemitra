import os
from supabase import create_client
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")  # Check your .env

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_to_supabase(file_obj, filename):
    print("Uploading file to:", filename)

    try:
        # Read file into bytes
        file_bytes = file_obj.read()

        # Upload file to Supabase
        result = supabase.storage.from_(SUPABASE_BUCKET).upload(
            path=filename,
            file=file_bytes,
            file_options={"content-type": "application/pdf"}
        )

        # Check if upload failed
        if hasattr(result, "error") and result.error:
            raise Exception(f"Upload failed: {result.error.message}")

    except Exception as e:
        raise Exception(f"Upload failed with error: {str(e)}")

    # Return public URL
    return f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"
