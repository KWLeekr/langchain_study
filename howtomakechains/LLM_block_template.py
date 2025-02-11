#-------------------------------------------

from langchain.chat_models import ChatOpenAI

#-------------------------------------------

# <무슨 봇 쓸지, MAX토큰 등 지정 코드>

# 여기서 설정할 수 있는 내용
# AI모델
# 맥스토큰
# 아웃풋 스키마
# Function_calling 등등...

chat = ChatOpenAI(
    model="gpt-4o-mini", 
    max_tokens=150
)

#-------------------------------------------

# <이 부분은, 그냥 parser임 (지 마음대로 만드는 것)>
# 이 부분은, 사용자가 커스텀 해서 만든 부분임

from langchain.schema import BaseOutputParser

class CommaOutputParser(BaseOutputParser):
    def parse(self, text):
        items = text.split(",")
        return list(map(str.strip,items))

from langchain.prompts import ChatPromptTemplate

#-------------------------------------------

# 이부분이 시스템 메시지, 사용자 메시지와 매개변수 집어넣는 부분
# 이 부분은, dify의 LLM 세팅하는 부분이라고 생각하자. -> 나중에 여기 .md파일을 연결할 수 있도록 하자.

template = ChatPromptTemplate.from_messages([
    ("system", "a list generating machine Everything you are asked will be answered with a comma separated list of max {max_items} in lowercase. Do not reply with anything else"),
    ("human", "{question}"),
])

#-------------------------------------------

# template을 chat에 넣고, 그 결과를 CommaOutputParser에 넣은 것
# 맨 마지막에 CommaOutputParser를 안 넣으면, 그냥 답변이 돌아옴 (이 위에 있는 요소들을 순차적으로 처리하기 위한 코드)

chain = template | chat | CommaOutputParser()

#-------------------------------------------
# 아래는, dify 시작 부분에서 Placeholder(매개변수)와 sys.query 등을 집어넣는 코드라고 생각하자. (일단은)

response = chain.invoke({
    "max_items":5,
    "question": "What are the pokemons?"
})

#-------------------------------------------


