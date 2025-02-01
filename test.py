import random
import datetime

def generate_data(num_records: int) -> list[dict]:
    """Генерирует список словарей с случайными данными."""
    data = []
    for _ in range(num_records):
        data.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "value": random.randint(1, 100)
        })
    return data

def save_data(data: list[dict], filename: str) -> None:
