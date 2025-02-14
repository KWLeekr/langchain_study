# 기억을 저장하는 코드만 있고, 기억을 불러오는 코드가 없지만, 일단 백업해둠

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.1, 
    streaming=True, 
    callbacks=[StreamingStdOutCallbackHandler()],
    max_tokens=150
)

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

chain = template | chat

#-------------------------------------------
# 이 부분의 코드는, 메모리를 정의함 (ConversationBufferWindowMemory임)

from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    return_messages=True,
    k=4
)

def add_message(input, output):
    memory.save_context({"input":input},{"output":output})
# 아래는, dify 시작 부분에서 Placeholder(매개변수)와 sys.query 등을 집어넣는 코드라고 생각하자. (일단은)

# 질문
question = "what are the pokemons?"

response = chain.invoke({
    "max_items":5,
    "question": question
})

# 여기서 리턴을 하든, 그 값을 다른데다가 돌려쓰든 마음대로 하면 된다.
#-------------------------------------------
# 기억 저장하는 부분
add_message(question, response)

#-------------------------------------------
# 출력
response
