import json
import yaml
import logging
import requests
from cryptography.fernet import Fernet
from logging.handlers import RotatingFileHandler


def setup_logger(log_file, max_log_size, backup_count):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger = logging.getLogger("bmc_alert_fetcher_logger")

    handler = RotatingFileHandler(
        log_file, maxBytes=max_log_size, backupCount=backup_count
    )
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


logger = setup_logger("/var/log/bmc_alert_fetcher.log", 1024 * 1024 * 1024, 5)


def decrypt_password(key, encrypted_password):
    """
    Decrypts an encrypted message using the provided key.
    """
    f = Fernet(key)
    decrypted_password = f.decrypt(
        encrypted_password
    ).decode()  # Decode from bytes to string
    return decrypted_password


def notify_feishu_bot(message):
    config_info = yaml.safe_load(file)
    webhook_url = config_info["bmc_credentials"]["bmc_ips"]
    payload = {"msg_type": "text", "content": {"text": message}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        logger.info(
            f"Failed to send alert to Feishu status code: {response.status_code}"
        )
    else:
        logger.error("Failed to send alert to Feishu")
