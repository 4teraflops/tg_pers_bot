from loguru import logger
from db import client

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='INFO', rotation='10 MB', compression='zip')


def get_metrics_from_actual_price():
    cursor = client.connect()
    metrics_from_actual_price = ['btc_rub', 'btc_usd', 'asset_actual_rub']
    data_from_actual_price = []
    for m in metrics_from_actual_price:
        cursor.execute(
            f'SELECT {m} FROM actual_price ORDER BY datetime DESC LIMIT 1'
        )
        data = str(cursor.fetchall()[0][0])
        #print(f'datatype: {type(data)}')
        data_from_actual_price.append(data)
    return data_from_actual_price


def get_data_from_asset():
    cursor = client.connect()
    cursor.execute(
        'SELECT asset_sum FROM asset ORDER BY check_datetime DESC LIMIT 1'
    )
    asset_sum = cursor.fetchall()[0][0]
    return round((asset_sum), 6)


def get_data_from_profit():
    cursor = client.connect()
    metrics_from_profit = ['profit_rub', 'profit_percent']
    data_from_profit = []

    for m in metrics_from_profit:
        cursor.execute(
            f'SELECT {m} FROM profit ORDER BY timestamp DESC LIMIT 1'
        )
        data = str(cursor.fetchall()[0][0])
        data_from_profit.append(data)

    return data_from_profit


def collect_dict():
    result_metrics_dict = {}
    actual_price_metrics = get_metrics_from_actual_price()
    result_metrics_dict['btc_rub'] = actual_price_metrics[0]
    result_metrics_dict['btc_usd'] = actual_price_metrics[1]
    result_metrics_dict['asset_actual_rub'] = actual_price_metrics[2]

    profit_metrics = get_data_from_profit()
    result_metrics_dict['profit_rub'] = profit_metrics[0]
    result_metrics_dict['profit_percent'] = profit_metrics[1]

    return result_metrics_dict
