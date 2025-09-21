# Customer-call-analyzer
# Customer Query Analysis Bot

This project is an **AI-powered bot** designed to analyze customer service call transcripts.  
It extracts structured insights such as conversation summary and customer sentiment.

---

## 📌 Features
- Takes a **customer service transcript** as input.  
- Uses **OpenAI API** to analyze the conversation.  
- Extracts key points like:
  - **Summary** (2–3 sentences)  
  - **Customer sentiment** (Positive / Negative / Neutral)  
- Saves results in a CSV file for future analysis.  
- Handles raw text and extracts clean JSON using **Regex**.  
- Keeps API keys secure with a `.env` file.  

---

## 🛠️ Tech Stack
- **Python**  
- **Libraries**: `requests`, `json`, `re`, `dotenv`, `pandas`  
- **API**: OpenAI  

---

## 📂 Example Input
Transcript (customer + agent):  
