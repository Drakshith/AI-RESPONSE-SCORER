# **AI Concept Scoring System**

This project implements a WebSocket-based real-time AI response scoring system. It allows users to respond to AI concept questions, receive scores, and get constructive feedback based on their responses. The system leverages Google Generative AI for grading and feedback generation.

---

## **Features**
- **WebSocket Integration**: Real-time connection between the server and clients.
- **Dynamic AI Concept Questions**: Automatically sends AI-related questions to clients.
- **Real-Time Scoring**: Scores user responses on a scale of 1-10.
- **Personalized Feedback**: Provides detailed, customized feedback for each response.
- **Response Caching**: Optimized using LRU caching to reduce redundant API calls.
- **Concurrent Request Handling**: Handles multiple client connections efficiently.
- **Error Handling**: Robust handling of edge cases and invalid inputs.

---

## **Getting Started**

### **Prerequisites**
- **Python**: Version 3.8 or later
- **Libraries**:
  - `websockets`
  - `streamlit`
  - `cachetools`
  - `google-generativeai`
  - `python-dotenv`

---

### **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-concept-scoring-system.git
   cd ai-concept-scoring-system
   ```

2. Set up a `.env` file in the project root directory:
   ```
   GENAI_API_KEY=your-google-generative-ai-api-key
   ```
---

### **Run the Application**

1. **Start the WebSocket Server**:
   ```bash
   python websocket_server.py
   ```

   This starts the WebSocket server on `ws://localhost:8765`.

2. **Run the Streamlit Client**:
   ```bash
   streamlit run ui.py
   ```

   Access the UI at `http://localhost:8501`.

---



## **Usage**
1. **Connect to WebSocket Server**:
   - Upon connection, a random AI concept question is sent to the client.
   
2. **Submit Responses**:
   - Enter your response in the text box provided in the Streamlit app.
   - Click the **Submit** button to score your response.

3. **View Feedback**:
   - The system returns a score and personalized feedback in real-time.

---

## **Technologies Used**
- **Backend**: Python with `websockets`
- **Frontend**: Streamlit for UI
- **AI API**: Google Generative AI (`gemini-1.5-flash`)
- **Caching**: `cachetools` for efficient response caching

---

## **Testing**

Run unit tests to verify scoring functionality:
```bash
python -m unittest test_scoring.py
```

---

## **Known Issues**
- Initial gRPC warnings may appear but do not impact functionality.
- Long API response times can occur under high load; optimize with caching and retry logic.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/my-new-feature`).
3. Commit your changes and push to the branch.
4. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For questions or support, please contact:
- **Name**: Kodithyala Drakshith  
- **Email**: draksh04@gmail.com 
- **GitHub**: [Drakshith](https://github.com/Drakshith)

