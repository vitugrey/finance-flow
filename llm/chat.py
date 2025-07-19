# ============ Importação ============= #
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI  # trocar para uma llm local no futuro
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ============== Código =============== #


# class AgentTranscription:
#     def __init__(self):
#         self.llm = ChatGoogleGenerativeAI(  # trocar para uma llm local no futuro
#             model="gemini-2.0-flash",
#             google_api_key="",  # colocar em um arquivo .env,
#             temperature=0,
#         )
#         self.response_schemas = [
#             ResponseSchema(name="description", description="Descrição da transação, como nome do estabelecimento"),
#             ResponseSchema(name="value", description="Valor da transação com símbolo (ex: 27,90)"),
#             ResponseSchema(name="category_id", description="Categoria como Alimentação, Transporte, etc."),
#             ResponseSchema(name="date", description="Data da transação no formato DD/MM/AAAA"),
#             ResponseSchema(name="is_credit", description="Se é crédito (true) ou débito (false)"),
#             ResponseSchema(name="is_fixed_expense", description="Se é uma despesa fixa (true) ou variável (false)"),
#             ResponseSchema(name="transaction_type", description="Tipo de transação: 'Income' ou 'Expense'"),
#             ResponseSchema(name="created_at", description="Data de criação no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)"),
#             ResponseSchema(name="updated_at", description="Data de atualização no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)"),
#         ]
#         self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schemas)
#         self.format_instructions = self.output_parser.get_format_instructions()

#         self.prompt = ChatPromptTemplate.from_template("""
#             Você é um assistente que extrai dados estruturados de um OCR de recibo.

#             Extraia as seguintes informações:

#             {format_instructions}

#             Texto OCR:
#             \"\"\"{ocr_text}\"\"\"
#             """)
        
#     def process_image_structured(self, img_path: str) -> dict:
#         """
#         Processa uma imagem e extrai informações estruturadas usando OCR e LLM.

#         Args:
#             img_path (str): Caminho da imagem a ser processada.

#         Returns:
#             dict: Dicionário com as informações extraídas.
#         """
#         ocr_text = pytesseract.image_to_string(Image.open(img_path), lang='por')
#         if not ocr_text.strip():
#             return {"erro": "Nenhum texto encontrado na imagem."}

#         chain = self.prompt | self.llm | self.output_parser
#         result = chain.invoke({
#             "ocr_text": ocr_text,
#             "format_instructions": self.format_instructions,
#         })

#         return result
