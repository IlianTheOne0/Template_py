def loop():
    items = []
    item_count = []
    item_price = []

    try:
        while True:
            item = input('Item: ')

            if item == 'fin':
                break

            total = int(input('Total: '))
            price = float(input('Total: '))

            items.append(item)
            item_count.append(total)
            item_price.append(price)

        for i in range(len(items)):
            print(f'{items[i]}: {item_count[i]} x {item_price[i]} = {item_count[i]}')
    except Exception as e:
        print(f'Error: {e}')

def main():
    loop()