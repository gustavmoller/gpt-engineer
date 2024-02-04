# Install dependencies and set up the environment for local development
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate mock data if in local development mode
if [ "$1" == "local" ]; then
    python mock_data/generate_mock_data.py
fi

# Run the Streamlit application
streamlit run streamlit_app.py &
