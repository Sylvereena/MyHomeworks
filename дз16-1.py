def print_info(name, **params):
    print(f"имя: {name}")
    for i, value in params.items():
        print(f"{i}: {value}")

print_info("Иван", возраст=30, профессия="инженер", город="Москва")