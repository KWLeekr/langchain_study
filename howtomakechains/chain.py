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
# 이 부분은, 그냥 parser임

from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "a list generating machine Everything you are asked will be answered with a comma separated list of max {max_items} in lowercase. Do not reply with anything else"),
    ("human", "{question}"),
]) # 이 부분은, dify의 LLM 세팅하는 부분이라고 생각하자.

chain = template | chat | CommaOutputParser() # template을 chat에 넣고, 그 결과를 CommaOutputParser에 넣은 것

chain.invoke({
    "max_items":5,
    "question": "What are the pokemons?"
}) #이건, dify 시작 부분에서 매개변수 Placeholder 집어넣는 코드라고 생각하자. (일단은)


# output : ['pikachu', 'bulbasaur', 'charmander', 'squirtle', 'jigglypuff']

# 중요한 부분, 이 문법으로, chain = chain1 | chain2 | chain3 이런식으로 쓰면, chain1의 결과를 2로, 2의 결과를 3로 보낼 수 있음
