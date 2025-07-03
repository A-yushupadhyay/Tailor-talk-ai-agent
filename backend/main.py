from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent

app = FastAPI()

#  Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with Streamlit domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "TailorTalk AI Backend is running."}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    print("Received data:", data)  # Debugging line to check incoming data
    user_msg = data.get("message")
    if not user_msg:
        return {"reply": "No message received."}
    
    try:
        reply = run_agent(user_msg)
        print("Agent reply:", reply)  # Debugging line to check agent response
        return {"reply": reply}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
