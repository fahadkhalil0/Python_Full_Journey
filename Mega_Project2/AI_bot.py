import pyautogui
import pyperclip
import time
from groq import Groq


# Initialize Groq client
client = Groq(api_key="enter the api key")

def get_last_sender(chat_history: str) -> str:
    """
    Extracts the name of the last sender from WhatsApp chat history text.
    
    Args:
        chat_history (str): Full copied WhatsApp chat text
        
    Returns:
        str: Name of the last sender, or "" if not found
    """
    try:
        # Split by lines and filter out empty lines
        lines = [line.strip() for line in chat_history.strip().split('\n') if line.strip()]
        
        # Look for the last line that contains a timestamp and sender pattern
        for line in reversed(lines):
            # WhatsApp format: [time, date] Sender Name: message
            if '] ' in line and ':' in line:
                # Extract everything after '] ' and before ':'
                after_bracket = line.split('] ', 1)
                if len(after_bracket) > 1:
                    sender_part = after_bracket[1].split(':', 1)
                    if len(sender_part) > 1:
                        sender_name = sender_part[0].strip()
                        print(f"Last sender identified: '{sender_name}'")
                        return sender_name
        
        print("No sender found in chat history")
        return ""
        
    except Exception as e:
        print("⚠️ Error while parsing:", e)
        return ""


# Step 1: Click on the WhatsApp icon
pyautogui.click(868, 871)
time.sleep(2)

# Step 2: Drag to select text (chat history)
pyautogui.moveTo(605, 187)
pyautogui.dragTo(1548, 776, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Step 4: Get from clipboard
chatHistory = pyperclip.paste()
print("Copied chat history:", chatHistory)

last_sender = get_last_sender(chatHistory)
if last_sender and last_sender == "Self": 
    # Agar last sender "Self" hai to reply karo
    # AI response code yahan chalega
    # Agar koi bhi valid sender mila hai to reply karo
    # AI response code yahan chalega 
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
    {"role": "system", "content": "You are chatting like a normal Pakistani friend on WhatsApp. Keep replies short (1-2 lines), casual, and sometimes incomplete. Mix Roman Urdu and English naturally. Never repeat same words every time. Do not sound like a bot. Avoid long explanations. Keep it chill and natural"
    "(just do only message dont give the refrence of sender or receiver with time)."},
    {"role": "user", "content": chatHistory}
    ],
        temperature=0.6,   # balanced & natural
        max_completion_tokens=150,  # short replies only
        top_p=1,
        stream=True,
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content

    print("\nNaruto Reply:\n", response)

    # Step 5: Send AI response to WhatsApp
    # Step 1: Click on WhatsApp text box
    pyautogui.click(1257, 803)   # <- update with your textbox position
    time.sleep(0.5)

    # Step 2: Copy response to clipboard
    pyperclip.copy(response)

    # Step 3: Paste into WhatsApp
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)

    # Step 4: Press Enter to send
    pyautogui.press('enter')
