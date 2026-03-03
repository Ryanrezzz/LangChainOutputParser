from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task= "text-generation",
    
)
model = ChatHuggingFace(llm=llm)
schema= [
    ResponseSchema(name='fact1',description='fact about the topic'),
    ResponseSchema(name='fact2',description='fact about the topic'),
    ResponseSchema(name='fact3',description='fact about the topic'),
    ResponseSchema(name='fact4',description='fact about the topic'),
    ResponseSchema(name='fact5',description='fact about the topic'),
]
parser= StructuredOutputParser.from_response_schemas(schema)
template1= PromptTemplate(
    template=" Give me 5 facts about the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}

)

# prompt = template1.format(topic='Black Holes')
# result= model.invoke(prompt)
# print(parser.parse(result.content))


# Using Chains

chains = template1 | model | parser
result = chains.invoke({'topic':"Black hole"})
print(result)
