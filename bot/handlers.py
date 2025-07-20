# ============ Importação ============= #
import logging

from pyrogram import Client, filters
from pyrogram.types import Message
from core.history import save_user_message
from llm.chat import get_llm_response


# ============== Código =============== #
logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

logger = logging.getLogger(__name__)

def register_handlers(app: Client):

    @app.on_message(filters.command("start"))
    async def start_handler(_, message: Message):
        logger.info(f'Usuário {message.from_user.id} ({message.from_user.first_name}) iniciou o bot.')
        await message.reply_text("Olá! Pode me mandar uma mensagem.")  # alterar essa mensagem antes do deploy

    @app.on_message(filters.text & ~filters.command("start"))
    async def text_handler(_, message: Message):
        user_id = message.from_user.id
        text = message.text

        # Exemplo de resposta simples
        save_user_message(user_id, "user", text)
        response = get_llm_response(user_id, text)
        save_user_message(user_id, "bot", response)
        # Exemplo de resposta simples

        await message.reply_text(response)
        logger.info(f'Resposta enviada para usuário {user_id}: {response}')
        
