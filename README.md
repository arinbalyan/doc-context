# BajajRx v2

BajajRx v2 (Bolt) is an intelligent document query-retrieval system designed to provide quick and accurate answers to questions based on provided documents. It leverages vector databases for efficient similarity search and large language models for generating coherent responses.

## Features

*   **Document Processing:** Ingests documents (currently supports PDF via URL) and processes them into searchable chunks.
*   **Semantic Search:** Uses sentence embeddings to perform semantic searches on document chunks, retrieving the most relevant information.
*   **AI-Powered Question Answering:** Utilizes a Large Language Model (LLM) to generate answers based on the retrieved context from documents.
*   **Scalable Backend:** Built with FastAPI for a robust and performant API.
*   **Vector Database Integration:** Integrates with Qdrant for efficient vector storage and retrieval.
*   **Authentication:** Secure API access using bearer tokens.

## Technologies Used

*   **Backend:**
    *   Python 3.10+
    *   FastAPI
    *   Qdrant (Vector Database)
    *   Sentence Transformers (for embeddings)
    *   OpenAI / OpenRouter (for LLM integration)
    *   Supabase (for potential future database needs, currently used for authentication)
    *   Pydantic (for data validation)
*   **Frontend:**
    *   HTML (basic `index.html` for demonstration)

## Prerequisites

Before you begin, ensure you have the following installed:

*   [Python 3.10+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
*   [Git](https://git-scm.com/downloads)

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/bajajrx-v2-bolt.git
    cd bajajrx-v2-bolt
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install backend dependencies:**

    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the `backend/` directory with the following content. Replace the placeholder values with your actual API keys and URLs.

    ```
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_anon_key
    QDRANT_URL=your_qdrant_cloud_url
    QDRANT_API_KEY=your_qdrant_api_key
    OPENROUTER_API_KEY=your_openrouter_api_key
    API_BEARER_TOKEN=your_secret_api_bearer_token
    QDRANT_COLLECTION_NAME=hackrx_documents
    ```
    *   `SUPABASE_URL` and `SUPABASE_KEY`: Obtain these from your Supabase project settings.
    *   `QDRANT_URL` and `QDRANT_API_KEY`: Obtain these from your Qdrant Cloud dashboard.
    *   `OPENROUTER_API_KEY`: Obtain this from your OpenRouter.ai account.
    *   `API_BEARER_TOKEN`: A secret token of your choice for authenticating API requests.

## Running the Application

1.  **Start the Backend Server:**

    Navigate to the `backend/` directory and run the FastAPI application using Uvicorn:

    ```bash
    cd backend
    uvicorn app.main:app --reload
    ```
    The API will be accessible at `http://127.0.0.1:8000`. The `--reload` flag enables auto-reloading on code changes.

2.  **Accessing the Frontend (Basic):**

    The `frontend/index.html` file provides a very basic interface. You can open this file directly in your web browser to see a placeholder. For a full-fledged frontend, you would typically serve it using a web server or a framework like React/Vue/Angular.

## API Usage

The primary API endpoint is `/api/v1/hackrx/run`.

*   **Endpoint:** `POST /api/v1/hackrx/run`
*   **Content-Type:** `application/json`
*   **Accept:** `application/json`
*   **Authentication:** `Authorization: Bearer <your_secret_api_bearer_token>` (replace `<your_secret_api_bearer_token>` with the value from your `.env` file).

### Request Body Example:

```json
{
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": [
        "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
        "What is the waiting period for pre-existing diseases (PED) to be covered?",
        "Does this policy cover maternity expenses, and what are the conditions?"
    ]
}
```

*   `documents`: A URL to the document (e.g., PDF) to be processed.
*   `questions`: A list of questions to be answered based on the document.

### Response Body Example:

```json
{
    "answers": [
        "The grace period for premium payment under the National Parivar Mediclaim Plus Policy is 30 days for yearly premium payment mode and 15 days for half-yearly/quarterly/monthly premium payment mode.",
        "The waiting period for pre-existing diseases (PED) to be covered is 48 months from the date of inception of the first policy.",
        "Yes, this policy covers maternity expenses after a waiting period of 24 months from the date of inception of the first policy. It covers delivery expenses (including caesarean section) and lawful medical termination of pregnancy."
    ]
}
```

*   `answers`: A list of answers corresponding to the questions asked.

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/             # API endpoints
│   │   ├── core/            # Configuration and security
│   │   ├── db/              # Database clients (Qdrant, Supabase)
│   │   ├── models/          # Pydantic schemas
│   │   └── services/        # Business logic (document processing, query answering)
│   ├── .env                 # Environment variables (local)
│   ├── .env.example         # Example environment variables
│   └── requirements.txt     # Python dependencies
├── documents/               # Placeholder for documents (e.g., .gitkeep)
├── frontend/
│   └── index.html           # Basic frontend HTML
├── venv/                    # Python virtual environment
└── README.md                # Project README
```
