from telegram import Update, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler
from unidecode import unidecode
from uuid import uuid4

import schedule
import threading

import os

from time_ir import Time


PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1858215359:AAG--4FDv3EN5K_hBFFjA2LNt0D8rZn849w'


def run_pending():
    schedule.run_pending()
    threading.Timer(1, run_pending).start()


class Bot:
    def __init__(self):
        self.my_calendar = None
        self.date_text: str = ''
        self.oghat_text: str = ''

        self.generate_text()
        schedule.every().day.at("00:01").do(self.generate_text)

        self.main()

    def generate_text(self):
        self.my_calendar = Time()
        self.date_text = f'🌞 تاریخ شمسی: ' \
                         f'<code>{unidecode(self.my_calendar.shamsi)}</code>\n\n' \
                         f'🎄 تاریخ میلادی: ' \
                         f'<code>{unidecode(self.my_calendar.miladi)}</code>\n\n' \
                         f'🌝 تاریخ قمری: ' \
                         f'<code>{unidecode(self.my_calendar.ghamari)}</code>\n\n' \
                         f'🔮 برج فلکی: ' \
                         f'<code>{self.my_calendar.borjfalaki}</code>\n\n'

        self.oghat_text = f'🌤 اذان صبح: ' \
                          f'<code>{unidecode(self.my_calendar.azan_sobh)}</code>\n\n' \
                          f'🌅 طلوع خورشید: ' \
                          f'<code>{unidecode(self.my_calendar.tolo_khorshid)}</code>\n\n' \
                          f'☀️ اذان ظهر: ' \
                          f'<code>{unidecode(self.my_calendar.azan_zohr)}</code>\n\n' \
                          f'🌆 غروب خورشید: ' \
                          f'<code>{unidecode(self.my_calendar.ghrob_khorshid)}</code>\n\n' \
                          f'🌛 اذان مغرب: ' \
                          f'<code>{unidecode(self.my_calendar.azan_maghreb)}</code>\n\n' \
                          f'✨ نیمه شب شرعی: ' \
                          f'<code>{unidecode(self.my_calendar.nime_shab)}</code>\n\n'

    @staticmethod
    def start_command(update: Update, context: CallbackContext) -> None:
        keyboard = [['📅 تقویم امروز']]
        update.message.reply_text(
            text='Hi!\n\n'
                 'Welcome',
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        )

    def get_today(self, update: Update, context: CallbackContext) -> None:
        text = self.date_text + '\n\n' + self.oghat_text
        update.message.reply_text(text, parse_mode='HTML')

    def inline_handler(self, update: Update, context: CallbackContext) -> None:
        text = self.date_text + '\n\n' + self.oghat_text
        result = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title='📅 تقویم امروز',
                input_message_content=InputTextMessageContent(
                    message_text=text,
                    parse_mode='HTML'
                )
            )
        ]
        update.inline_query.answer(result, cache_time=60)

    def main(self):
        updater = Updater(TOKEN, use_context=True)
        dpa = updater.dispatcher.add_handler

        dpa(CommandHandler('start', self.start_command, run_async=True))
        dpa(MessageHandler(Filters.regex(r'^📅 تقویم امروز'), self.get_today, run_async=True))
        dpa(InlineQueryHandler(self.inline_handler, run_async=True))

        updater.start_polling()
        # updater.start_webhook(listen="0.0.0.0", port=int(PORT),
        #                       url_path=TOKEN,
        #                       webhook_url='https://oghatgostarangharb.herokuapp.com/' + TOKEN)
        updater.idle()


if __name__ == '__main__':
    Bot()
