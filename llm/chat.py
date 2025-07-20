# ============ Importação ============= #
import os
from core.config import GOOGLE_API_KEY
from core.history import get_session_history
from llm.prompt import prompt
from langchain_google_genai import ChatGoogleGenerativeAI  # trocar para uma llm local no futuro 
from langchain_core.runnables.history import RunnableWithMessageHistory


# ============== Código =============== #
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
)

runnable = prompt | llm

runnable_w_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history", 
)

def run_llm_with_history(user_id: int, user_input: str):
    response = runnable_w_history.invoke(
    {"input": user_input},
    config={"configurable": {"session_id": user_id}},
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
