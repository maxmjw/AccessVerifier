import time
from app.utils import update_allowed_ips

def update_ips():
    update_allowed_ips()
    
def schedule_ip_updates():
    while True:
        print("Updating IP list...")
        update_allowed_ips()
        print("Updating finished, .")
        time.sleep(86400)  # 24 godziny


if __name__ == "__main__":
    schedule_ip_updates()