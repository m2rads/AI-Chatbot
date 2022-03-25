from flask import Flask, render_template, request, escape, jsonify, flash, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
# custome methods
from extract_data import extractData
from populate_trainer_data import populateTrainerData
from preprocessor import extract_menu_items


# app configuratoins
app = Flask(__name__)

kamato_bot = ChatBot(
    'Kamato Sushi',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
    )
trainer = ListTrainer(kamato_bot)

menu = populateTrainerData('./static/data/menu.json', 'name', 'price')
conversations = populateTrainerData('./static/data/conversation.json', 'question', 'response')
trainer.train(menu)
print(conversations)
trainer.train(conversations)

app.config["SECRET_KEY"] = 'adb24bb904544d1f488714d369c9de83' # https://docs.python.org/3/library/uuid.html

@app.route("/index")
@app.route("/")
@app.route("/home", methods=['GET'])
def index():
    return render_template("index.html")
    
    
@app.route('/api', methods=['GET'])
def api():
    data = extractData('./static/data/menu.json')
    if data != "failed":
        return jsonify(menu=data, status=200)
    else:
        return jsonify(status=400)

@app.route("/get", methods=['POST'])
def get_response():
    data = request.get_json()
    userInput = data['userInput']
    filtered_input = extract_menu_items(userInput)
    if isinstance(filtered_input, list):
        response = process_multi_select(filtered_input)
    elif isinstance(filtered_input, str):
        response = str(kamato_bot.get_response(filtered_input))
    return jsonify(response=response, status=200)
    
def process_multi_select(userInput):
    total = 0.00
    response = 'Sure, your total is '
    for i in userInput:
        total += float(str(kamato_bot.get_response(i)).replace("$", ""))
    format_total = "{:.2f}".format(total)
    print(format_total)
    
    return response + format_total
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  