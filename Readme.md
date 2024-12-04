
# College FAQ Chatbot

This project implements a **FAQ Chatbot** for answering common queries related to college information using **Hugging Face Transformers** and a **pre-trained language model**. The chatbot uses **Natural Language Processing (NLP)** to answer questions based on a given context, which could be about courses, admission process, campus facilities, etc.

## Features

- **Question-Answering**: Answer questions related to the college.
- **Pre-trained Model**: Uses a pre-trained language model from Hugging Face (e.g., DistilBERT) for efficient and accurate question answering.
- **Streamlit Interface**: Simple user interface to interact with the chatbot.

## Tech Stack

- **Programming Language**: Python
- **Libraries**:
  - `transformers`: For loading pre-trained NLP models.
  - `torch`: Required for PyTorch models.
  - `streamlit`: For building the user interface.
- **Model**: DistilBERT-based model fine-tuned for question answering.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/college-faq-chatbot.git
cd college-faq-chatbot
```

### 2. Install the required libraries:
You can install the required dependencies using pip:
```bash
pip install transformers torch streamlit
```

## How to Run the Chatbot

### 1. Save your `app.py` script (or whatever script you're using) in the project directory.
### 2. Run the Streamlit app:

In the terminal, navigate to your project directory and use the following command:
```bash
streamlit run app.py
```

This will open the chatbot interface in your default browser.

## Usage

Once the chatbot interface opens in the browser, you can type in any questions related to the college. For example:
- "What courses are offered?"
- "What is the admission process?"
- "Where is the college located?"

The chatbot will respond with relevant answers based on the given context.

### Example:
1. **Context**: "We offer B.Tech programs in Information Technology, Computer Science, Electronics."
2. **Question**: "What courses are offered?"
3. **Response**: "Information Technology, Computer Science, Electronics."

## Project Structure

```
college-faq-chatbot/
│
├── app.py                # Main file to run the Streamlit app
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Notes

- This project uses a pre-trained **DistilBERT** model fine-tuned on SQuAD (Stanford Question Answering Dataset).
- You can modify the `context` to add more college-related information (e.g., admission procedures, fee structure, campus facilities, etc.).
  
## Future Improvements

- **Support for multiple languages**: Add multi-language support for non-English queries.
- **Enhanced Data**: Use more extensive data (e.g., college brochures, websites) for better responses.
- **User Interface**: Improve the UI to make it more interactive and visually appealing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

