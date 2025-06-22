API_ID = 24249014
API_HASH = "0a8d55a05546869565d1c1ab07e2234f"
BOT_TOKEN = "7742667419:AAEvIkYBCr1qHVslZVT4fkazgcxgqK5ZX9s"
DATABASE_URL = "mongodb+srv://zuiiixx:zuiiixx@cluster0.jsrns5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUST_JOIN = ""  # Or set your channel ID like "@yourchannel"

# Validation
if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")
