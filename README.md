# News Research Tool

This project uses **LangChain** and **Groq's LLM** to analyze and extract insights from news articles provided via URLs. Users can ask questions, and the tool will retrieve answers along with the source information.

## Features
- Extracts content from up to three news article URLs.
- Splits and processes the content for efficient retrieval.
- Allows users to ask questions about the articles.
- Provides answers along with the source links.
- Utilizes **FAISS** for fast similarity search and **Groq's LLM** for question answering.

## Technologies Used
- **Python**: Main programming language.
- **LangChain**: For building language model chains.
- **Groq**: To access and interact with the LLM model.
- **Streamlit**: For building an interactive web interface.
- **FAISS**: For efficient similarity search.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VIJAYABASKARVB/news-research-tool.git
   cd news-research-tool
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your Groq API Key: Ensure you have a `.env` file with the following content:
   ```bash
   GROQ_API_KEY="your_groq_api_key_here"
   ```

## Usage

Run the Streamlit application:
```bash
streamlit run main.py
```

## Example Output

```bash
Loaded data from URLs.
Splitting text into chunks...
Generating embeddings...

Question: What is the main topic of the articles?

Answer:
The main topic is about the latest developments in AI technology.

Sources:
1. https://example.com/article1
2. https://example.com/article2
```

## Customization

1. **Number of URLs**: Adjust the `for` loop to accept more or fewer URLs.

2. **Model Settings**: Modify the `temperature` parameter of the `ChatGroq` instance to control the creativity of responses.

## Requirements

Ensure you have the following Python packages installed:

- `streamlit`
- `langchain`
- `langchain-groq`
- `sentence-transformers`
- `faiss-cpu`
- `unstructured`
- `python-dotenv`

## You can install these via:
```bash
pip install -r requirements.txt
```

## Contributions

Feel free to open a pull request or submit issues if you'd like to contribute!
