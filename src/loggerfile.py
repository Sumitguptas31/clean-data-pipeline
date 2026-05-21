import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename="logs/app.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)