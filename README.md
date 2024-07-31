# FAQ Generator

## Description

The FAQ Generator is a web application that creates a list of frequently asked questions (FAQs) based on a given product description. Utilizing `dotenv`, `Streamlit`, and `langchain_groq`, this tool helps businesses and product owners generate comprehensive FAQs to better inform their potential customers.

## Features

- Upload a product description in `.txt` format
- View the uploaded description
- Generate a list of FAQs with answers
- Display the generated FAQs in a user-friendly format

## Requirements

- Python 3.x
- `dotenv`
- `Streamlit`
- `langchain_groq`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/faq-generator.git
    cd faq-generator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with the necessary environment variables:
    ```dotenv
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload a `.txt` file containing your product description.

4. Click the "Generate FAQs" button to get a list of frequently asked questions and answers.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Thanks

Thank you for checking out this project! If you have any questions or feedback, feel free to reach out.
