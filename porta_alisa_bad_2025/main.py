# hi porta one
"""
Дешифратор тексту

Словник найчастіших англійських слів + імена + 10 000(wordsmini.txt)
Жадібний алгоритм

"""
def decrypt(text):
    words = {'the': 50, 'and': 45, 'was': 50, 'of': 50, 'in': 50, 'it': 50, 'a': 50, 'to': 45, 'had': 45, 'she': 40,
             'her': 40, 'he': 40, 'his': 40, 'i': 40, 'alice': 35, 'very': 35, 'book': 35, 'but': 35, 'what': 35,
             'into': 35, 'by': 30, 'on': 30, 'or': 30, 'is': 30, 'no': 30, 'be': 30, 'you': 30, 'not': 30, 'for': 30,
             'are': 30, 'all': 30, 'one': 30, 'with': 30, 'this': 30, 'that': 30, 'have': 30, 'were': 30, 'their': 30,
             'which': 30, 'some': 30, 'time': 30, 'beginning': 25, 'sitting': 25, 'sister': 25, 'tired': 25,
             'having': 25, 'nothing': 25, 'twice': 25, 'peeped': 25, 'reading': 25, 'pictures': 25, 'conversations': 25,
             'thought': 25, 'without': 25, 'beautiful': 25, 'flowers': 25, 'garden': 25, 'student': 25, 'studying': 25,
             'mathematics': 25, 'science': 25, 'library': 25, 'because': 25, 'wanted': 25, 'examinations': 25,
             'running': 25, 'singing': 25, 'working': 25, 'once': 20, 'do': 20, 'so': 20, 'up': 20, 'if': 20, 'as': 20,
             'we': 20, 'me': 20, 'my': 20, 'him': 20, 'from': 20, 'they': 20, 'been': 20, 'said': 20, 'each': 20,
             'them': 20, 'than': 20, 'many': 20, 'good': 20, 'make': 20, 'take': 20, 'come': 20, 'know': 20,
             'think': 20, 'look': 20, 'find': 20, 'give': 20, 'tell': 20, 'ask': 20, 'try': 20, 'help': 20, 'work': 20,
             'happy': 20, 'old': 20, 'big': 20, 'long': 20, 'first': 20, 'last': 20, 'much': 20, 'most': 20, 'more': 20,
             'after': 20, 'before': 20, 'where': 20, 'when': 20, 'every': 20, 'other': 20, 'man': 20, 'tree': 20,
             'bird': 20, 'cat': 20, 'dog': 20, 'park': 20, 'bank': 20, 'use': 20, 'saw': 20, 'get': 20, 'see': 20,
             'say': 20, 'way': 20, 'day': 20, 'can': 20, 'how': 20, 'now': 20, 'out': 20, 'new': 20, 'who': 20,
             'has': 20, 'did': 20, 'our': 20, 'an': 15, 'at': 15, 'woman': 15, 'boy': 15, 'girl': 15, 'child': 15,
             'people': 15, 'family': 15, 'friend': 15, 'mother': 15, 'father': 15, 'house': 15, 'home': 15, 'room': 15,
             'door': 15, 'car': 15, 'water': 15, 'food': 15, 'place': 15, 'world': 15, 'school': 15, 'year': 15,
             'life': 15, 'hand': 15, 'head': 15, 'name': 15, 'word': 15, 'story': 15, 'black': 15, 'white': 15,
             'red': 15, 'blue': 15, 'green': 15, 'small': 15, 'fast': 15, 'slow': 15, 'hot': 15, 'cold': 15, 'warm': 15,
             'easy': 15, 'hard': 15, 'light': 15, 'dark': 15, 'near': 15, 'far': 15, 'early': 15, 'late': 15,
             'best': 15, 'next': 15, 'same': 15, 'open': 15, 'close': 15, 'under': 15, 'over': 15, 'around': 15,
             'through': 15, 'about': 15, 'against': 15, 'behind': 15, 'john': 25, 'mary': 25, 'james': 25, 'robert': 25,
             'michael': 25, 'william': 25, 'david': 25, 'richard': 25, 'joseph': 25, 'thomas': 25, 'charles': 25,
             'christopher': 25, 'daniel': 25, 'matthew': 25, 'anthony': 25, 'mark': 25, 'donald': 25, 'steven': 25,
             'paul': 25, 'andrew': 25, 'kenneth': 25, 'peter': 25, 'joshua': 25, 'kevin': 25, 'brian': 25, 'george': 25,
             'edward': 25, 'ronald': 25, 'timothy': 25, 'jason': 25, 'jeffrey': 25, 'ryan': 25, 'jacob': 25, 'gary': 25,
             'nicholas': 25, 'eric': 25, 'jonathan': 25, 'stephen': 25, 'larry': 25, 'justin': 25, 'scott': 25,
             'brandon': 25, 'benjamin': 25, 'samuel': 25, 'gregory': 25, 'alexander': 25, 'patrick': 25, 'frank': 25,
             'raymond': 25, 'jack': 25, 'dennis': 25, 'jerry': 25, 'tyler': 25, 'aaron': 25, 'henry': 25, 'douglas': 25,
             'peter': 25, 'jose': 25, 'adam': 25, 'nathan': 25, 'zachary': 25, 'arthur': 25, 'harold': 25, 'ralph': 25,
             'jordan': 25, 'albert': 25, 'wayne': 25, 'eugene': 25, 'louis': 25, 'phillip': 25, 'logan': 25,
             'patricia': 25, 'jennifer': 25, 'linda': 25, 'elizabeth': 25, 'barbara': 25, 'susan': 25, 'jessica': 25,
             'sarah': 25, 'karen': 25, 'nancy': 25, 'lisa': 25, 'betty': 25, 'helen': 25, 'sandra': 25, 'donna': 25,
             'carol': 25, 'ruth': 25, 'sharon': 25, 'michelle': 25, 'laura': 25, 'emily': 25, 'kimberly': 25,
             'deborah': 25, 'dorothy': 25, 'amy': 25, 'angela': 25, 'ashley': 25, 'brenda': 25, 'emma': 25,
             'olivia': 25, 'cynthia': 25, 'marie': 25, 'janet': 25, 'catherine': 25, 'frances': 25, 'christine': 25,
             'samantha': 25, 'debra': 25, 'rachel': 25, 'carolyn': 25, 'janet': 25, 'virginia': 25, 'maria': 25,
             'heather': 25, 'diane': 25, 'julie': 25, 'joyce': 25, 'victoria': 25, 'kelly': 25, 'christina': 25,
             'joan': 25, 'evelyn': 25, 'lauren': 25, 'judith': 25, 'megan': 25, 'cheryl': 25, 'anna': 25,
             'jacqueline': 25, 'martha': 25, 'gloria': 25, 'teresa': 25, 'sara': 25, 'janice': 25, 'marie': 25,
             'julia': 25, 'grace': 25, 'rose': 25, 'theresa': 25, 'beverly': 25, 'denise': 25, 'marilyn': 25,
             'amber': 25, 'danielle': 25, 'abigail': 25, 'brittany': 25, 'alice': 25, 'bob': 25, 'tom': 25, 'jane': 25,
             'sue': 25, 'joe': 25, 'bill': 25, 'mike': 25, 'dave': 25, 'steve': 25, 'jim': 25, 'rob': 25, 'chris': 25,
             'dan': 25, 'matt': 25, 'tony': 25, 'kate': 25, 'ann': 25, 'lucy': 25, 'emma': 25, 'eve': 25, 'max': 25,
             'sam': 25, 'ben': 25, 'nick': 25, 'rex': 25, 'luke': 25, 'noah': 25, 'owen': 25, 'jack': 25, 'leo': 25,
             'ivy': 25, 'zoe': 25, 'may': 25, 'joy': 25, 'hope': 25, 'faith': 25, 'harry': 30, 'hermione': 30,
             'ron': 30, 'dumbledore': 30, 'snape': 30, 'voldemort': 30, 'gandalf': 30, 'frodo': 30, 'aragorn': 30,
             'legolas': 30, 'gimli': 30, 'gollum': 30, 'sherlock': 30, 'watson': 30, 'holmes': 30, 'darcy': 30,
             'elizabeth': 30, 'jane': 30, 'emma': 30, 'gatsby': 30, 'daisy': 30, 'tom': 30, 'nick': 30, 'atticus': 30,
             'scout': 30, 'jem': 30, 'holden': 30, 'phoebe': 30, 'romeo': 30, 'juliet': 30, 'hamlet': 30, 'ophelia': 30,
             'macbeth': 30, 'othello': 30, 'iago': 30, 'desdemona': 30, 'prospero': 30, 'ariel': 30, 'caliban': 30,
             'miranda': 30}

    try:
        with open("wordsmini.txt", 'r') as f:
            for line in f:
                word = line.strip().lower()
                if word and len(word) >= 2 and word not in words:
                    words[word] = len(word)
    except:
        pass

    result = []
    pos = 0

    for i in range(len(text)):
        if pos >= len(text):
            break

        best_word = ""
        best_score = 0

        for length in range(1, 21):
            if pos + length > len(text):
                continue

            segment = text[pos:pos + length].lower()

            for word in words:
                if len(word) != len(segment):
                    continue

                match = True
                if '*' in segment:
                    for j in range(len(segment)):
                        if segment[j] != '*' and segment[j] != word[j]:
                            match = False
                            break
                else:
                    if sorted(segment) != sorted(word):
                        match = False

                if match:
                    score = words[word] * len(word)
                    if '*' in segment:
                        score = score * 2
                    if score > best_score:
                        best_score = score
                        best_word = word

        if best_word:
            result.append(best_word)
            pos = pos + len(best_word)
        else:
            pos = pos + 1

    return ' '.join(result)


def main():
    with open("input.txt", 'r') as f:
        text = f.read().strip()

    output = decrypt(text)

    with open("output.txt", 'w') as f:
        f.write(output)


if __name__ == "__main__":
    main()