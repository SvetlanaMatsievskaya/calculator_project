from datetime import datetime as dt



def result_logger(data, result):
    left_value, operation, right_value = data
    data_str = f'{str(left_value)} {operation} {str(right_value)}'
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} результат :{}\n'.format(
            time, data_str, result))