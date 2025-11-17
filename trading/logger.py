from datetime import datetime

def log_message(msg):
    with open("./trader_logs.txt", "a") as log:
        log.write(f"{datetime.now()}: {msg}\n")
