# ============ Importação ============= #
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


# ============== Código =============== #
def get_session_history(user_id: int) -> BaseChatMessageHistory:
    return SQLChatMessageHistory(user_id, "sqlite:///storage/history/memory.db")


# import json
# import os
# from core.config import HISTORY_DIR

# def get_user_history(user_id: int) -> list:
#     os.makedirs(HISTORY_DIR, exist_ok=True)
#     history_file = os.path.join(HISTORY_DIR, f"{user_id}_history.json")
#     if os.path.exists(history_file):
#         try:
#             with open(history_file, 'r',encoding='utf-8') as f:
#                 return json.load(f)
#         except json.JSONDecodeError:
#             return []
#     return []


# def save_user_message(user_id: int, role: str, message: str):
#     history = get_user_history(user_id)
#     history.append({"role": role, "message": message})
#     history_file = os.path.join(HISTORY_DIR, f"{user_id}_history.json")
#     with open(history_file, "w", encoding="utf-8") as f:
#         json.dump(history, f, indent=2, ensure_ascii=False)
