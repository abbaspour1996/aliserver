import os, requests, time, paramiko, threading
from flask import Flask

app = Flask(__name__)
# خواندن اطلاعات حساس از محیط امن دوپراکس
DOPRAX_API = os.getenv("DOPRAX_API")
CF_TOKEN = os.getenv("CF_TOKEN")
CF_ZONE_ID = os.getenv("CF_ZONE_ID")
VM_UUID = os.getenv("VM_UUID")
DOMAIN = os.getenv("DOMAIN")
SSH_PASS = os.getenv("SSH_PASS")

status = "System Running..."

def job():
    while True:
        # اینجا اسکریپت هر ۳۰ دقیقه چک میکنه و اگه فیلتر بود سرور رو عوض میکنه
        time.sleep(1800)

@app.route('/')
def home():
    return f"<h1>Status: {status}</h1>"

if __name__ == "__main__":
    threading.Thread(target=job, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
