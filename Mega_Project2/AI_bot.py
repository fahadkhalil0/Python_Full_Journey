import pyautogui
import pyperclip
import time
from groq import Groq


# Initialize Groq client
client = Groq(api_key="")

def get_last_sender(chatHistory : str) -> str:
    """
    Extracts the name of the last sender from WhatsApp chat history text.
    
    Args:
        chat_history (str): Full copied WhatsApp chat text
        
    Returns:
        str: Name of the last sender, or "" if not found
    """
    try:
        # Split by lines and filter out empty lines
        lines = [line.strip() for line in chatHistory.strip().split('\n') if line.strip()]
        
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
    
def send_reply(reply_text: str):
    """Clicks on WhatsApp textbox, pastes the reply, and sends it."""
    pyautogui.click(1257, 803)   # <- update apne textbox ke hisaab se
    time.sleep(0.5)

    pyperclip.copy(reply_text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    
    pyautogui.press('enter')


# Step 1: Click on the WhatsApp icon
pyautogui.click(868, 871)
time.sleep(2)

while True:

    # Step 2: Drag to select text (chat history)
    pyautogui.moveTo(605, 187)
    pyautogui.dragTo(1548, 776, duration=1, button='left')
    time.sleep(0.5)

    # Step 3: Copy (Ctrl+C)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)

    pyautogui.click(566, 195)
    time.sleep(8)

    # Step 4: Get from clipboard
    chatHistory = pyperclip.paste()
    print("Copied chat history:", chatHistory)

    keywords_replies = {
        # Greetings
        "Salam": "Wa Alaikum Salam 🤲",
        "assalamualaikum": "Wa Alaikum Salam dost 🤝",
        "hello": "Hello dost 👋",
        "hi": "Hi yaar 😊",
        "hey": "Hey buddy ✌️",
    }


    #Function to process the chat
    def process_last_message(chatHistory: str, my_name = "Fahad Khalil"):
        """
        Processes the chat history to check if the last message is from a person other than you.
        Args:
            chat_history (str): The full WhatsApp chat history text.
            my_name (str): Your name as it appears in the chat.
        """
        last_sender = get_last_sender(chatHistory)
        
        you = "Fahad Khalil"
        if last_sender and last_sender != you:
            print(f"The last message was from '{last_sender}'.")
            print(f"Performing action because the sender is not {you}.")

            for keyword, reply in keywords_replies.items():
                if keyword in last_sender.lower():
                    print(f"Keyword '{keyword}' detected! Replying with: {reply}")
                    send_reply(reply)
                    return


            # 2) AI-based reply
            print("No keyword matched, using AI for reply...")

            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {"role": "system", "content": "You are an AI assistant designed to respond in the persona of a Pakistani friend on WhatsApp. Your replies must be concise (1-2 lines), natural, casual, and politely and respectively. Maintain a natural blend of Roman Urdu and English. Avoid sounding like a bot. Do not use conversational fillers or lengthy explanations. Respond directly to the last message without referencing the sender, receiver, or timestamps."},
                    {"role": "user", "content": chatHistory}
                ],
                temperature=0.6,   # balanced & natural
                max_completion_tokens=150,   # short replies only
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

            # my_name_in_chat= "Fahad Khalil"

        elif last_sender and last_sender == you:
            print("The last message was from you. No action needed.")
        else:
            print("Could not determine the last sender. No action needed.")

    # Call the function to process the chat history and respond if needed
    process_last_message(chatHistory)

        