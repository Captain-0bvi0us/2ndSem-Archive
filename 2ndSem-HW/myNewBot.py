import logging
import datetime
import json
from telegram.ext import CommandHandler, Application

logging.basicConfig(level=logging.INFO)

TOKEN = '7561355539:AAEgsXY7aHkShNfDEYJvA1UqYPVHFIVKFqU'

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Бот запущен! \n\n'
                                                                        'Доступные команды: \n'
                                                                        '/add_event - добавить новое событие (пример: /add_event Название события, Дата события) \n'
                                                                        '/remind - напомнить о событиях на сегодня \n'
                                                                        '/clear - очистить все события до сегодняшнего дня \n'
                                                                        '/help - показать это меню')
def save_events(events):
    with open('2ndSem-HW/events.json', 'w') as f:
        json.dump(events, f, indent=4)

def load_events():
    try:
        with open('2ndSem-HW/events.json', 'r') as f:
            events = json.load(f)
            for event_name, event_date in events.items():
                events[event_name] = datetime.datetime.strptime(event_date, '%Y-%m-%d').date()
            return events
    except json.JSONDecodeError:
        return {}
    except FileNotFoundError:
        return {}
    
events = load_events()

def get_events():
    return events

async def add_event(event_name, event_date):
    events[event_name] = event_date.strftime('%Y-%m-%d')  # Преобразовать дату в строку
    save_events(events)

async def add_event_handler(update, context):
    message_text = update.message.text
    if message_text.startswith('/add_event '):
        message_text = message_text.replace('/add_event ', '')
    parts = message_text.split(', ')
    if len(parts) != 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Неправильный формат сообщения. Пожалуйста, отправьте сообщение в формате "Название события, Дата события"')
        return
    event_name = parts[0]
    event_date = parts[1]
    try:
        event_date = datetime.datetime.strptime(event_date, '%Y-%m-%d').date()
    except ValueError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Неправильный формат даты. Пожалуйста, отправьте дату в формате YYYY-MM-DD')
        return
    try:
        await add_event(event_name, event_date)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Событие добавлено!')
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Ошибка добавления события: ' + str(e))

async def remind(update, context):
    events = load_events()
    today = datetime.date.today()
    today_events = [event for event, date in events.items() if date == today]

    if not today_events:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Событий нет сегодня')
    else:
        for event in today_events:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Напоминание: {event}')
            
async def clear_before_today(update, context):
    eventsForClear = load_events()
    today = datetime.date.today()
    new_events = {}
    for event, date in eventsForClear.items():
        if date >= today:
            new_events[event] = date.strftime('%Y-%m-%d') 
    save_events(new_events)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Записи до сегодняшнего дня очищены')

async def help(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Доступные команды: \n'
                                                                        '/add_event - добавить новое событие (пример: /add_event Название события, Дата события) \n'
                                                                        '/remind - напомнить о событиях на сегодня \n'
                                                                        '/clear - очистить все события до сегодняшнего дня \n'
                                                                        '/help - показать это меню')

def main():
    aplication = Application.builder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    gadd_event_handler = CommandHandler('add_event', add_event_handler)
    remind_handler = CommandHandler('remind', remind)
    clear_handler = CommandHandler('clear', clear_before_today)
    help_handler = CommandHandler('help', help)

    aplication.add_handler(start_handler)
    aplication.add_handler(gadd_event_handler)
    aplication.add_handler(remind_handler)
    aplication.add_handler(clear_handler)
    aplication.add_handler(help_handler)

    try:
        aplication.run_polling()
    except Exception as e:
        print('Ошибка запуска приложения: ' + str(e))

if __name__ == '__main__':
    main()