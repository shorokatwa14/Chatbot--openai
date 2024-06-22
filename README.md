# Dr. AI - Arabic Medical Chatbot with GPT-3.5 Turbo

Dr. AI is a Flask application that implements a chatbot powered by OpenAI's GPT-3.5 Turbo model. This chatbot assists users in Arabic with medical inquiries, providing tailored responses using advanced natural language processing capabilities. It stores conversation history in an SQLite database and ensures privacy by handling non-medical queries appropriately.

## Features

- **GPT-3.5 Turbo Model**: Uses OpenAI's powerful model for generating contextually relevant responses.
- **SQLite Database**: Stores chat history securely for future reference and analysis.
- **Medical Focus**: Responds specifically to medical questions in Arabic.
- **Privacy and Security**: Prioritizes patient confidentiality by not responding to non-medical queries.
- **Flask API**: Implements a RESTful API for seamless integration with client-side applications.
- **Cross-Origin Resource Sharing (CORS)**: Allows interaction with the API from different domains.

## Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shorokatwa14/Chatbot--openai.git
   cd your-repository
   ```
2.  Create a new virtual environment (replace `venv` with your preferred name):

   ```bash
   python -m venv venv
```
3. Activate the virtual environment

   On Windows

   ```bash
        venv\Scripts\activate
   ```

     On macOS and Linux

```bash
        source venv/bin/activate
```
4. Install Dependencies
   ```bash
    pip install -r requirements.txt

    ```
5. run app (open terminal)
      ```bash
         python app.py
   ```
