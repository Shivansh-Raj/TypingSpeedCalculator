from flask import Flask, render_template, request, jsonify
from time import *
import random as r

app = Flask(__name__)

random_lines = [
    "The quick brown fox jumps over the lazy dog.",
    "How razorback-jumping frogs can level six piqued gymnasts!",
    "Pack my box with five dozen liquor jugs.",
    "Jackdaws love my big sphinx of quartz.",
    "Amazingly few discotheques provide jukeboxes.",
    "The five boxing wizards jump quickly.",
    "Sphinx of black quartz, judge my vow.",
    "Sixty zippers were quickly picked from the woven jute bag.",
    "Jinxed wizards pluck ivy from the big quilt.",
    "Woven silk pyjamas exchanged for blue quartz.",
    "Brawny gods just flocked up to quiz and vex him.",
    "Mr. Jock, TV quiz PhD, bags few lynx.",
    "A wizard’s job is to vex chumps quickly in fog.",
    "The big dwarf only jumps.",
    "My girl wove six dozen plaid jackets before she quit.",
    "Hazy lazy dog on the foggy lawn barks away.",
    "Big July earthquakes confound zany experimental vow.",
    "Quirky, brown fox jumps over a dog in the night.",
    "A quick movement of the enemy will jeopardize six gunboats.",
    "Jim quickly realized that the beautiful gowns are expensive.",
    "All questions asked by five watch experts amazed the judge.",
    "Back in June, we delivered oxygen equipment of the same size.",
    "The jukebox near the back end played music throughout the day.",
    "An expert in speed-reading has saved so much time.",
    "We promptly judged antique ivory buckles for the next prize.",
    "A large fawn jumped quickly over white zinc boxes.",
    "The twelve tagged jayhawks stopped quickly and gazed at the fireworks.",
    "Crazy Frederick bought many very exquisite opal jewels.",
    "Jack quietly moved up front and seized the big ball of wax.",
    "Six big juicy steaks sizzled in a pan as five workmen left the quarry.",
    "Puzzled women bequeath jerks very exotic gifts.",
    "The vixen jumped quickly over the sleeping dog.",
    "Jaded zombies acted quaintly but kept driving their oxen forward.",
    "The quick brown fox quickly jumps over the lazy dog.",
    "Foxy parsons quiz and cajole the lovably dim wiki-girl.",
    "The hungry bunny ate all the carrots in the garden.",
    "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.",
    "The job of waxing linoleum frequently peeves chintzy kids.",
    "Sixty zippers were quickly picked from the woven jute bag.",
    "The town was flooded, and many houses were damaged.",
    "The cat jumped onto the roof and then into the tree.",
    "She sells sea shells by the sea shore.",
    "Peter Piper picked a peck of pickled peppers.",
    "Betty Botter bought some butter, but she said the butter’s bitter.",
    "Sally sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "Sheena leads, Sheila needs.",
    "I scream, you scream, we all scream for ice cream.",
    "Rubber baby buggy bumpers.",
    "Unique New York, unique New York.",
    "Toy boat, toy boat, toy boat.",
    "Red lorry, yellow lorry, red lorry, yellow lorry.",
    "You know New York, you need New York, you know you need unique New York.",
    "Irish wristwatch, Swiss wristwatch.",
    "She sells sea shells beside the sea shore.",
    "Good blood, bad blood, good blood, bad blood.",
    "Three free throws.",
    "Truly rural.",
    "I wish to wish the wish you wish to wish, but if you wish the wish the witch wishes, I won't wish the wish you wish to wish.",
    "I saw Susie sitting in a shoeshine shop.",
    "I thought a thought but the thought I thought wasn't the thought I thought I thought.",
    "A big black bear sat on a big black rug.",
    "I slit a sheet, a sheet I slit, and on that slitted sheet I sit.",
    "She sells seashells by the seashore.",
    "Black bug bleeds black blood. Or does a black bug bleed red blood?",
    "Lesser leather never weathered wetter weather better.",
    "If a dog chews shoes, whose shoes does he choose?",
    "How many cookies could a good cook cook If a good cook could cook cookies?",
    "Peter Piper picked a peck of pickled peppers.",
    "Which wristwatches are Swiss wristwatches?",
    "I scream, you scream, we all scream for ice cream.",
    "I saw Susie sitting in a shoeshine shop.",
    "Wayne went to Wales to watch walruses.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "How can a clam cram in a clean cream can?",
    "Sheena leads, Sheila needs.",
    "I wish to wish the wish you wish to wish, but if you wish the wish the witch wishes, I won't wish the wish you wish to wish.",
    "Six sticky skeletons.",
    "The sixth sick sheik's sixth sheep's sick.",
    "The great Greek grape growers grow great Greek grapes.",
    "Which wristwatches are Swiss wristwatches?",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "How can a clam cram in a clean cream can?",
    "Red lorry, yellow lorry.",
    "Four fine fresh fish for you.",
    "Six slimy snails slid slowly seaward.",
    "Sally sells seashells by the seashore.",
    "How much ground would a groundhog hog, if a groundhog could hog ground?",
    "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn't very fuzzy, was he?",
    "Denise sees the fleece, Denise sees the fleas. At least Denise could sneeze and feed and freeze the fleas.",
    "Gobbling gorgoyles gobbled gobbling goblins.",
    "The great Greek grape growers grow great Greek grapes.",
    "She sells sea shells beside the sea shore.",
    "Toy boat, toy boat, toy boat.",
    "Good blood, bad blood.",
    "Silly Sally swiftly shooed seven silly sheep.",
    "A big bug bit the little beetle, but the little beetle bit the big bug back.",
    "Six slippery snails slid slowly seaward.",
    "Nine nice night nurses nursing nicely.",
    "A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.",
    "Round and round the rugged rock, the ragged rascal ran.",
    "She saw Sharif's shoes on the sofa. But was she so sure those were Sharif's shoes?",
    "Swan swam over the sea, swim, swan, swim! Swan swam back again, well swum, swan!",
    "The great Greek grape growers grow great Greek grapes.",
    "Three thin thinkers thinking thick thoughtful thoughts.",
    "Six slippery snails, slid slowly seaward.",
    "Benny bought a bit of butter but the bit of butter was bitter so Benny bought a bit of better butter to make the bitter butter better.",
    "The cat crept through the cornfield and caterwauled.",
    "Shep Schwab shopped at Scott's Schnapps shop; One shot of Scott's Schnapps stopped Schwab's watch.",
    "The boot black brought the black boot back.",
    "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn't very fuzzy, was he?",
    "I saw a kitten eating chicken in the kitchen.",
]
already_fetched = []

