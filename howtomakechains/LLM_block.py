#-------------------------------------------

from langchain.chat_models import ChatOpenAI

#-------------------------------------------

# 무슨 봇 쓸지 지정
chat = ChatOpenAI(
    model="gpt-4o-mini", 
    max_tokens=150
)

#-------------------------------------------
# 이 부분은, 그냥 parser임 (지 마음대로 만드는 것)

from langchain.schema import BaseOutputParser

class CommaOutputParser(BaseOutputParser):
    def parse(self, text):
        items = text.split(",")
        return list(map(str.strip,items))

from langchain.prompts import ChatPromptTemplate

#-------------------------------------------

# 이부분이 시스템 메시지, 사용자 메시지와 매개변수 집어넣는 부분
# 이 부분은, dify의 LLM 세팅하는 부분이라고 생각하자.

template = ChatPromptTemplate.from_messages([
    ("system", "a list generating machine Everything you are asked will be answered with a comma separated list of max {max_items} in lowercase. Do not reply with anything else"),
    ("human", "{question}"),
])

#-------------------------------------------

# template을 chat에 넣고, 그 결과를 CommaOutputParser에 넣은 것
# 맨 마지막에 CommaOutputParser를 안 넣으면, 그냥 답변이 돌아옴

chain = template | chat | CommaOutputParser()

#-------------------------------------------
# 아래는, dify 시작 부분에서 매개변수 Placeholder와 sys.query 집어넣는 코드라고 생각하자. (일단은)

chain.invoke({
    "max_items":5,
    "question": "What are the pokemons?"
})

#-------------------------------------------


