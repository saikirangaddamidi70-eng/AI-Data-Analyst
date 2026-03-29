# 🤖 AI Data Analyst

An AI-powered data analysis web application built using Streamlit and OpenAI. This tool allows users to upload datasets, ask questions in natural language, and get insights, results, and visualizations automatically.

---

## 🚀 Features

- Upload CSV datasets  
- Ask questions in natural language  
- Automatic data analysis using AI  
- Generates pandas code dynamically  
- Displays results instantly  
- Supports data visualization using matplotlib  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- OpenAI API  
- Matplotlib  

---

## 📂 Project Structure

app.py              # Main application file  
data.csv            # Sample dataset  
.gitignore          # Ignored files  
README.md           # Project documentation  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/ai-data-analyst.git  
cd ai-data-analyst  

### 2. Install dependencies
pip install streamlit pandas matplotlib openai  

### 3. Add your API Key

Create a folder:
.streamlit  

Inside it, create a file:
secrets.toml  

Add your OpenAI API key:
OPENAI_API_KEY = "your_api_key_here"  

### 4. Run the application
streamlit run app.py  

---

## 📊 Usage

1. Upload your CSV file  
2. Enter a question about your data  
3. View generated results and visualizations  

---

## 🔐 Important Note

This project does not include API keys.  
Users must provide their own OpenAI API key in the `.streamlit/secrets.toml` file.  

---

## 📌 Future Improvements

- Chat history support  
- Advanced data visualizations  
- Multi-file support  
- Export results  

---

## 👨‍💻 Author

Sai Kiran  

---

## 📄 License

This project is for educational and internship purposes.
