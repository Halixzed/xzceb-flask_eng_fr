from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_translated = translator.englishtofrench(textToTranslate)
    return french_translated['translations'][0]['translation']

@app.route("/frenchToEnglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_translated = translator.frenchtoenglish(textToTranslate)    
    return english_translated['translations'][0]['translation']

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
