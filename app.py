from flask import Flask, render_template, request
from questions import questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def test():
    submitted = False
    score = 0
    result = []

    if request.method == "POST":
        submitted = True

        for q in questions:
            qid = str(q["id"])

            if q["type"] == "multiple":
                selected = request.form.getlist(qid)
            else:
                selected = request.form.get(qid)
                selected = [selected] if selected else []

            correct = q["answer"]

            if set(selected) == set(correct):
                score += 1

            result.append({
                "question": q["question"],
                "selected": selected,
                "correct": correct
            })

    return render_template(
        "test.html",
        questions=questions,
        submitted=submitted,
        score=score,
        total=len(questions),
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
