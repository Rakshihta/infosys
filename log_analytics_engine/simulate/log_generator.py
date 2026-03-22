import random
from datetime import datetime

services = ["auth-service", "payment-service", "order-service", 
            "inventory-service", "notification-service"]

normal_levels = ["INFO", "WARNING"]
anomaly_levels = ["ERROR", "CRITICAL"]

normal_messages = [
    "Operation completed successfully",
    "User login successful",
    "Payment initiated successfully",
    "Inventory check completed",
    "Order placed successfully"
]

anomaly_messages = [
    "Critical system failure detected",
    "Database connection lost",
    "Authentication server down",
    "Inventory service crash detected",
    "Order service unavailable"
]

def generate_log(anomaly: bool = False) -> str:
    service = random.choice(services)
    
    if anomaly:
        level = random.choice(anomaly_levels)
        status = random.randint(900, 999)
        message = random.choice(anomaly_messages)
    else:
        level = random.choice(normal_levels)
        status = random.randint(200, 399)
        message = random.choice(normal_messages)
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"{level} {service} {status} {message} {timestamp}"


def generate_logs(n: int) -> list[str]:
    logs = []
    for i in range(n):
        if random.random() < 0.1:
            logs.append(generate_log(anomaly=True))
        else:
            logs.append(generate_log(anomaly=False))
    return logs