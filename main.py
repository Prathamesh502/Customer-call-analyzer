import os
import streamlit as st
import pandas as pd
import re
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=API_KEY,
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0.5,
    max_tokens=512
)

prompt = '''
You are an AI assistant analyzing customer service call transcripts.  
Tasks: 1) Summarize in 2–3 sentences. 2) Identify sentiment: "Positive", "Neutral", or "Negative".  
Transcript: <<< {transcript_text} >>>  
Return ONLY JSON: {{"summary": "...", "sentiment": "..."}}
'''

from langchain.prompts import PromptTemplate
template = PromptTemplate(template=prompt, input_variables=["transcript_text"])
chain = template | llm

st.title("Customer Call Analyzer")
transcript = st.text_area("Paste transcript here:")

if st.button("Analyze") and transcript.strip() != "":
    response = chain.invoke({"transcript_text": transcript})
    raw = response.content
    matches = re.findall(r'\{[^{}]*\}', raw)
    if matches:
        data = matches[-1]
        import json
        result = json.loads(data)
        summary = result.get("summary", "")
        sentiment = result.get("sentiment", "")
        st.write("**Summary:**", summary)
        st.write("**Sentiment:**", sentiment)
        st.write("**Transcript:**",transcript)
        df = pd.DataFrame([[transcript, summary, sentiment]],
                          columns=["Transcript", "Summary", "Sentiment"])
        df.to_csv("call_analysis.csv", mode="a",
                  header=not os.path.exists("call_analysis.csv"),
                  index=False)
        st.success("Saved ✅")

