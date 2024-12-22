# **************************************************
# pip install -U streamlit
# python -m pip install -U streamlit
# **************************************************
# import streamlit

# print("Streamlit Version:", streamlit.__version__)
# **************************************************

# **************************************************
# import os
# import streamlit

# os.system(command="cls")

# print("Streamlit Version:", streamlit.__version__)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# print("Streamlit Version:", st.__version__)
# **************************************************

# **************************************************
# Notes:
# 1) app.py                    --> streamlit_app.py
# 2) python ./streamlit_app.py --> streamlit run ./streamlit_app.py
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.write("Hello, World!")  # <p>
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.write("Hello, World!")
# st.write("I'm Dariush Tasdighi!")
# **************************************************

# **************************************************
# In One Line!
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.write("Hello, World!", "I'm Dariush Tasdighi!")
# **************************************************

# **************************************************
# Using Markdown
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.header(body="Dariush Tasdighi")  # <h2>

# st.markdown(body="## Dariush Tasdighi")

# st.markdown(body="<h2>Dariush Tasdighi</h2>")

# st.markdown(body="<h2>Dariush Tasdighi</h2>", unsafe_allow_html=True)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.markdown(body="# Dariush Tasdighi")
# st.markdown(body="## Dariush Tasdighi")
# st.markdown(body="### Dariush Tasdighi")
# st.markdown(body="#### Dariush Tasdighi")
# st.markdown(body="##### Dariush Tasdighi")
# st.markdown(body="###### Dariush Tasdighi")
# st.divider()

# # body = """# Dariush Tasdighi
# # ## Dariush Tasdighi
# # ### Dariush Tasdighi
# # #### Dariush Tasdighi
# # ##### Dariush Tasdighi
# # ###### Dariush Tasdighi"""

# body = """
# # Dariush Tasdighi
# ## Dariush Tasdighi
# ### Dariush Tasdighi
# #### Dariush Tasdighi
# ##### Dariush Tasdighi
# ###### Dariush Tasdighi
# """

# st.write(body)
# st.divider()

# st.markdown(body=body)
# st.divider()

# st.write(body)
# st.divider()

# st.write("# Dariush Tasdighi")
# st.write("## Dariush Tasdighi")
# st.write("### Dariush Tasdighi")
# st.write("#### Dariush Tasdighi")
# st.write("##### Dariush Tasdighi")
# st.write("###### Dariush Tasdighi")
# st.divider()
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.header(body="Dariush")
# st.header(body="Dariush", divider="rainbow")
# **************************************************

# **************************************************
# https://gitlab.com/-/snippets/2526872
# https://gist.github.com/rxaviers/7360908
# https://gohugo.io/quick-reference/emojis
# https://github.com/ikatyang/emoji-cheat-sheet
# https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# # نکته مهم: این دستور باید اول نوشته شود
# # st.set_page_config(page_title="Dariush Tasdighi", page_icon="👋")
# st.set_page_config(page_title="Dariush Tasdighi", page_icon="👋", layout="wide")

# st.title(body="👋 Welcome to Dariush's Streamlit App!")  # <h1>
# st.header(body="👋 Welcome to Dariush's Streamlit App!")  # <h2>
# st.subheader(body="👋 Welcome to Dariush's Streamlit App!")  # <h3>

# st.markdown(body="Hello, **Dariush**! :computer:")
# st.markdown(body="Hello, _Dariush_! :kiss:")
# st.divider()

# st.caption(body="This is a small text!")
# st.divider()

# st.write("Hello, World! :wave:")
# st.write("[Learn More](https://IranianExperts.ir)")
# st.divider()

# code_example = """
# def greet(name):
#     result = f'Hello, {name}!'
#     return result
# """

# st.code(body=code_example, language="python")
# st.divider()
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.warning(body="Warning")
# st.divider()

# st.error(body="Error")
# st.divider()

# st.info(body="Info")
# st.divider()

# st.success(body="Success")
# st.divider()

# ex = RuntimeError("This is an exception of type RuntimeError")
# st.exception(exception=ex)
# st.divider()
# **************************************************

# **************************************************
# Display Image
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# # آدرس‌دهی نسبی
# image_file_path = "./static/images/dariush_tasdighi.jpg"

# # آدرس‌دهی فیزیکی
# # image_file_path = os.path.join(os.getcwd(), "static", "images", "dariush_tasdighi.jpg")

# # st.image(image=image_file_path)
# st.image(image=image_file_path, width=200)

# st.write(image_file_path)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# pressed = st.button(label="Press Me")

# if pressed:
#     st.write("You pressed the button!")
# **************************************************

# **************************************************
# Learning: toast()
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# pressed = st.button(label="Press Me")

# if pressed:
#     st.toast(body="Wow! You did it...", icon="👋")

