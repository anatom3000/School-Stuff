from browser import document, html, timer
qcm = [
    {
        "question": "Question 1", 
        "answers": [
            {"text": "dis question bad", "Ambition": -1, "Courage": 7, "Good": 3, "Intelligence": 1},
            {"text": "no its good", "Ambition": -1, "Courage": -1, "Good": 8, "Intelligence": 7},
        ]
    },
    {
        "question": "Question 2",
        "answers":[
            {"text": "haha one answer", "Ambition": -1, "Courage": -1, "Good": -1, "Intelligence": -1}
        ]
    }
]

stats_player = {}

question_num = 0

def draw_question(num):
    document["qcmbox"].html = ''
    qhtml = html.P(id=f'question{num}')
    qhtml <= html.H2(qcm[num]["question"])
    for a in qcm[num]["answers"]:
        qhtml <= html.BUTTON(a.pop('text'), **a)
    document["qcmbox"] <= qhtml

def onanswering(ev):
    if question_num > 0:
        global stats_player
        answers = document[f"question{question_num-1}"]
        for
    if question_num < len(qcm): 
        draw_question(question_num)
        global question_num; question_num += 1

timer.set_interval(onanswering, 2000)

document["qcmbox"] <= html.P(content="TEst")