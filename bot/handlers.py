# ============ Importação ============= #
import logging
import os
import json

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.ocr import extract_text_from_image
from utils.pdf import extract_text_from_pdf
from llm.chat import (
    get_response_with_history,
    get_estructured_json)

# ============== variaveis =============== #
user_data = {}  # estrutura melhor depois


# ============== Código =============== #
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def register_handlers(app: Client):

    @app.on_message(filters.command("start"))
    async def start_handler(_, message: Message):
        user_id = message.from_user.id
        user_namer = message.from_user.first_name
        logger.info(f'User({user_id}) -> {user_namer} iniciou o bot.')
        await message.reply_text(f"Olá {user_namer}! Eu sou a Kallia Finance, sua nova gerente financeira.")
        # alterar essa mensagem antes do deploy

    @app.on_message(filters.command("confirmar"))
    async def confirm_handler(_, message: Message):
        user_id = message.from_user.id
        if user_id in user_data:
            transaction_info = user_data[user_id]
            # Aqui você pode adicionar a lógica
            
            # Aqui você pode adicionar a lógica
            await message.reply_text(f"Transação confirmada:\n\n{json.dumps(transaction_info, indent=4)}")
            logger.info(f'User({user_id}) -> Confirmou a transação: {transaction_info}')


    @app.on_message(filters.text & ~filters.command("start"))
    async def text_handler(_, message: Message):
        user_id = message.from_user.id
        text = message.text
        logger.info(f'User({user_id}) -> {text}')

        # Exemplo de resposta simples
        response = get_response_with_history(user_id, text)
        # Exemplo de resposta simples

        await message.reply_text(response)
        logger.info(f'Bot({user_id}): -> {response}')


    @app.on_message(filters.document & filters.private)
    async def handle_pdf(_, message: Message):
        user_id = message.from_user.id
        file = await app.download_media(message)
        logger.info(f'User({user_id}) -> Enviou o arquivo: {file}')
        if file.endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file)
            response = get_estructured_json(user_id, extracted_text)
            await message.reply_text(response)
            os.remove(file)
        logger.info(f'Bot({user_id}): -> {response}')

    @app.on_message(filters.photo & filters.private)
    async def handle_image(_, message: Message):
        user_id = message.from_user.id
        file_path = await app.download_media(message)
        logger.info(f'User({user_id}) -> Enviou a imagem: {file_path}')

        extracted_text = extract_text_from_image(file_path)
        json_data = get_estructured_json(user_id, extracted_text)
        os.remove(file_path)

        user_data[user_id] = json_data[8:-4].replace('\n    ','').replace('\n','')
        user_data[user_id] = json.loads(user_data[user_id])

        missing_fields = [k for k, v in user_data[user_id].items() if v == "null"]

        if missing_fields:
            await message.reply_text(
            f"Algumas informações estão faltando: {', '.join(missing_fields)}. Por favor, envie as informações faltantes no formato:\n\n`campo: valor`\n\nPor exemplo:\n`category: Alimentação`\n`date: 2023-10-05`"
        )
        else:
            await message.reply_text(
                f"Tudo certo com os dados extraídos. Deseja confirmar?\n\n{json_data}\n\nEnvie `/confirmar` para prosseguir ou envie alterações no formato:\n\n`campo: novo_valor`"
            )

        logger.info(f'Bot({user_id}): -> response')