#     st.write("You pressed the button!")
# **************************************************

# **************************************************
# یک چیز باحال و هیجان‌انگیز
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# button_1_pressed = st.button(label="Button (1)")

# if button_1_pressed:
#     st.snow()
#     st.write("You pressed the button (1)!")

# button_2_pressed = st.button(label="Button (2)")

# if button_2_pressed:
#     st.balloons()
#     st.write("You pressed the button (2)!")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# name = st.text_input(label="Name")

# st.write(f"Hello, {name}!")
# **************************************************

# **************************************************
# Python Note!
# **************************************************
# name = ""
# # name = None
# # name = "Dariush"

# if name:
#     print("Name is not None! and is not Null String")

# if name is not None and name != "":
#     print("Name is not None! and is not Null String")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# name = st.text_input(label="Name")

# # if name is not None and name != "":
#     # st.write(f"Hello, {name}!")

# if name:
#     st.write(f"Hello, {name}!")
# **************************************************

# **************************************************
# یک مشکل اساسی
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# number = 0

# pressed = st.button(label="Press Me")

# if pressed:
#     number += 1
#     st.write(f"Number: {number}")
# **************************************************

# **************************************************
# حل مشکل اساسی
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# # دستور ذیل صحیح نمی‌باشد
# # st.session_state.number = 0

# # if not st.session_state.get(key="number"):
# #     st.session_state.number = 0

# # OR

# if "number" not in st.session_state:
#     st.session_state.number = 0

# pressed = st.button(label="Press Me")

# if pressed:
#     st.session_state.number += 1
#     st.write(f"Number: {st.session_state.number}")
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")
# # st.set_page_config(page_title="DT Chatbot", page_icon="👋", layout="wide")

# st.title(body="DT Chatbot")

# with st.sidebar:
#     st.subheader(body="Settings")

# st.chat_input(placeholder="Type your question here...")

# with st.chat_message(name="AI"):
#     st.write("Hello! How can I help you?")

# with st.chat_message(name="Human"):
#     st.write("I want to know about your products.")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# st.title(body="DT Chatbot")

# with st.sidebar:
#     st.subheader(body="Settings")

# user_query = st.chat_input(placeholder="Type your question here...")

# if user_query:
#     with st.chat_message(name="Human"):
#         st.write(user_query)

#     with st.chat_message(name="AI"):
#         st.write(f"I don't know! {user_query}")
# **************************************************

# **************************************************
# import os
# import streamlit as st


# def get_response(user_query: str) -> str:
#     response = f"I don't know! {user_query}"
#     return response


# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# st.title(body="DT Chatbot")

# with st.sidebar:
#      st.subheader(body="Settings")

# user_query = st.chat_input(placeholder="Type your question here...")

# if user_query:
#     response = get_response(user_query=user_query)

#     with st.chat_message(name="Human"):
#         st.write(user_query)

#     with st.chat_message(name="AI"):
#         st.write(response)
# **************************************************

# **************************************************
# We Need Chat History, But There is a Problem!
# **************************************************
# import os
# import streamlit as st


# def get_response(user_query: str) -> str:
#     response = f"I don't know! {user_query}"
#     return response


# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# st.title(body="DT Chatbot")

# # chat_history = []
# chat_history = [
#     {"role": "assistant", "content": "Hello, I'm Dariush. How can I help you?"}
# ]

# with st.sidebar:
#     st.subheader(body="Settings")

# user_query = st.chat_input(placeholder="Type your question here...")

# if user_query:
#     response = get_response(user_query=user_query)

#     chat_history.append({"role": "user", "content": user_query})
#     chat_history.append({"role": "assistant", "content": response})

# st.write(chat_history)
# **************************************************

# **************************************************
# Fix the previous problem with session state
# **************************************************
# import os
# import streamlit as st


# def get_response(user_query: str) -> str:
#     response = f"I don't know! {user_query}"
#     return response


# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# st.title(body="DT Chatbot")

# if st.session_state.get(key="chat_history") is None:
#     # st.session_state.chat_history = []
#     st.session_state.chat_history = [
#         {"role": "assistant", "content": "Hello, I'm Dariush. How can I help you?"}
#     ]

# with st.sidebar:
#     st.subheader(body="Settings")

# user_query = st.chat_input(placeholder="Type your question here...")

# if user_query:
#     response = get_response(user_query=user_query)

#     st.session_state.chat_history.append({"role": "user", "content": user_query})
#     st.session_state.chat_history.append({"role": "assistant", "content": response})

# st.write(st.session_state.chat_history)
# **************************************************

# **************************************************
# Final Code! (English)
# **************************************************
# import os
# import streamlit as st


# def get_response(user_query: str) -> str:
#     response = f"I don't know! {user_query}"
#     return response


# os.system(command="cls")

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# st.title(body="DT Chatbot")

