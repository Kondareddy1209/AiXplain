# 🎓 Virtual Tutor Agent

An **AI-powered Virtual Tutor Agent** built using **Flask, Gunicorn, and Aixplain**, designed to assist students by answering their questions using Wikipedia and online resources.

![Screenshot 2025-03-23 223529](https://github.com/user-attachments/assets/1ad7902d-5816-4c54-8021-c9b4cea734e2)

## 📖 Table of Contents  
1. Introduction  
2. Features  
3. Technologies Used  
4. Setup and Installation  
5. How It Works  
6. Project Structure  
7. API Endpoints  
8. Live Demo  
9. Future Enhancements  
10. Development  
11. License  

## 🎯 Introduction  
This project leverages **AI-driven question answering** to help students by retrieving information from Wikipedia and other web sources. It uses the **Aixplain framework** to integrate tools for fetching and processing online data.

## ✨ Features  
- AI-based question answering using **Wikipedia and Web Scraper tools**  
- Flask-based **backend with RESTful API**  
- JSON-based response system for easy integration  
- Secure and scalable deployment with **Gunicorn**  
- Error handling and logging for robustness  

## 🔧 Technologies Used  
- **Backend:** Flask (Python)  
- **Web Hosting:** Gunicorn, Render  
- **AI Framework:** Aixplain  
- **Tools:** Wikipedia API, Web Scraper  

## 🛠️ Setup and Installation  
### Prerequisites  
- Python 3.7+  
- Flask & Gunicorn  
- Aixplain API Key  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/virtual-tutor-agent.git  
   cd virtual-tutor-agent  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Set up environment variables:  
   ```bash  
   export TEAM_API_KEY=your_aixplain_api_key  
   ```  
4. Run the application:  
   ```bash  
   python app.py  
   ```  
   Open **http://127.0.0.1:5000/** in your browser.  

## 🚀 How It Works  
1. **User Input:** The user enters a question.  
2. **Processing:** The system fetches data from Wikipedia or other web resources.  
3. **AI Response:** The AI agent processes the data and returns an answer.  
4. **Output:** The response is displayed or returned in JSON format.  

## 📂 Project Structure  
```
virtual-tutor-agent/  
│  
├── app.py                 # Main Flask application  
├── templates/  
│   └── index.html         # Frontend HTML  
├── static/  
│   └── styles.css         # CSS for styling  
├── requirements.txt       # Dependencies  
├── README.md              # Documentation  
└── LICENSE                # Project license  
```

## 🔗 API Endpoints  
### `POST /ask`  
- **Request:** JSON with a `query` field  
  ```json  
  { "query": "What is artificial intelligence?" }  
  ```  
- **Response:** JSON with an AI-generated answer  
  ```json  
  { "response": "Artificial intelligence (AI) is the simulation of human intelligence in machines..." }  
  ```  

## 🌐 Live Demo  
[Live Demo](#)  
(*Replace with the deployed link or keep as a placeholder.*)  

## 🔮 Future Enhancements  
- Integrate more knowledge sources for broader answers  
- Improve response accuracy with AI model fine-tuning  
- Deploy on **Cloud Platforms** (AWS, GCP) for better scalability  

## 🛠️ Development  
1. Fork the repository:  
   ```bash  
   git fork https://github.com/your-username/virtual-tutor-agent.git  
   ```  
2. Create a new branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit changes:  
   ```bash  
   git commit -m "Added a new feature"  
   ```  
4. Push the branch:  
   ```bash  
   git push origin feature-name  
   ```  
5. Open a **Pull Request**.  

## ⚖️ License  
This project is licensed under the **MIT License**.  

---  

**💙 THANK YOU!** 🚀
