import os

def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('images/negative/All Negatives'):
            f.write('images/negative/All Negatives/'+filename+'\n')