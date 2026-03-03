from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from  langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task= "text-generation",
    
)

model=ChatHuggingFace(llm=llm)

template1= PromptTemplate(
    template="Explain about this {topic}",
    input_variables=['topic']
)


template2=PromptTemplate(
    template="Summarize the given {text} in 5 lines",
    input_variables=['text']
)
parser= StrOutputParser()

chain= template1 | model |parser | template2 | model | parser

result= chain.invoke({'topic':'Black Holes'})
print(result)




