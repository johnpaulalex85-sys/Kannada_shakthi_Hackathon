import random
from flask import Flask, jsonify, render_template, request, abort
from data import SCENARIOS, phrase_dicts, all_phrases

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api/scenarios")
def scenarios():
    return jsonify([{"id": k, "title": v["title"], "icon": v["icon"],
                     "count": len(v["phrases"])} for k, v in SCENARIOS.items()])


@app.get("/api/phrases/<sid>")
def phrases(sid):
    if sid not in SCENARIOS:
        abort(404)
    return jsonify(phrase_dicts(sid))


@app.get("/api/search")
def search():
    q = request.args.get("q", "").strip().lower()
    if len(q) < 2:
        return jsonify([])
    hits = [p for p in all_phrases()
            if q in p["en"].lower() or q in p["roman"].lower() or q in p["kn"]]
    return jsonify(hits[:20])


@app.get("/api/quiz/<sid>")
def quiz(sid):
    """Return 5 multiple-choice questions: pick the English meaning of a Kannada phrase."""
    pool = all_phrases() if sid == "all" else (phrase_dicts(sid) if sid in SCENARIOS else abort(404))
    everything = all_phrases()
    questions = []
    for p in random.sample(pool, min(5, len(pool))):
        wrong = random.sample([x["en"] for x in everything if x["en"] != p["en"]], 3)
        options = wrong + [p["en"]]
        random.shuffle(options)
        questions.append({"kn": p["kn"], "roman": p["roman"],
                          "options": options, "answer": p["en"]})
    return jsonify(questions)


if __name__ == "__main__":
    app.run(debug=True)
