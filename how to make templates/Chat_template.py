from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a geography expert, And you only reply in {language}"),
    ("ai", "Ciao mi chamo {name}!"),
    ("human","What is the distance between {country_A} and {country_B} and what is your name?"),
])

prompt = template.format_messages(language = "Greek", name = "Gyungwook",country_A="mexico", country_B = "Thailand")

chat.predict_messages(prompt)
