import random
import time
import json
import string
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='traffic_generator.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Function to generate a random IP address
def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate random domains
def generate_domain():
    length = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) + ".com"

# Function to generate user creation frequency
def generate_user_creation():
    return random.randint(1, 100)

# Function to generate domain permutation as threat
def generate_domain_permutation(domain):
    return ''.join(random.sample(domain, len(domain)))

# Function to generate a random port number
def generate_port():
    return random.randint(1024, 65535)

# Function to generate a random protocol
def generate_protocol():
    return random.choice(["HTTP", "HTTPS", "FTP", "SSH", "SMTP", "IMAP"])

# Function to simulate network traffic
def generate_traffic():
    source_ip = generate_ip()
    destination_ip = generate_ip()
    domain = generate_domain()
    user_creation_frequency = generate_user_creation()
    domain_permutation_threat = generate_domain_permutation(domain)
    source_port = generate_port()
    destination_port = generate_port()
    protocol = generate_protocol()

    traffic_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "domain": domain,
        "user_creation_frequency": user_creation_frequency,
        "domain_permutation_threat": domain_permutation_threat,
        "source_port": source_port,
        "destination_port": destination_port,
        "protocol": protocol
    }
    return traffic_data

if __name__ == "__main__":
    while True:
        traffic = generate_traffic()
        traffic_json = json.dumps(traffic)
        print(traffic_json)
        logging.info(traffic_json)
        time.sleep(random.uniform(0.1, 1))  # Simulate varying traffic intervals
