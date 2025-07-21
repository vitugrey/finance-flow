from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt_generic = ChatPromptTemplate.from_messages(
    [
        # antes do deply mudar o system prompt para algo mais especifico
        ("system","Você é um chatbot de conversação que ajuda a gerenciar as finanças pessoais."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)


prompt_extract = ChatPromptTemplate.from_messages(
    [
        # antes do deply mudar as categorias e fazer uma manipulação de dados para padronizar as categorias.
        ("system","Você é um chatbot de conversação que ajuda a gerenciar as finanças pessoais."),
        MessagesPlaceholder(variable_name="history"),
        ("human", """Extraia o seguinte dados:
         'description' no formato de string;
         'value' no formato de float;
         'category' no formato de string com umas das opções: "	Alimentação", "	Transporte", "Lazer", "Moradia", "Educação", "Investimento", "Renda Extra", "Salário", "Outros", "Skin";
         'date' no formato de datetime no padrão ISO 8601 (YYYY-MM-DD);
         'transaction_type' no formato de string com uma das opções: "Expense", "Income";
         'is_credit' no formato booleano, onde True indica que é uma despesa de cartão de crédito e False indica que é uma despesa gasta diretamente da conta bancária;
         'is_fixed_expense' no formato booleano, onde True indica que é uma despesa fixa e False indica que é uma despesa variável;
         'created_at' no formato de datetime no padrão ISO 8601 (YYYY-MM-DDTHH:MM:SSZ);e
         'updated_at' no formato de datetime no padrão ISO 8601 (YYYY-MM-DDTHH:MM:SSZ).
        
         Texto extraido: 
         {extracted_text}"""),
    ]
)

prompt_output_parsers = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um chatbot de conversação que ajuda a gerenciar as finanças pessoais."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{extracted_text}"),
    ]
)
