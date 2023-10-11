from loader import logger


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    try:
        executor.start_polling(dp, skip_updates=False, on_shutdown=on_shutdown)
    except KeyboardInterrupt:
        print('Вы завершили работу программы collector')
        logger.info('Program has been stop manually')