# if st.session_state.get(key="chat_history") is None:
#     st.session_state.chat_history = [
#         {"role": "assistant", "content": "Hello, I'm Dariush. How can I help you?"}
#     ]

# with st.sidebar:
#     st.subheader(body="Settings")

# user_query = st.chat_input(placeholder="Type your question here...")

# if user_query:
#     response = get_response(user_query=user_query)

#     st.session_state.chat_history.append({"role": "user", "content": user_query})
#     st.session_state.chat_history.append({"role": "assistant", "content": response})

# # st.write(st.session_state.chat_history)
# # for message in st.session_state.chat_history:

# for index, message in enumerate(st.session_state.chat_history):
#     if message["role"] == "user":
#         with st.chat_message(name="Human"):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name="AI"):
#             st.write(message["content"])
# **************************************************

# **************************************************
# Final Code! (Persian)
# **************************************************
# import os
# import streamlit as st


# def get_response(user_query: str) -> str:
#     response = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_query}"
#     return response


# os.system(command="cls")

# st.set_page_config(page_title="پشتیبانی شرکت ما", page_icon="👋")

# streamlit_style = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container, section, input, textarea {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """

# st.markdown(body=streamlit_style, unsafe_allow_html=True)

# st.title(body="ربات پشتیبانی داریوش تصدیقی")

# if st.session_state.get(key="chat_history") is None:
#     st.session_state.chat_history = [
#         {
#             "role": "assistant",
#             "content": "سلام، وقت به خیر. من داریوش تصدیقی هستیم، چه کمکی می‌تونم به شما بکنم؟",
#         }
#     ]

# with st.sidebar:
#     st.subheader(body="تنظیمات")

# user_query = st.chat_input(placeholder="لطفا سوال خودتان را اینجا بنویسید...")

# if user_query:
#     response = get_response(user_query=user_query)

#     st.session_state.chat_history.append({"role": "user", "content": user_query})
#     st.session_state.chat_history.append({"role": "assistant", "content": response})

# # st.write(st.session_state.chat_history)

# for index, message in enumerate(st.session_state.chat_history):
#     if message["role"] == "user":
#         with st.chat_message(name="Human"):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name="AI"):
#             st.write(message["content"])
# **************************************************

# **************************************************
# Final Code! (Persian) with API Key
# **************************************************
import os
import streamlit as st


def get_response(user_query: str) -> str:
    response = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_query}"
    return response


os.system(command="cls")

st.set_page_config(page_title="پشتیبانی شرکت ما", page_icon="👋")

streamlit_style = """
<style>
    @import url('https://fonts.cdnfonts.com/css/iransansx');

    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
        font-family: 'IRANSansX', tahoma !important;
    }

    .block-container, section, input, textarea {
        direction: rtl;
        text-align: justify;
    }
</style>
"""

st.markdown(body=streamlit_style, unsafe_allow_html=True)

st.header(body="تیم پشتیبانی شرکت ما، در خدمت شما می‌باشد", divider="rainbow")

if "api_key" not in st.session_state:
    st.session_state.api_key = ""
    st.error(body="لطفا برای انجام عملیات، API Key را وارد نمایید!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": "You are a C# and Python expert developer assistant.",
        },
        {
            "role": "assistant",
            "content": "سلام، وقت به خیر. من داریوش تصدیقی هستیم، چه کمکی می‌تونم به شما بکنم؟",
        },
    ]

with st.sidebar:
    st.subheader(body="تنظیمات")

    st.session_state.api_key = st.text_input(label="API Key")

if st.session_state.api_key:
    user_query = st.chat_input(placeholder="لطفا سوال خودتان را اینجا بنویسید...")

    if user_query:
        response = get_response(user_query=user_query)

        st.session_state.chat_history.append({"role": "user", "content": user_query})
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    for index, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            with st.chat_message(name="Human"):
                st.write(message["content"])
        elif message["role"] == "assistant":
            with st.chat_message(name="AI"):
                st.write(message["content"])
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# # data_frame = pd.read_csv("./data/users.csv")
# data_frame = pd.read_csv("./data/movies.csv")
# st.write(data_frame)
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# st.title(body="Working with Pandas!")

# data_frame = pd.DataFrame(
#     {
#         "Name": ["Alice", "Bob", "Charlie", "David"],
#         "Age": [25, 32, 37, 45],
#         "Occupation": ["Engineer", "Doctor", "Artist", "Chef"],
#     }
# )

# st.subheader(body="write()")
# st.write(data_frame)
# st.divider()

# st.subheader(body="dataframe()")
# st.dataframe(data=data_frame)
# st.divider()

# st.subheader(body="table() -> Static Table")
# st.table(data=data_frame)
# st.divider()

