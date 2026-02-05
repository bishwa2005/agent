import streamlit as st
from agents.planner import plan
from agents.executer import execute
from agents.verifier import verify

st.set_page_config(
    page_title="AI Operations Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Operations Assistant")
st.caption("Multi-Agent System using Gemini + Real APIs")

st.markdown("""
Enter a natural language task like:
- *Find trending GenAI GitHub repos and show weather in Bangalore*
""")

task = st.text_area("📝 Enter your task", height=100)

if st.button("🚀 Run Assistant"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Planner Agent is thinking..."):
            try:
                plan_json = plan(task)
                st.subheader("🧠 Planner Output")
                st.json(plan_json)
            except Exception as e:
                st.error("Planner failed")
                st.exception(e)
                st.stop()

        with st.spinner("Executor Agent is calling tools..."):
            try:
                execution_result = execute(plan_json)
                st.subheader("⚙️ Executor Output")
                st.json(execution_result)
            except Exception as e:
                st.error("Executor failed")
                st.exception(e)
                st.stop()

        with st.spinner("Verifier Agent is validating output..."):
            try:
                final_output = verify(execution_result)
                st.subheader("✅ Final Verified Output")
                st.json(final_output)
            except Exception as e:
                st.error("Verifier failed")
                st.exception(e)
