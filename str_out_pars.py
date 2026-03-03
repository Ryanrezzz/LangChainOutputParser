from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from  langchain_core.prompts import PromptTemplate
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
prompt= template1.invoke({'topic':'Black Holes'})
result= model.invoke(prompt)

template2=PromptTemplate(
    template="Summarize the given {text} in 5 lines",
    input_variables=['text']
)

prompt2=template2.invoke({'text':result.content})
result2=model.invoke(prompt2)

print(result2.content)