# st.subheader(body="data_editor() -> Editable Table")
# editable_data_frame = st.data_editor(data=data_frame)
# print(editable_data_frame)
# st.divider()

# st.subheader(body="Metrics")
# st.metric(label="Total Rows", value=len(data_frame))
# st.metric(label="Average Age", value=round(data_frame["Age"].mean(), 1))

# st.subheader(body="JSON and Dictionary")
# sample_dictionary = {
#     "name": "Dariush",
#     "age": 52,
#     "skills": {"C#", "Python", "AI", "Cyber Security"},
# }

# st.subheader(body="write()")
# st.write(sample_dictionary)

# st.subheader(body="json()")
# st.json(body=sample_dictionary)

# st.divider()
# st.write("Data:", sample_dictionary)
# **************************************************

# **************************************************
# *** Multipage App
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.header(body="Welcome to Dariush Site!", divider="rainbow")

# st.link_button(label="About", url="/about")
# st.link_button(label="Contact", url="/contact")
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.header(body="Dariush", divider="rainbow")

# # data_frame = yf.download(tickers="AAPL", period="1d", interval="1m")
# data_frame = yf.download(tickers="AAPL", start="2024-01-01", end="2024-01-31")

# st.table(data=data_frame)
# st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.selectbox(label="Select a ticker", options=tickers, index=1)

# if dropdown:
#     st.write(dropdown)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)
# # dropdown = st.multiselect(label="Select tickers", options=tickers, default=["ETH-USD"])

# if len(dropdown) > 0:
#     # st.write(dropdown)
#     for item in dropdown:
#         st.write(item)
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)

# start_date = st.date_input(label="Start Date", value="today")
# end_date = st.date_input(label="End Date", value="today")

# if len(dropdown) > 0:
#     data_frame = yf.download(tickers=dropdown, start=start_date, end=end_date)

#     st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# https://www.varzesh3.com
# https://www.varzesh3.com/news
# https://search-api.varzesh3.com/v1.0/query?q=طارمی
# **************************************************
# import os
# import requests

# os.system(command="cls")

# url = "https://search-api.varzesh3.com/v1.0/query?q=طارمی"

# response = requests.get(url=url)

# print("-" * 50)
# print("response:", response)
# print("-" * 50)
# print("response.status_code:", response.status_code)
# print("-" * 50)
# print("response.encoding:", response.encoding)
# print("-" * 50)
# print("response.headers['content-type']:", response.headers["content-type"])
# print("-" * 50)

# if response.status_code == 200:
#     print("response.text:")
#     print()
#     print(response.text)  # Note: -> "
#     print("-" * 50)
#     print("response.json():")
#     print()
#     print(response.json())  # Note: -> '
#     print("-" * 50)

#     data = response.json()
#     for index, item in enumerate(data["news"]):
#         row_index = index + 1

#         id = item["id"]
#         title = item["title"]
#         published_on = item["publishedOn"]

#         message = f"{row_index}: id: {id} - Published On: {published_on} - {title}"

#         print(message)
# **************************************************

# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# st.title(body="Search in Varzesh3 Site")

# search = st.text_input(label="Search")

# url = f"{base_url}{search}"
# response = requests.get(url=url)

# if response.status_code == 200:
#     data = response.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         #         message = f"""
#         # ### {title}
#         # - {short_description}
#         # - زمان انتشار: {persian_published_on}
#         # """

#         #         st.write(message)

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# https://www.cdnfonts.com/iransansx.font
# https://www.cdnfonts.com/iranian-sans.font
# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# streamlit_style = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """

# st.markdown(body=streamlit_style, unsafe_allow_html=True)

# st.title(body="جستجو در سایت ورزش سه")

# search = st.text_input(label="جستجو")

# url = f"{base_url}{search}"
# response = requests.get(url=url)

# if response.status_code == 200:
#     data = response.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import streamlit as st

# st.set_page_config(page_title="Dariush Tasdighi", page_icon="👋", layout="wide")

# with st.container():
#     st.title("👋 Welcome to Dariush's Streamlit App!")
#     st.subheader("👋 Welcome to Dariush's Streamlit App!")
#     st.write("Hello, World! :wave:")
#     st.write("[Learn More >](https://IranianExperts.ir)")

# with st.container():
#     st.write("---")

#     left_column, right_column = st.columns(2)

#     with left_column:
#         st.header("Dariush Tasdighi")
#         st.write("##")
#         st.write(
#             """
# I am a student at the University of Tehran.
# I take courses in Computer Science and Mathematics.
# I teach:
# - Python
# - C++
# - C#
# - Java
# """)

#     with right_column:
#         st.header("Dariush Tasdighi")
# **************************************************

# **************************************************
# import streamlit as st

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Dariush's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# with st.sidebar:
#     st.header("About")
#     st.write("This is my first app!")

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Dariush's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************
