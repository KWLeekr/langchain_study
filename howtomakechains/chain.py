from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "a list generating machine Everything you are asked will be answered with a comma separated list of max {max_items} in lowercase. Do not reply with anything else"),
    ("human", "{question}"),
])

chain = template | chat | CommaOutputParser()

chain.invoke({
    "max_items":5,
    "question": "What are the pokemons?"
})
