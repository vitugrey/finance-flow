# ============ Importação ============= #
import os
from core.config import GOOGLE_API_KEY
from core.history import get_session_history
from langchain_google_genai import ChatGoogleGenerativeAI  # trocar para uma llm local no futuro 
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import PydanticOutputParser
from llm.prompt import prompt_generic, prompt_extract
from api.schemas.transaction import TransactionBase


# ============== llm =============== #
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
)

parser = PydanticOutputParser(
    pydantic_object=TransactionBase,)

# ============== runnubles =============== #
runnable_generic = prompt_generic | llm
runnable_extract = prompt_extract | llm

runnable_generic_w_history = RunnableWithMessageHistory(
    runnable_generic,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history", 
)

runnable_extract_w_history = RunnableWithMessageHistory(
    runnable_extract,
    get_session_history,
    input_messages_key="extracted_text",
    history_messages_key="history",
)


# ============== funções=============== #
def get_response_with_history(user_id: int, user_input: str):
    response = runnable_generic_w_history.invoke(
    {"input": user_input},
    config={"configurable": {"session_id": user_id}},
)
    return response.content

def get_estructured_json(user_id: int, user_input: str):
    response = runnable_extract.invoke(
        {"extracted_text": user_input},
    )
    return response.content


# def load_history_as_langchain_messages(user_id: int):
#     history = get_user_history(user_id)
#     history = history[-15:]
#     messages = []
#     for item in history:
#         if item["role"] == "user":
#             messages.append(HumanMessage(content=item["message"]))
#         elif item["role"] == "ia":
#             messages.append(AIMessage(content=item["message"]))
#     return messages

# def get_llm_response(user_id: int, user_input: str) -> str:
#     messages = load_history_as_langchain_messages(user_id)
#     messages.append(HumanMessage(content=user_input))
#     response = llm.invoke(messages)
#     return response.content
