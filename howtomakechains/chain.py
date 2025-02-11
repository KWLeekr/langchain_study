from langchain.chat_models import ChatOpenAI

# chat 객체 만들기
chat = ChatOpenAI(
    model="gpt-4o-mini", 
    max_tokens=150
)

from langchain.schema import BaseOutputParser

class CommaOutputParser(BaseOutputParser):
# split 하면, 입력한 문자를 기준으로, 문장을 나눠서, 그것을 배열에 넣어준다.
    def parse(self, text):
        items = text.split(",")
        return list(map(str.strip,items))

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

# output : ['pikachu', 'bulbasaur', 'charmander', 'squirtle', 'jigglypuff']
