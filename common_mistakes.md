# Common Mistakes Developers Make When Using LangChain

## 1. Treating LangChain as Just an LLM Wrapper

Many beginners think LangChain is only for calling LLMs.  
But in reality, it is a full framework for building:

-   Pipelines
-   Agents
-   Retrieval-Augmented Generation (RAG) systems
-   Complex workflows

If you only use it to call the LLM, you’re missing most of its power.

---

## 2. Not Using LCEL (LangChain Expression Language)

LCEL makes it easy to chain steps like

-   prompts
-   models
-   parsers
-   and tools

using simple operators.  
Many people still use older procedural patterns, which result in longer, harder-to-maintain code.

Use LCEL to keep your pipelines **clean, fast, and easy to debug**.

---

## 3. Forgetting to Use Output Parsers

LLMs produce unstructured text.  
Without output parsers, you may get:

-   messy outputs
-   inconsistent answers
-   errors in downstream steps

Use parsers such as:

-   **PydanticOutputParser**
-   **StructuredOutputParser**
-   **CommaSeparatedListOutputParser**

These help enforce structure like **JSON, lists, and tables**.

---

## 4. Ignoring Memory or Using It Incorrectly

Memory is optional but powerful. Common mistakes include:

-   Not using memory when needed
-   Storing too much history
-   Keeping unnecessary details

Choose the memory type that fits your use case, such as:

-   Chat history memory
-   Entity memory
-   Custom memory classes

Avoid saving full transcripts unless required.

---

## 5. Only Using Local Documents for RAG

Testing RAG with local PDFs is fine, but real-world RAG needs:

-   High-quality embeddings
-   A strong vector store
-   A smart retrieval strategy, such as:
    -   **MultiQueryRetriever**
        -   User query → LLM expands into multiple queries → each query retrieves docs → results are combined.
    -   **ContextualCompressionRetriever**
        -   Retriever finds documents → compressor (LLM) extracts the parts relevant to the query → irrelevant text is removed.
    -   **RAG-Fusion**
        -   Generate multiple versions of the query
        -   Retrieve documents for each version
        -   Merge the results
        -   Rank them using scoring (e.g., similarity, frequency)
        -   Return the top documents

Without these, your results will often be **weak or irrelevant**.

---
