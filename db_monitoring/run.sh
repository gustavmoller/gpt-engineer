# Install dependencies and set up the environment for local development
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate mock data
python mock_data/generate_mock_data.py


# Run the Streamlit application
streamlit run streamlit_app.py &
