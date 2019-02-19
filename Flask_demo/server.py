import pandas as pd
import numpy as np
from flask import Flask, abort, jsonify, request
from flask_cors import cross_origin
from sklearn.externals import joblib
from json import dumps
import random
import pickle
import json


app = Flask(__name__)


@app.route('/hello', methods=['POST'])
@cross_origin()
def make_predict():
    """
     JSON should look like this

    {"firstName":"John",
    "lastName":"Snow",
    "knows":"nothing"}
    """

    # get data, xform to a dict of  pandas series
    data = request.get_json(force=True)

    # this is just a silly example
    entity = data['ent']
    problem = data['prob']
    msg = data['message']
    #results_dict = dict()
    data = pd.read_csv('test.csv')
    
    #import product_dict
    with open('product_dict.pickle', 'rb') as handle:
            pro_dict = pickle.load(handle)
            
            
    #return value phraser
    def retvals(msg,ent="",prob=""):
            results_dict = dict()
            results_dict['response'] = msg
            results_dict['problem'] = prob
            results_dict['entity'] = ent
            return results_dict
    
    
    #knn fuction
    def knear(msg):
        vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
        selector = pickle.load(open("selector.pickle", "rb"))
    #text = ['my printer is not working']
        
        text = [msg]
        dv1 = vectorizer.transform(text)
        t = selector.kneighbors(dv1, 10, return_distance=False)
        for i in t:
            arry  = data.iloc[i].Product.values
        counts = np.bincount(arry)       
        return np.argmax(counts)
    def probfind(msg):
        vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
        selector = pickle.load(open("selector.pickle", "rb"))
        text = [msg]
        dv1 = vectorizer.transform(text)
        t = selector.kneighbors(dv1, 15, return_distance=False)
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        res = []
        for i in t:
                res = [data.iloc[i].reason.values]
        removetable = str.maketrans('', '', "[]'|:")
        var =[]
        for line in res[0]:
            for word in line.split():    
                r = word.translate(removetable)
                k =stemmer.stem(r)
                var.append(k)
        li = ''
        givenwords = text[0].split()
        for x in givenwords:
            if x in var:
                li += x + ' '
        return li
    
    #check for greeting words or knn
    if not entity and not problem:
        q_dict = {'greet' : ["hello", "hi", "greetings", "sup", "what's up","hey"],
                  'wave' : ["bye", "goodbye", "shutup"]}

        a_dict = {'greet' : ["'sup bro how can i help?", "hey, what can i do for you?", "hola, what's your problem", "hey, what's wrong?"],
                  'wave' : ["ok bye", "see you later", "don't go", "have a good day"]}
        for word in msg.split():
            for key in q_dict.keys():
                if word.lower() in q_dict[key]:
                    result = retvals(random.choice(a_dict[key]))
                    return jsonify(results=result)
                
        #checking for knearest neighbours if not greetings
        identified = pro_dict[knear(msg)]
        res = "i see you have a problem in " + str(identified) + " catogery, right?"
        rdict = retvals(res,identified)
        return jsonify(results=rdict)
    
    
    
    #if problem is already identified but not entity
    if entity and not problem:
        q_dict = {'greet' : ["hello", "hi", "greetings", "sup", "what's up","hey"],
                  'wave' : ["bye", "goodbye", "shutup"]
                  }
        agree_dict = {'agree' : ["yes", "yep", "ya","yaa","yaaa","right"]}
        negate_dict = {'negate' : ["no", "nope", "wrong","why"]}

        a_dict = {'greet' : ["you wanna restart the convo?, ok fine. HELLO", 
                             "why a hello in middle of convo?, fine, hello what can i do for you?", 
                             "ok, restarting the convo, what's your problem", "hey, what's  wrong?(asking again)"],
                  'wave' : ["ok bye", "see you later", "don't go", "have a good day"]
                  }
        agree_dict_1 = {'agree' : ["cool,can you describe the problem further", "yo, describe the problem bit more please",
                             "great i found correctly, so describe a bit more please"]}
        negate_dict_1 = {'negate' : ["oh damn, i am still learning, say your problem again", "oh no, say it again please", 
                              "i am dumass, say your problem again"]}
        for word in msg.split():
            for key in q_dict.keys():
                if word.lower() in q_dict[key]:
                    result = retvals(random.choice(a_dict[key]))
                    return jsonify(results=result)
            for key in agree_dict.keys():
                if word.lower() in agree_dict[key]:
                    result = retvals(random.choice(agree_dict_1[key]),entity)
                    return jsonify(results=result)
            for key in negate_dict.keys():
                if word.lower() in negate_dict[key]:
                    result = retvals(random.choice(negate_dict_1[key]))
                    return jsonify(results=result)
        prob = probfind(msg)
        finalres = "i am able to identify you problem as <strong>" + str(entity) + " - " + prob + "</strong>" +"  ,further process can be giving bot required access or sending request to respective departmnet. currently we don't have the data nor permission"
        fres = retvals(finalres,entity,prob)
        return jsonify(results=fres)
        
    
    if entity and problem:
        restresp = "i've think i've just found you problem. ok then restarting the conversation. Hello, how can i help you?"
        fres = retvals(restresp)
        return jsonify(results=fres)
    
    #knearest neighbours 
    
    
    #results_dict = dict()
    results_dict=retvals("shit happend, that is not expected")
    # return the json
    return jsonify(results=results_dict)
        
if __name__ == '__main__':
    app.run(port=7000, host='0.0.0.0', debug=True)
    
    