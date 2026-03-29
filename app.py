import streamlit as st
import pandas as pd
from openai import OpenAI
import matplotlib.pyplot as plt
import os

st.title("AI Data Analyst")
st.write("Upload data and ask questions")

api_key = st.secrets["OPENAI_API_KEY"]

if not api_key:
    st.error(" API Key not found. Please set OPENAI_API_KEY.")
    st.stop()

client = OpenAI(api_key=api_key)
uploaded_file = st.file_uploader("data.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(" Data Preview")
    st.write(df.head())
    query = st.text_input("Ask a question about your data:")

    if query:
        try:
            with st.spinner("Analyzing your data... "):

                prompt = f"""
                You are a professional data analyst.
                Dataset columns: {df.columns.tolist()}
                Convert the user question into pandas code.
                Rules:
                - Use df as the dataframe
                - Return ONLY valid Python code
                - No explanations
                - No import statements
                - Store final answer in a variable named 'result'
                - Use matplotlib (plt) only if needed
                Question: {query}
                """

                response = client.responses.create(model="gpt-4.1-mini",input=prompt )

                try:
                    code = response.output[0].content[0].text.strip()
                except:
                    code = response.output_text.strip()

                code = code.replace("```python", "").replace("```", "").strip()
                st.write("### Generated Code")
                st.code(code)

                unsafe_keywords = ["import", "__", "open(", "exec(", "eval(", "os.", "sys."]

                if any(word in code for word in unsafe_keywords):
                    st.error("Unsafe code detected! Try a different question.")
                else:
                    local_vars = {"df": df, "plt": plt}
                    exec(code, {}, local_vars)
                    if "result" in local_vars:
                        st.write(" Result")
                        st.write(local_vars["result"])
                    else:
                        st.info("No result returned by AI.")

                    if plt.get_fignums():
                        st.pyplot(plt)
                        plt.close()

        except Exception as e:
            st.error(f"Error: {e}")