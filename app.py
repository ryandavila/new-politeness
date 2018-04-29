
import os
import math
from flask import Flask
from flask import render_template, request, jsonify
import json


import politeness
from politeness.classifier import Classifier
from politeness.helpers import set_corenlp_url
import politeness.strategies as ps
set_corenlp_url('http://localhost:9000')

cls = Classifier()

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])


# @app.route("/")
# def hello():
#     return "Hello world, it's the Politeness Classifier!"


@app.route("/")
def text_input_form():
    return render_template("politeness-form.html")


# @app.route("/")
# def text_input_form2():
#     return render_template("politeness-form.html")


@app.route("/score-politeness", methods=['POST'])
def score_text():
    text = request.form['text']
    probs = cls.predict(text)

    # Based on probs, determine label and confidence
    # print(probs)
    # if probs['polite'] > 0.6:
    #     l = "polite"
    #     confidence = probs['polite']
    # elif probs['impolite'] > 0.6:
    #     l = "impolite"
    #     confidence = probs['impolite']
    # else:
    #     l = "neutral"
    #     confidence = 1.0 - math.fabs(probs['polite'] - 0.5)
    #
    # confidence = "%.2f" % confidence

    #new attempt at code
    endIndex = len(probs) - 1
    print(text)
    predictionSeg = probs[endIndex]
    # print(predictionSeg)
    doc = predictionSeg["document"]
    parses = predictionSeg["parses"]


    stratDict = (ps.sentCheck(text))
    #print(parses)
    initialParse = parses[0]
    # print (initialParse)
    # smolParse2 = parses[1]
    # print (smolParse2) #prints information for sentence two, probably

    fullParse = parses[0]
    parsing = fullParse["parses"]
    # print (parsing) #prints information
    formattedParse = str(parsing)
    formattedParse = formattedParse.replace("),", ") , ")


    politeProb = float(doc[0])
    impoliteProb = float(doc[1])
    print(politeProb)
    print(impoliteProb)

    if politeProb > 0.6:
        l = "polite"
        confidence = politeProb
    elif impoliteProb > 0.6:
        l = "impolite"
        confidence = impoliteProb
    else:
        l = "neutral"
        confidence = 1.0 - math.fabs(politeProb - .5)

    confidence = "%.2f" % confidence

    # Return JSON:
    return jsonify(text=text, label=l, confidence=confidence, parsing=formattedParse, strategies=stratDict)


if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 8000))
    # app.run(host='0.0.0.0', port=port)
    set_corenlp_url('localhost:9000')
    app.run()
