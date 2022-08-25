import subprocess
from loader import webhook_url, admin_id
import requests
import json
import asyncio
import sys
import os
from dotenv import load_dotenv
from tinkoff.invest import AsyncClient, PositionsResponse


def do_alarm(t_alarmtext):
    headers = {"Content-type": "application/json"}
    payload = {"text": f"{t_alarmtext}", "chat_id": f"{admin_id}"}
    requests.post(url=webhook_url, data=json.dumps(payload), headers=headers)


async def get_data_from_tink():
    load_dotenv()
    token = os.getenv('API_KEY')
    br_account_id = os.getenv('BR_ACCOUNT_ID')
    anti_cry_account_id = os.getenv('ANTI_CRY_ACCOUNT_ID')

    amounts = []
    expected_yields = []

    async with AsyncClient(token) as client:
        accounts = [br_account_id, anti_cry_account_id]
        for account in accounts:
            account_portfolio = await client.operations.get_portfolio(account_id=account)
            total_amount_rub = account_portfolio.total_amount_shares.units + account_portfolio.total_amount_bonds.units \
                               + account_portfolio.total_amount_etf.units + account_portfolio.total_amount_currencies.units \
                               + account_portfolio.total_amount_futures.units
            amounts.append(total_amount_rub)

            expected_yield = account_portfolio.expected_yield.units
            expected_yields.append(expected_yield)

        if expected_yields[0] > 0:
            text = f'Брокерский счет: {amounts[0]}, {expected_yields[0]}\n' \
                   f'Антикризисный счет: {amounts[1]}, {expected_yields[1]}\n' \
                   f'Общая сумма: {sum(amounts)}'

            return text

        else:
            text = f'Брокерский счет: {amounts[0]}, {expected_yields[0]}\n' \
                   f'Антикризисный счет: {amounts[1]}, {expected_yields[1]}\n' \
                   f'Общая сумма: {sum(amounts)}'

            return text
