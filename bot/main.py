# ============ Importação ============= #

from pyrogram import Client
from core.config import API_ID, API_HASH, BOT_TOKEN
from bot.handlers import register_handlers, logger

# ============== Código =============== #
app = Client("KaLLiaFinance_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
# antes do deploy trocar o nome do bot para algo mais apropriado
register_handlers(app) 

# ============= Execução ============== #
if __name__ == "__main__":
    app.run()
    logger.info('Bot iniciado.')
