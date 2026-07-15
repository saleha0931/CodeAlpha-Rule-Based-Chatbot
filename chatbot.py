"""
Project : Rule Based Chatbot

Internship : CodeAlpha Python Programming

Developed By

Saleha Shahid

University of Management and Technology
--------------------------------------------------
A simple but polished rule-based chatbot. Matches user input
against keyword patterns (not just exact phrases) and replies
accordingly. Keeps a log of the conversation and can save it
to a file at the end.

Key concepts used: if-elif, functions, loops, input/output.

Run:  python chatbot.py
"""

import os
import random
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class _NoColor:
        def __getattr__(self, name):
            return ""
    Fore = _NoColor()
    Style = _NoColor()


BOT_NAME = "Deedee"


# ------------------------------------------------------------
# UI helpers
# ------------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def box(title, width=58, color=Fore.CYAN):
    print(color + "╔" + "═" * (width - 2) + "╗")
    print(color + "║" + title.center(width - 2) + "║")
    print(color + "╚" + "═" * (width - 2) + "╝" + Style.RESET_ALL)


def divider(width=58, char="─", color=Fore.LIGHTBLACK_EX):
    print(color + char * width + Style.RESET_ALL)


def show_welcome_screen():
    clear_screen()
    art = r"""
    ____  ________________  ____________
   / __ \/ ____/ ____/ __ \/ ____/ ____/
  / / / / __/ / __/ / / / / __/ / __/
 / /_/ / /___/ /___/ /_/ / /___/ /___
/_____/_____/_____/_____/_____/_____/

      C H A T B O T
"""
    print(Fore.MAGENTA + Style.BRIGHT + art + Style.RESET_ALL)
    box(f"Chat with {BOT_NAME}! 🤖", color=Fore.CYAN)
    print(Fore.WHITE + f"""
  {BOT_NAME} can chat about greetings, how you're doing,
  what it can do, and more. Type 'help' anytime to see
  what it understands, or 'bye' to end the chat.
""" + Style.RESET_ALL)
    divider()
    input(Fore.GREEN + "\n  Press Enter to start chatting..." + Style.RESET_ALL)


# ------------------------------------------------------------
# Response rules
# key: list of trigger keywords (matched anywhere in the input)
# value: list of possible replies (chosen at random for variety)
# ------------------------------------------------------------
RULES = [
    (["haha", "hehe", "lol", "lmao", "rofl", "😂", "🤣"],
     ["Glad that made you laugh! 😄",
      "Haha, I'm funnier than I thought!",
      "That's the reaction I was hoping for!",
      "Hehe, love that."]),

    (["good morning"],
     ["Good morning! Hope you have a great day ahead.",
      "Morning! Ready to get things done today?"]),

    (["good night"],
     ["Good night! Sleep well.", "Night! Take care."]),

    (["good evening"],
     ["Good evening! How was your day?"]),

    (["hello", "hi", "hey", "salam", "assalam"],
     ["Hi there! How can I help you today?",
      "Hello! Nice to hear from you.",
      "Hey! What's on your mind?"]),

    (["how are you", "how're you", "kya haal"],
     ["I'm doing great, thanks for asking! How about you?",
      "I'm just a program, but I'm running smoothly! And you?",
      "Can't complain, I run on electricity, not stress! How's your day going?"]),

    (["i am fine", "i'm fine", "i'm good", "i am good", "doing well", "im good"],
     ["Glad to hear that!", "That's great, keep it up!"]),

    (["i am sad", "i'm sad", "feeling down", "i am tired", "i'm tired", "i am bored", "i'm bored"],
     ["Sorry to hear that. Sometimes a short break helps.",
      "That's tough. Hope things get better soon.",
      "I hear you. Maybe a quick walk or a joke could help — want to hear one?"]),

    (["i am happy", "i'm happy", "i am excited", "i'm excited"],
     ["That's awesome! Glad you're feeling good.",
      "Nice! What's making you happy today?"]),

    (["your name", "who are you"],
     [f"I'm {BOT_NAME}, a simple rule-based chatbot built in Python.",
      f"You can call me {BOT_NAME}!"]),

    (["my name is", "i am ", "i'm ", "call me"],
     ["name_capture"]),  # handled specially in get_response

    (["how old are you", "your age"],
     ["I don't have an age — I was just written in Python a little while ago!"]),

    (["what can you do", "help", "commands"],
     ["I can chat about greetings, how you're feeling, tell you the time or "
      "date, tell a joke, and remember your name if you tell me. Try saying "
      "'hello', 'how are you', 'joke', or 'my name is ...'."]),

    (["thank", "thanks", "shukriya"],
     ["You're welcome!", "Anytime!", "Happy to help!"]),

    (["love you", "i like you", "you are great", "you're great", "good bot", "well done"],
     ["Aww, thank you! That means a lot.", "You're too kind!"]),

    (["weather"],
     ["I can't check live weather yet, but I hope it's nice where you are!"]),

    (["time"],
     [lambda: f"My clock says it's {datetime.now().strftime('%I:%M %p')} right now."]),

    (["date"],
     [lambda: f"Today's date is {datetime.now().strftime('%B %d, %Y')}."]),

    (["joke", "funny"],
     ["Why do programmers prefer dark mode? Because light attracts bugs!",
      "I told my computer I needed a break, and it said: 'No problem — "
      "I'll go to sleep.'",
      "Why do Python programmers wear glasses? Because they can't C!"]),

    (["favorite color", "favourite color"],
     ["I'd say cyan — it just looks good in a terminal!"]),

    (["favorite food", "favourite food"],
     ["I run on electricity, but if I had to pick, I'd say bytes and bits!"]),

    (["bye", "goodbye", "exit", "quit", "khuda hafiz"],
     ["Goodbye! Have a great day!",
      "Bye! Talk to you soon.",
      "See you later!"]),
]

