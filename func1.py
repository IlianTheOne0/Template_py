def main():
    try:
        temp = [1, 'apple', 2, 3, 'banana']

        for item in temp:
            if type(item).__name__ == 'int': # if type(item) == int: pass
                item *= 2
            print(item)

        for i in range(len(temp)):
            if i % 2 == 0:
                temp[i] *= 2
            print(temp[i])
    except Exception as e:
        print(f'Error: {e}')