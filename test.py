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
    """Сохраняет данные в JSON-файл."""
    import json
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

if __name__ == "__main__":
    num_records = 10
    data = generate_data(num_records)
    save_data(data, "random_data.json")
    print(f"Сгенерировано {num_records} записей и сохранены в random_data.json")