import re

# Simple keyword heuristics. Expand these sets to tune behavior.
NEG_WORDS = {"frustrated","angry","upset","annoyed","mad","disappointed"}
POS_WORDS = {"great","awesome","love","perfect","thanks","appreciate"}
URGENCY_WORDS = {"asap","urgent","now","today","deadline","immediately"}
FORMAL_MARKERS = {"dear","regards","sincerely","sir","madam"}
CASUAL_MARKERS = {"hey","lol","btw","omg","haha","kinda","gonna"}
UNCERTAINTY_MARKERS = {"maybe","not sure","idk","unsure","perhaps","confused"}

def detect_sentiment(text: str) -> str:
    t = text.lower()
    neg = sum(w in t for w in NEG_WORDS)
    pos = sum(w in t for w in POS_WORDS)
    if neg > pos and neg > 0:
        return "negative"
    if pos > neg and pos > 0:
        return "positive"
    return "neutral"

def detect_tone(text: str) -> set:
    t = text.lower()
    tone = set()
    if any(w in t for w in FORMAL_MARKERS):
        tone.add("formal")
    if any(w in t for w in CASUAL_MARKERS):
        tone.add("casual")
    if any(w in t for w in URGENCY_WORDS):
        tone.add("urgent")
    if any(w in t for w in UNCERTAINTY_MARKERS):
        tone.add("uncertain")
    # punctuation cues
    if "!" in t and "?" in t:
        tone.add("stressed")
    return tone

def choose_style(sentiment: str, tone: set) -> str:
    # simple routing
    if "urgent" in tone:
        return "concise_business"
    if sentiment == "negative" or "stressed" in tone:
        return "empathetic"
    if "formal" in tone:
        return "formal"
    if "casual" in tone:
        return "casual"
    if "uncertain" in tone:
        return "motivational"
    return "concise_business"

def classify(text: str) -> dict:
    sentiment = detect_sentiment(text)
    tone = detect_tone(text)
    style = choose_style(sentiment, tone)
    return {"sentiment": sentiment, "tone": list(tone), "style": style}
