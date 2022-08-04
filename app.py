from loader import bot, storage
from src.services_manager import do_alarm
from loader import logger


async def on_shutdown(dp):
    await bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    try:
        executor.start_polling(dp)#, on_shutdown=on_shutdown)
    except KeyboardInterrupt:
        print('Вы завершили работу программы collector')
        logger.info('Program has been stop manually')
    except Exception as e:
        t_alarm_text = f'monitoring_tg_bot (app.py): {str(e)}'
        do_alarm(t_alarm_text)
        logger.error(f'Other except error Exception', exc_info=True)