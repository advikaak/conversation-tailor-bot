from typing import Tuple

def build_reply(user_text: str, goal: str, style: str) -> Tuple[str, str]:
    """
    Returns (reply, next_step) where next_step is a short CTA aligned to the goal.
    """
    goal_cta = {
        "schedule a call": "Does tomorrow or Wednesday 3–5 PM ET work for a quick 15‑min call?",
        "collect email": "What’s the best email to send a quick summary and next steps?",
        "confirm donation": "Would you like me to send the secure donation link now?",
        "book demo": "Can I book you for a 15‑min product walkthrough this week?",
    }
    cta = goal_cta.get(goal.lower().strip(), "What’s the best next step for you?")

    styles = {
        "concise_business": (
            "Thanks for the context—here’s a quick path forward: {goal_sentence} "
            "I can keep it brief and handle details for you."
        ),
        "formal": (
            "Thank you for your message. To move this along efficiently, {goal_sentence} "
            "I’ll ensure everything remains straightforward and professional."
        ),
        "casual": (
            "Got it! Let’s keep this simple—{goal_sentence} "
            "I’ll make it easy on your end."
        ),
        "empathetic": (
            "I hear you—that sounds frustrating. We can keep this focused and low‑lift: {goal_sentence} "
            "I’ll handle the details so it’s smooth for you."
        ),
        "motivational": (
            "Totally understandable. We can make fast progress with a clear step: {goal_sentence} "
            "I’ll make sure this stays simple."
        ),
    }

    template = styles.get(style, styles["concise_business"])
    goal_sentence = ""
    if goal:
        goal_sentence = f"the next best step is to {goal}."
    reply = template.format(goal_sentence=goal_sentence)
    return reply, cta
