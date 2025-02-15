# Learning Streamlit for Chatbot / Data Science

- https://streamlit.io
- https://docs.streamlit.io
- https://pypi.org/project/streamlit
- https://github.com/streamlit/streamlit

## Setup

```shell
python -m venv .venv
.\.venv\Scripts\activate

python -m pip install -U pip

python -m pip install -U streamlit

python -m pip install -U pandas
python -m pip install -U requests
python -m pip install -U yfinance

# Now! we write / modify / run Source Code(s)

deactivate
```

## For Publishing!

- Self Host / VPS Server
- https://streamlit.io
    - https://streamlit.io/cloud
- Microsoft Azure (Web App)
- https://huggingface.co/new-space

## For Testing Streamlit

```shell
streamlit hello
```

## For Running Project

```shell
streamlit run ./streamlit_app.py
```

```shell
python -m streamlit run ./app.py --server.address 0.0.0.0 --server.port 8000

```