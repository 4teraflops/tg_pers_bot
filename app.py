from loader import bot
from src import services_manager
from loader import logger
import asyncio
import aioschedule
from handlers.users.daily_reporter_handlers import start_daily_pool


async def daily_pool_scheduler():
    #aioschedule.every().day.at("23:00").do(start_daily_pool)
    aioschedule.every().minute.do(start_daily_pool)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    asyncio.create_task(daily_pool_scheduler())


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    try:
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    except KeyboardInterrupt:
        print('Вы завершили работу программы collector')
        logger.info('Program has been stop manually')
    except Exception as e:
        t_alarm_text = f'personal_tg_bot (app.py): {str(e)}'
        services_manager.do_alarm(t_alarm_text)
        logger.error(f'Other except error Exception', exc_info=True)
