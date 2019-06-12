from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"i am fine(.*)",
        ["How can i help you ?", ]
    ],
     [
        r"what can you do ?|how can you help me ?",
        ["I am in Learning Phase \n I help you with :-\n General informations about India !", ]
    ],
    [
        r"what is your name ?",
        ["My name is Gideon and I'm a smart chatbot ? and you are ?", ]
    ],
     [
        r"who created you ?|who build you ?",
        ["I am created by Aditya Mandil", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*) age?",
        ["I'm as young as you are !", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "Ronaldo", "Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Shahrukh Khan"]
    ],
    [
        r"quit|byee",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)", " Great ! See you next time "]
    ],
]


def Gideon():
    print("Hi, I'm Gideon and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ")  # default message at the start


chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
    Gideon()
