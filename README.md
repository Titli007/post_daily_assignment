# News App with Precautionary Guide

## Overview
This application fetches news articles based on user queries and provides a summary along with precautionary steps. It uses Flask for the backend and Streamlit for the frontend.

## Features
- Fetch news articles based on user-defined queries.
- Summarize articles in an easy-to-read format.
- Provide precautionary steps related to the news content.
- Send the summary via email to the user.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables. Create a `.env` file in the backend directory with the following variables:
   ```plaintext
   MAIL_USERNAME=your_email@gmail.com
   APP_PASSWORD=your_app_password
   GEMINI_API_KEY=your_api_key
   ```

5. Run the Flask application:
   ```bash
   flask run
   ```

## Usage

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Enter your query and an optional email address to receive the news summary.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements.

## Contact
For any inquiries, please contact [your_email@example.com].