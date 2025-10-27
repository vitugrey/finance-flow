from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_PROMPT = """Você é um chatbot de conversação que ajuda a gerenciar as finanças pessoais. Eu sou o Vitor Mattos de Siqueira Grey"""

prompt_generic = ChatPromptTemplate.from_messages(
    [
        # antes do deply mudar o system prompt para algo mais especifico
        ("system",SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)


prompt_extract = ChatPromptTemplate.from_messages(
    [
        # antes do deply mudar as categorias e fazer uma manipulação de dados para padronizar as categorias.
        ("system",SYSTEM_PROMPT),
        ("human", """Você é um extrator de texto no formato JSON que retornar apenas as informações da transação caso não tenha tal infomação retorne 'null' no lugar da informação. Retorne o seguinte json:
         
            'description': descição da transação no formato de string;
            'value': valor da transação no formato de float;
            'category': categoria da transação no formato de string com umas destas opções: "Alimentação", "Transporte", "Lazer","Moradia", "Educação", "Investimento", "Renda Extra", "Salário", "Outros", "Skin";
            'date': data da transação no formato de string no padrão ISO 8601 (YYYY-MM-DD);
            'transaction_type': tipo da transação no formato de string com uma destas opções: "Expense", "Income";
            'is_credit': metodo de pagamento no formato booleano, onde True indica que é uma despesa de cartão de crédito e False indica que é uma despesa gasta diretamente da conta bancária;
            'is_fixed_expense': se a transação é uma despesa fixa no formato booleano, onde True indica que é uma despesa fixa e False indica que é uma despesa não recorrente;
            'created_at': data de criação da transação no formato de string no padrão TIMESTAMP (AAAA-MM-DD HH:MM:SS.SSS);
            'updated_at': data de atualização da transação no formato de string no padrão TIMESTAMP (AAAA-MM-DD HH:MM:SS.SSS);
         
         Texto extraido: 
         {extracted_text}
         
         JSON: """),
    ]
)
