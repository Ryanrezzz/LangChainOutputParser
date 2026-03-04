# LangChain Output Parsers

This module demonstrates various **Output Parsers** in LangChain, which are used to structure and format the raw text output from LLMs into more usable formats.

All examples use **Meta Llama 3.3 70B Instruct** via HuggingFace.

---

## 📂 Files

### 1. `str_out_pars.py` — String Output (Basic)
A basic example of invoking an LLM **without** an explicit output parser. The raw `AIMessage` content is printed directly.

- Uses two chained prompts: first explains a topic, then summarizes the result in 5 lines.
- Demonstrates manual prompt chaining by passing one result into the next.

### 2. `str_out_pars2.py` — String Output Parser (with Chains)
Uses `StrOutputParser` to extract the string content from the model response, enabling **seamless prompt chaining**.

- Builds a single chain: `PromptTemplate → Model → StrOutputParser → PromptTemplate → Model → StrOutputParser`
- Shows how `StrOutputParser` makes it possible to pipe model output directly into the next prompt template.

### 3. `json_out_pars.py` — JSON Output Parser
Uses `JsonOutputParser` to instruct the LLM to return structured **JSON** output.

- Injects format instructions into the prompt via `partial_variables`.
- Demonstrates both manual invocation (commented out) and **LCEL chains**.
- ⚠️ Notes that `JsonOutputParser` may not always produce well-structured output for complex requests.

### 4. `pydantic_out_pars.py` — Pydantic Output Parser
Uses `PydanticOutputParser` with a **Pydantic model** (`Person`) to enforce a strict schema on the LLM output.

- Defines a `Person` schema with `name`, `age` (must be > 18), and `city` fields.
- The parser auto-generates format instructions from the Pydantic model.
- Returns a validated Pydantic object instead of a raw dict.

### 5. `structured_out_pars.py` — Structured Output Parser
Uses `StructuredOutputParser` with `ResponseSchema` definitions to get structured key-value output.

- Defines 5 response schemas (fact1–fact5), each expecting a fact about a given topic.
- Uses `langchain_classic` for the `StructuredOutputParser` import.
- Demonstrates chain-based invocation with topic **"Black hole"**.

---

## 🧠 Key Concepts

| Parser | Output Type | Use Case |
|---|---|---|
| `StrOutputParser` | `str` | Simple text extraction for chaining |
| `JsonOutputParser` | `dict` | Flexible JSON output |
| `PydanticOutputParser` | Pydantic `BaseModel` | Schema-validated structured output |
| `StructuredOutputParser` | `dict` | Key-value structured output via response schemas |

---

## ⚙️ Setup

1. Create a `.env` file with your HuggingFace API token:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```
2. Install dependencies:
   ```bash
   pip install langchain-huggingface langchain-core langchain-classic pydantic python-dotenv
   ```
3. Run any file:
   ```bash
   python str_out_pars.py
   ```
