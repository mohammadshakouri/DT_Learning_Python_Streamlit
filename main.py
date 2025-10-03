import streamlit as st
import chatbot_constants as constants
import chatbot_functions as functions

functions.set_page_config()
functions.initial_session_state()

with st.sidebar:
    st.subheader(body=constants.SETTINGS, divider="rainbow")

    st.session_state.model_name = st.radio(
        index=0,
        options=constants.MODELS,
        label=constants.SELECT_YOUR_MODEL,
    ).strip()

    st.write(constants.SELECTED_MODEL, st.session_state.model_name)
    st.divider()

    st.markdown(body=constants.ABOUT, unsafe_allow_html=True)
    st.divider()

st.header(body=constants.PAGE_HEADER, divider="rainbow")

if not st.session_state.model_name:
    st.error(body=constants.ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME)

if st.session_state.model_name:
    user_prompt: str | None = st.chat_input(
        placeholder=constants.USER_PROMPT_PLACEHOLDER
    )

    if user_prompt:
        user_prompt = user_prompt.strip()

    if user_prompt:
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        assistant_answer = functions.get_assistant_answer(user_prompt=user_prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_answer}
        )

    for index, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            with st.chat_message(name=constants.USER):
                st.write(message["content"])
        elif message["role"] == "assistant":
            with st.chat_message(name=constants.AI):
                st.write(message["content"])