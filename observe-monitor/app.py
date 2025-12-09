import logging
from flask import Flask
import random
import time

app = Flask(__name__)

# Basic Logging Setup (OTEL hooks into this)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def roll_dice():
    # Log (Goes to Loki)
    logger.info("Rolling the dice...")

    # Metric (Goes to Mimir automatically via instrumentation)
    res = random.randint(1, 6)

    # Trace (Goes to Tempo automatically)
    time.sleep(0.1) # Simulate work

    if res == 6:
        logger.warning("Rolled a 6! Lucky!")

    return f"Rolled: {res}"

if __name__ == "__main__":
    app.run(port=5000)