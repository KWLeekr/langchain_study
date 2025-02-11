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

chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class chef. you create easy-to-follow recipes for any type of cuisine with easy to find ingredients"),
    ("human", "I want to cook {cuisine} food.")
])

chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a vegetarian chef specialized on making traditional recipes vegetarian. You find alternative ingredients and explain their preparation. You don't radically modify the recipe. If there is no alternative for a food just say you don't know how to recipe it."),
    ("human", "{recipe}")
])

veg_chef_chain = veg_chef_prompt | chat

final_chain = {"recipe":chef_chain} | veg_chef_chain # 중요, recipe 안에 chef_chain의 실행결과를 넣는 코드 예제임

final_chain.invoke({"cuisine" : "indian"})
