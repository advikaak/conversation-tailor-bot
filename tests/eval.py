import json
from classifier import classify

with open("tests/test_cases.json") as f:
    cases = json.load(f)

correct = 0
for i, c in enumerate(cases, 1):
    meta = classify(c["text"])
    got = meta["style"]
    want = c["expected_style"]
    ok = got == want
    correct += ok
    print(f"{i:02d}. text={c['text']!r}  expected={want}  got={got}  {'✅' if ok else '❌'}")

print(f"\nAccuracy: {correct}/{len(cases)} = {correct/len(cases):.0%}")
