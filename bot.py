import env
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Logging config
logging.basicConfig(
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m"
)

# Dummy HTTP server for Heroku health checks
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

def start_web_server():
    import os
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), HealthCheckHandler)
    server.serve_forever()

# Start dummy server in a separate thread
threading.Thread(target=start_web_server, daemon=True).start()

# Pyrogram Client
app = Client(
    "Session_bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins={'root': 'StringSessionBot'},
)

# Main
if __name__ == "__main__":
    logging.info("Starting the bot")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")

    uname = app.me.username
    logging.info(f"@{uname} is now running!")

    idle()

    app.stop()
    logging.info("Bot stopped. Alvida!")