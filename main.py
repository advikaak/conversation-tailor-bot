from classifier import classify
from responder import build_reply

def run():
    print("Conversation Tailor Bot — CLI")
    goal = input("Business goal (e.g., schedule a call / collect email / book demo): ").strip()
    print("Type a message (or 'quit')\n")
    while True:
        text = input("User: ").strip()
        if text.lower() in {"quit","exit"}:
            break
        meta = classify(text)
        reply, cta = build_reply(text, goal, meta["style"])
        print(f"\n[detected] style={meta['style']} sentiment={meta['sentiment']} tone={meta['tone']}")
        print(f"Bot: {reply}\nCTA: {cta}\n")

if __name__ == "__main__":
    run()
