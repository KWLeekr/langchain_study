from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.callbacks import StreamingStdOutCallbackHandler

# -----------------------------------------------------------------------
# 간단한 해설 (완전 정확하지는 않음)

# Langchain은 chain이라는 것을 만들어서, LLM의 워크플로우를 구성한다.
# 그러기 위해서 해야할 일은 다음과 같다.

# 1. LLM 설정 -> LLM 요소를 만들고, 그안에 어떤 모델을 쓸지, 그 모델의 temperature, 등 옵션을 설정한다.
# 2. Memory 설정 -> 어떤 방식의 기억(메모리)을 사용할지 설정한다. (LLM으로 요약된 메모리 or 대화내용 그대로 넣기) (저장하는 범위, 용량)
# 3. Template 설정 -> 현재의 상황을 어떻게 보여줄지 설정 (System prompt, memory, 현재 입력한 내용 등을 어떤 형태로 보여줄지 설정 가능) 
# 4. 지금까지 만든 LLM, Memory, Template의 설정값이 들어있는 변수들을 넣어서 "Chain"을 만든다. -> 이렇게 LLM사용을 위한 설정이 끝남.

# chain을 통해 지금까지 설정한 Memory, Template을 LLM에게 전달 할 수 있음 -> LLM을 원하는대로 사용할 수 있음
# **완성** : 이 Chain을 실행하면, LLM과 대화할 수 있는 구조이다.


# 좋은 점은, 같은 Memory를 여러 Chain이 공유할 수도 있고, Template도 공유할 수 있음. (이걸 조합해서 여러가지 시스템에 응용할 수 있음)

# -----------------------------------------------------------------------

# LLM 선언(어떤 LLM모델 쓸지 등)
LLM = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.1, 
    streaming=True, 
    callbacks=[StreamingStdOutCallbackHandler()],
    max_tokens=150
)
# -----------------------------------------------------------------------

# 이 부분의 코드는, 채팅의 메모리(기억) 설정 (ConversationBufferWindowMemory임)
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    return_messages=True,
    k=20,
    memory_key="chat_history"
)

# -----------------------------------------------------------------------

# chat template 만들기 (아직까지 manual 기억은 추가되지 않음) -> 다음에 추가할 파일에서 만들 것임
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a geography expert, And you only reply in Korean"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{question}"),
])

# -----------------------------------------------------------------------

# LLMChain 만들기 -> Chain에서 구동할 프롬프트, 메모리, LLM 설정 (이걸 뭐라고 표현하는지 모르겠음)
from langchain.chains import LLMChain

chain = LLMChain(
    llm=LLM,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# -----------------------------------------------------------------------

# LLM에게 "Hello, My name is gyungwook" 이라고 보내는 것
# 실제 의미는 Template의 {question}에 들어갈 부분을 넣어서 LLM을 구동한다는 뜻에 더 가깝다.

chain.predict(question="Hello, My name is gyungwook")


