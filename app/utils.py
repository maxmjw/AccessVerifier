import json
import requests

ALLOWED_IPS_FILE = "app/data/allowed_ips.json"
AWS_IP_RANGES_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"


def load_allowed_ips():
    """
    Loading  JSON.
    """
    try:
        with open(ALLOWED_IPS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def update_allowed_ips(region=["eu-west-1", "eu-west-2", "eu-west-3"]):
    """
    Updating AWS EC2 IP list for specified region.
    """
    response = requests.get(AWS_IP_RANGES_URL)
    response.raise_for_status()

    data = response.json()
    region_ips = [
        prefix["ip_prefix"]
        for prefix in data.get("prefixes", [])
        if prefix["region"] in region and prefix["service"] == "EC2"
    ]

    with open(ALLOWED_IPS_FILE, "w") as file:
        json.dump(region_ips, file)


def extract_client_ip(headers: str):
    """
    Extract IP address from HTTP header.
    """
    for line in headers.splitlines():
        if "X-Forwarded-For" in line:
            return line.split(":")[1].strip()
    return None