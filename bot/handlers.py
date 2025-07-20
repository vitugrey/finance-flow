# ============ Importação ============= #
import logging

from pyrogram import Client, filters
from pyrogram.types import Message
from llm.chat import run_llm_with_history


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
        response = run_llm_with_history(user_id, text)
        # Exemplo de resposta simples

        await message.reply_text(response)
        logger.info(f'Resposta enviada para usuário {user_id}: {response}')
        
