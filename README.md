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

---

## 📂 Example Output
```json
{
  "summary": "The customer faced a payment failure while booking a slot. The agent asked for the order ID, and the customer expressed frustration.",
  "sentiment": "Negative"
}

---

Do you also want me to **add a “How to Run” section** with the commands (like `pip install -r requirements.txt` + `python main.py`)? That way anyone on GitHub can clone and try it immediately.

