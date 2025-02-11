from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "What is distance between {country_A} and {country_B}?"
)

template.format(country_A = "italy", country_B = "Mexico")
