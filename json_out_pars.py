from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from  langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task= "text-generation",
    
)
model = ChatHuggingFace(llm=llm)

parser= JsonOutputParser()

template1= PromptTemplate(
    template=" Give me name ,age, city of a fictional character \n{format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
# prompt=template1.format()
# result=model.invoke(prompt)
# print(parser.parse(result.content))

# using CHAINS

chains = template1 | model | parser
result= chains.invoke({})
print(result)


# Problem with JSON output parser is: dosent structure it well
template2= PromptTemplate(
    template=" write 5 facts about this {topic} \n{format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain2= template2 | model | parser
result2= chain2.invoke({'topic':'LLM'})
print(result2)
