"""
MITRE-Mapped Phishing Campaign Logger (Simulated)
"""

import logging
from datetime import datetime

def log_campaign_event(event_type, details):
    logging.basicConfig(filename='campaign.log', level=logging.INFO)
    logging.info(f"{datetime.now().isoformat()} | {event_type}: {details}")

if __name__ == "__main__":
    log_campaign_event("CAMPAIGN_LAUNCH", "Outlook/GoPhish Campaign initiated")
    log_campaign_event("PHISHLET_ENABLED", "Evilginx microsoft365 phishlet enabled")
    log_campaign_event("INTERCEPT", "Credentials and session token captured from target")

    print("Phishing campaign simulation complete. See campaign.log for details.")
