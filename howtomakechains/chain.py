chain = template | chat | CommaOutputParser()

chain.invoke({
    "max_items":5,
    "question": "What are the pokemons?"
})