typer = {'grave':'Typing so slow, even the ghosts are waiting for updates.',
          'snail':'Typing at a pace that makes glaciers look fast',
          'tortoise': 'Your typing pace makes a sloth look speedy!',
          'rabbit':'His fingers move faster than gossip in a small town!',
          'human':'You types with the enthusiasm of a sloth on a Monday morning!',
          'cheetah':"Keyboards fear the lightning strike of this typist's fingers.",
          'hawk':"Typing with precision and speed, spotting typos from miles away.",
          'formula1':"Racing through words like they're on the final lap.",
          'god':'Their typing speed is so divine, even celestial beings are impressed.',
          'hacker':"Typing at the speed of 'access granted' before you finish typing 'password'."}

def typer_type(speed):
    if(speed<5):
        return 'grave'
    elif(speed<10):
        return 'snail'
    elif(speed<15):
        return 'tortoise'
    elif(speed<20):
        return 'rabbit'
    elif(speed<25):
        return 'human'
    elif(speed<30):
        return 'cheetah'
    elif(speed<35):
        return 'hawk'
    elif(speed<40):
        return 'formula1'
    elif(speed<45):
        return 'god'
    else:
        return 'hacker'
def mistakes(test,user):
    test = test.split(' ')
    user_ip = user.split(' ')
    error =0
    for i in range(len(user_ip)):
        try:
            if (test[i] != user_ip[i]):
                error = error +1
        except:
            if(user_ip[i]):
                error = error + 1
    return [error,len(user_ip),len(test)]

def typing_speed(test_data,user_ip,time):
    print('----------------------->',test_data)
    error=0
    words_count= 0
    test_words =0 
    user_ip = user_ip.split('\n')
    for i in range(len(user_ip)):
        mistake = mistakes(test_data[i],user_ip[i])
        error = error +mistake[0]
        words_count = words_count + mistake[1]
        test_words = test_words + mistake[2]
    wpm = words_count
    accuracy = round(((words_count-error)/words_count)*100,3)
    net_speed = int(wpm*accuracy/100)
    user_type=typer_type(net_speed)
    print(typer[user_type])
    return {'wpm':wpm,'accuracy':accuracy,'net_speed':net_speed,'typer':user_type,'typer_bio':typer[user_type]}

@app.route('/')
def home():
    already_fetched.clear()
    print('emptied list')
    return render_template('index.html')

@app.route('/fetch_test', methods=['POST'])
def test():
    test_line = r.choice(random_lines)
    while( test_line in already_fetched):
        test_line = r.choice(random_lines)
    already_fetched.append(test_line)
    return jsonify({'test_line':test_line})

@app.route('/reset_test', methods=['POST'])
def reset():
    already_fetched.clear()
    return jsonify({})

@app.route('/result', methods=['POST'])
def result():
    user_ip = request.form.get('user_ip')

    result = typing_speed(already_fetched,user_ip,60)
    print(result)
    return result 
