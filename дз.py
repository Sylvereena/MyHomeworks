import matplotlib.pyplot as plt

def read_file(file_path):
    file = open(file_path, 'r')
    data = file.readlines()
    file.close()
    return data

def process_data(data):
    sales_data = {}
    for line in data:
        pts = line.strip().split(',')
        period = pts[0].strip()
        sales = float(pts[1].strip().split()[0])  # Берем первое слово (число)

        if period not in sales_data:
            sales_data[period] = []

        sales_data[period].append(sales)


    return sales_data

def filter_data(data, threshold):
    filtered_data = {period: sum(sales) for period, sales in data.items() if sum(sales) > threshold}
    return filtered_data

def aggregate_data(data):
    total_sales = sum(data.values())
    return total_sales

def visualize_data(aggregated_data):
    periods = list(aggregated_data.keys())
    sales = list(aggregated_data.values())

    plt.bar(periods, sales)
    plt.xlabel('Периоды')
    plt.ylabel('Объем продаж')
    plt.title('Агрегированные данные')
    plt.tight_layout()
    plt.show()

file_paths = ['sales_data1.txt', 'sales_data2.txt', 'sales_data3.txt']
threshold = 100 

all_sales_data = {}

for file_path in file_paths:
    data = read_file(file_path)
    processed_data = process_data(data)

    for period, sales in processed_data.items():
        if period not in all_sales_data:
            all_sales_data[period] = []
        all_sales_data[period].extend(sales)

filtered_data = filter_data(all_sales_data, threshold)
aggregated_data = aggregate_data(filtered_data)

print(f'Общий объем продаж (превышающий {threshold}): {aggregated_data}')
visualize_data(filtered_data)