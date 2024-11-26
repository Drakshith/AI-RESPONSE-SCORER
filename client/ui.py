import streamlit as st
import asyncio
import websockets
import json
from scoring import response_cache, score_response

SERVER_URI = "ws://localhost:8765"

async def send_and_receive():
    try:
        async with websockets.connect(SERVER_URI) as websocket:
            feedback = await websocket.recv()
            return feedback
    except Exception as e:
        return {"error": str(e)}

def main():
    result = asyncio.run(send_and_receive())
    data = json.loads(result)

    question = data.get("question")
    st.title("AI Response Scorer")
    st.caption(question)
    user_response = st.text_area("Enter your response:", placeholder="Type your response here...")
    if st.button("Submit"):
        if user_response.strip():
            with st.spinner("Processing..."):
                if user_response in response_cache:
                    score, feedback = response_cache[user_response]
                else:

                    score, feedback = score_response(
                        question, user_response
                    )

                st.success(f"Score: {score}")
                st.write(f"Feedback: {feedback}")
        else:
            st.warning("Please enter a response.")

if __name__ == "__main__":
    main()
