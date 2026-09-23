import streamlit as st
from src.gemini_client import improve_email
from src.prompt_engine import build_prompt
from src.utils import validate_email

st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="✉️",
    layout="wide",
)

st.title("✉️ AI Email Assistant")
st.caption("GenAI-powered email rewriting and optimization with Gemini")

with st.sidebar:
    st.header("Email Settings")
    email_type = st.selectbox(
        "Email purpose",
        ["General", "Job Application", "Follow-up", "Meeting Request",
         "Leave Request", "Customer Support", "Complaint", "Business"],
    )
    tone = st.selectbox(
        "Tone",
        ["Professional", "Formal", "Friendly", "Casual", "Persuasive", "Apologetic"],
    )
    length = st.selectbox("Length", ["Short", "Medium", "Detailed"])
    action = st.selectbox("Action", ["Improve", "Rewrite", "Generate Reply", "Summarize"])

left, right = st.columns(2)

with left:
    st.subheader("Original Email")
    email_text = st.text_area(
        "Enter your email",
        height=360,
        placeholder="Paste or write your email here...",
        label_visibility="collapsed",
    )

with right:
    st.subheader("AI Result")
    result_placeholder = st.empty()

if st.button("✨ Process Email", type="primary", use_container_width=True):
    error = validate_email(email_text, action)
    if error:
        st.warning(error)
    else:
        prompt = build_prompt(
            email_text=email_text,
            email_type=email_type,
            tone=tone,
            length=length,
            action=action,
        )

        with st.spinner("Gemini is processing your email..."):
            try:
                result = improve_email(prompt)
                if result:
                    result_placeholder.text_area(
                        "Generated result",
                        value=result,
                        height=360,
                        label_visibility="collapsed",
                    )
                    st.success("Email processed successfully.")
                else:
                    st.error("The model returned an empty response.")
            except Exception as exc:
                st.error(
                    "Unable to process the email. Check your Gemini API configuration "
                    "and try again."
                )
                with st.expander("Technical details"):
                    st.code(str(exc))

st.divider()
st.caption("Security: API credentials are loaded from Streamlit secrets and are never stored in source code.")