FALLBACK_REPLIES = [
    "I'm not sure I understand. Try 'help' to see what I can do.",
    "Hmm, I don't have an answer for that yet. Type 'help' for ideas.",
    "Sorry, I didn't quite get that. Could you rephrase?",
]

EXIT_KEYWORDS = ["bye", "goodbye", "exit", "quit", "khuda hafiz"]

NAME_PATTERNS = ["my name is", "i am ", "i'm ", "call me"]


def extract_name(text):
    """Very simple name extraction for phrases like 'my name is Sara'."""
    lowered = text.lower()
    for pattern in NAME_PATTERNS:
        if pattern in lowered:
            idx = lowered.find(pattern) + len(pattern)
            candidate = text[idx:].strip().strip(".!,").split()
            if candidate:
                return candidate[0].capitalize()
    return None


def get_response(user_input, session):
    text = user_input.lower().strip()

    for keywords, replies in RULES:
        if any(keyword in text for keyword in keywords):
            if replies == ["name_capture"]:
                name = extract_name(user_input)
                if name:
                    session["name"] = name
                    return f"Nice to meet you, {name}! I'll remember that."
                return "Nice to meet you! What should I call you?"

            reply = random.choice(replies)
            return reply() if callable(reply) else reply

    return random.choice(FALLBACK_REPLIES)


def is_exit(user_input):
    text = user_input.lower().strip()
    return any(keyword in text for keyword in EXIT_KEYWORDS)


# ------------------------------------------------------------
# Main chat loop
# ------------------------------------------------------------
def main():
    show_welcome_screen()
    transcript = []
    session = {"name": None}

    while True:
        user_input = input(Fore.YELLOW + "You: " + Style.RESET_ALL).strip()

        if not user_input:
            continue

        response = get_response(user_input, session)
        print(Fore.CYAN + f"{BOT_NAME}: " + Style.RESET_ALL + response)

        transcript.append(("You", user_input))
        transcript.append((BOT_NAME, response))

        if is_exit(user_input):
            break

    save = input(Fore.YELLOW + "\nSave this chat transcript? (y/n): "
                 + Style.RESET_ALL).strip().lower()
    if save == "y":
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"chat_transcript_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Chat with {BOT_NAME} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 40 + "\n")
            for speaker, line in transcript:
                f.write(f"{speaker}: {line}\n")
        print(Fore.GREEN + f"✔  Transcript saved to: {filename}" + Style.RESET_ALL)

    print(Fore.MAGENTA + "\nThanks for chatting! 👋\n" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
