from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task= "text-generation",
    
)
model = ChatHuggingFace(llm=llm)
class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City of the person")
parser= PydanticOutputParser(pydantic_object=Person)

template1= PromptTemplate(
    template=" Give me name, age, city of a fictional {place} person\n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}

)

# prompt = template1.format(topic='Black Holes')
# result= model.invoke(prompt)
# print(parser.parse(result.content))


# Using Chains

chains = template1 | model | parser
result = chains.invoke({"place":"Sri Lanka"})
print(result)
