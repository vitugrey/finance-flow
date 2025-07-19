# ============ Importação ============= #
import base64
import io
import logging
import asyncio
import os
from dotenv import load_dotenv

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.enums import ChatAction

from ..llm.chat import AgentTranscription

load_dotenv()
# ============== Código =============== #
app = Client(
    "financeflow_bot",
    api_id=int(os.getenv("TELEGRAM_API_ID")),
    api_hash=os.getenv("TELEGRAM_API_HASH"),
    bot_token=os.getenv("TELEGRAM_BOT_TOKEN")
)


# class TelegramBot:
#     def __init__(self):
#         logging.basicConfig(
#             level=logging.INFO,
#             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         )
#         self.logger = logging.getLogger(__name__)
#         self.app = Client(
#             api_id='',  # colocar em um arquivo .env
#             api_hash='',  # colocar em um arquivo .env
#             bot_token='',  # colocar em um arquivo .env
#             name=''  # colocar em um arquivo .env
#         )
#         self.agent = AgentTranscription()

#         self._setup_handlers()

#     async def start(self, client: Client, message: Message):
#         await message.reply_text('Ola! EU sou KaLLia! Sua LLM Financeira.')
#         self.logger.info(f'Usuário {message.from_user.id} ({message.from_user.first_name}) iniciou o bot.')

#     async def handle_photo(self, client: Client, message: Message):
#         telegram_id = message.from_user.id
#         try:
#             await client.send_chat_action(telegram_id, ChatAction.UPLOAD_PHOTO)

#             # Baixa a foto
#             photo_path = await client.download_media(message.photo.file_id)

#             # Chama o agent
#             result = self.agent.process_image_structured(photo_path)

#             await message.reply_text(
#                 f"descricao: {result['description']}\nvalor: {result['value']}\ncategoria_id: {result['category_id']}\ndata: {result['date']}\nis_credit: {result['is_credit']}\nis_fixed_expense: {result['is_fixed_expense']}\ntransaction_type: {result['transaction_type']}\ncreated_at: {result['created_at']}\nupdated_at: {result['updated_at']}"
#             )

#         except Exception as e:
#             await message.reply_text(f"Erro ao processar imagem: {str(e)}")
#             self.logger.exception("Erro ao lidar com foto")

#     def _setup_handlers(self):
#         self.app.add_handler(MessageHandler(self.start, filters.command('start')))
#         self.app.add_handler(MessageHandler(self.handle_photo, filters.photo))

#     def run(self):
#         self.logger.info('Bot iniciado.')
#         self.app.run()


# ============= Execução ============== #
if __name__ == "__main__":
    app.run()
