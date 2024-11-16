import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Официант", callback_data='oficiant'), InlineKeyboardButton("Хостес", callback_data='hostes')],
        [InlineKeyboardButton("Повар", callback_data='povar'), InlineKeyboardButton("Бармен", callback_data='barmen')],
        #[InlineKeyboardButton("Назад", callback_data='back')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Путь к локальному файлу
    photo_path = "foto.jfif"
    
    # Отправка фото
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(photo_path, 'rb'),
        caption="Привет, рады видеть в команде ресторана 'Перк'. Наш адрес г. Саратов, ул. Вольская, д. 63/69. Телефон для связи +79878250490. Телефон для обратной связи о стажировке. Выбери должность и ознакомься с памяткой",
        #reply_markup = reply_markup
     )

    await update.message.reply_text('Привет, рады видеть в команде ресторана "Перк". Наш адрес г. Саратов, ул. Вольская, д. 63/69. Телефон для связи +79878250490. Телефон для обратной связи о стажировке +79649987878 - Ольга. Выбери должность и ознакомься с памяткой', reply_markup=reply_markup)

# Функция для обработки нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query    
    await query.answer()

    # Ответ на выбранный вариант
    if query.data == 'oficiant':
        text = "Вы выбрали должность: Официант. Нажмите 'Назад', чтобы вернуться в меню."
        back_keyboard = [[InlineKeyboardButton("Назад", callback_data="назад")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == 'hostes':
        text = "Вы выбрали должность: Хостес. Нажмите 'Назад', чтобы вернуться в меню."
        back_keyboard = [[InlineKeyboardButton("Назад", callback_data="назад")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == 'povar':
        text = "Вы выбрали должность: Повар. Нажмите 'Назад', чтобы вернуться в меню."
        back_keyboard = [[InlineKeyboardButton("Назад", callback_data="назад")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == 'barmen':
        text = "Вы выбрали должность: Бармен. Нажмите 'Назад', чтобы вернуться в меню."
        back_keyboard = [[InlineKeyboardButton("Назад", callback_data="назад")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == "назад":
        # Возвращаем меню выбора кнопок
        caption="Привет, рады видеть в команде ресторана 'Перк'. Наш адрес г. Саратов, ул. Вольская, д. 63/69. Телефон для связи +79878250490. Телефон для обратной связи о стажировке. Выбери должность и ознакомься с памяткой",
        keyboard = [
                [InlineKeyboardButton("Официант", callback_data='oficiant'), InlineKeyboardButton("Хостес", callback_data='hostes')],
                [InlineKeyboardButton("Повар", callback_data='povar'), InlineKeyboardButton("Бармен", callback_data='barmen')],
                #[InlineKeyboardButton("Назад", callback_data='back')]
            ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(caption=caption, reply_markup=reply_markup) 

# Основная функция
async def main():
    application = Application.builder().token("7553661995:AAFcB1kBgNEwqfx2BtyhaJRe9aTtyt4v_tY").build()

    # Обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()  # Позволяет работать с asyncio.run() в интерактивной среде
    asyncio.run(main())
