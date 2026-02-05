import streamlit as st
from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

st.set_page_config(page_title="AI Operations Assistant", layout="centered")

st.title("🤖 AI Operations Assistant")
st.write("Enter a natural language task and let the AI plan, execute, and verify it.")

task = st.text_input("Enter your task:")

if st.button("Run Assistant"):
    if not task:
        st.warning("Please enter a task.")
    else:
        with st.spinner("Planning..."):
            plan = plan_task(task)
            st.subheader("🧠 Planner Output")
            st.json(plan)

        with st.spinner("Executing tools..."):
            results = execute_plan(plan)
            st.subheader("⚙️ Executor Output")
            st.json(results)

        with st.spinner("Verifying and formatting..."):
            final_answer = verify_and_format(results)
            st.subheader("✅ Final Answer")
            st.write(final_answer)
