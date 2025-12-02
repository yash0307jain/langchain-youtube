# **LangChain Playlist**

Welcome to the **LangChain Playlist** repository!  
This playlist is designed to help you understand LangChain from the ground up — starting with basic concepts like prompts and output parsers, all the way to advanced topics like tools, memory, and Retrieval‑Augmented Generation (RAG).

Each video walks you through real, practical examples so you can build production‑ready AI applications.

---

## 🐍 **Install Python Using Miniconda / Miniforge**

To keep your AI projects clean and organized, it is recommended to use **conda environments**. Follow the steps below to install Miniforge and set up your environment.

---

### 🔗 **Download Miniforge for macOS (ARM64)**

Download from the official repository:  
https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh

---

### 💻 **Install Miniforge**

Run the following commands:

```bash
chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
source ~/miniforge3/bin/activate
```

---

### 🧱 **Create a project-specific conda environment**

```bash
conda create --prefix ./env python=3.13
conda activate ./env
```

---

### 📦 **Install packages from requirements.txt**

```bash
pip install -r requirements.txt
```

Your LangChain environment is ready to build powerful AI apps 🚀

---

# **📺 Playlist Breakdown**

### **1. Calling LLMs with APIs vs Using LangChain**

-   Understanding raw API usage vs LangChain abstractions.

### **2. Prompts in LangChain**

-   Creating dynamic prompts using `PromptTemplate`.

### **3. Output Parsers in LangChain**

-   Structuring and validating LLM outputs.

### **4. Runnables in LangChain**

-   Core building blocks to create modular AI pipelines.

### **5. Basic Chatbot using LangChain**

-   Building your first chatbot using chains.

### **6. Memory in LangChain**

-   Adding conversation memory to enhance user interactions.

### **7. Tools in LangChain**

-   Using tools and agents to extend LLM capabilities.

### **8. AI‑Powered Resume Analyzer & Job Matcher**

-   A practical project using prompts, models, and logic.

### **9. Retrieval‑Augmented Generation (RAG) Code Walkthrough**

-   Implementing RAG with vector stores, retrievers, and text splitters.

---

# **📄 requirements.txt**

```
langchain
langchain-openai
langchain-text-splitters
langchain-chroma
python-dotenv
notebook
```

---

# **🤝 Contributing**

Got suggestions or improvements?  
Feel free to open an issue or submit a pull request.

---

# **📜 License**

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

# **📬 Stay Connected**

-   [YouTube Channel](https://www.youtube.com/@yash0307jain)
-   [LinkedIn](https://www.linkedin.com/in/yash0307jain)

---

Thank you for checking out the **LangChain Playlist**!  
Happy building with AI 🚀
