from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        # antes do deply mudar o system prompt para algo mais especifico
        ("system","Você é um chatbot de conversação que ajuda a gerenciar as finanças pessoais."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
