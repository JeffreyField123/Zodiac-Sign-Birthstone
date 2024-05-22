from flask import Flask, render_template, request

app = Flask(__name__)


def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"


def get_birthstone(month):
    birthstones = {
        1: ("Garnet", "garnet.jpg",
            "Garnet is known for its deep red color and is often associated with vitality, energy, and protection. Historically, it was believed to protect its wearer from nightmares and provide guidance in the dark. Garnet symbolizes peace, prosperity, and good health, and is said to bring about a sense of calm and stability."),
        2: ("Amethyst", "amethyst.jpg",
            "Amethyst is a beautiful purple stone that has been cherished for centuries. It is known for its calming properties and is believed to help the mind and emotions. Amethyst promotes calm, balance, and peace, and is often used to aid with insomnia and anxiety. It is also associated with clarity and sobriety."),
        3: ("Aquamarine", "aquamarine.jpg",
            "Aquamarine, with its serene blue color, is reminiscent of the sea. It is known for its soothing and calming properties, making it a popular stone for meditation. Aquamarine is believed to provide mental clarity and help with communication. It symbolizes tranquility, harmony, and emotional balance."),
        4: ("Diamond", "diamond.jpg",
            "Diamond is renowned for its brilliance and strength. It represents love, strength, and invincibility. Historically, diamonds were believed to be fragments of stars and were used to ward off evil. They symbolize purity and eternal love, making them a popular choice for engagement rings."),
        5: ("Emerald", "emerald.jpg",
            "Emerald is a vibrant green gemstone that has been associated with fertility, rebirth, and love. It is believed to enhance intuition and bring truth to the wearer. Emeralds have been cherished by royalty and are thought to bring prosperity and growth. They also symbolize balance, harmony, and patience."),
        6: ("Pearl", "pearl.jpg",
            "Pearls are unique as they are created by living organisms in the sea. They symbolize purity, humility, and innocence. Pearls are often associated with the moon and have been used for centuries in jewelry. They are believed to bring emotional balance and calm to the wearer, and are a symbol of wisdom gained through experience."),
        7: ("Ruby", "ruby.jpg",
            "Ruby is a stunning red gemstone that represents love, passion, and energy. It is considered one of the most powerful gems in the universe and is often associated with the sun. Rubies are believed to enhance vitality and bring about a sense of power and confidence. They also symbolize protection and prosperity."),
        8: ("Peridot", "peridot.jpg",
            "Peridot is a vibrant green stone that is known for its protective and healing powers. It is believed to ward off negative energy and bring about a sense of peace and well-being. Peridot symbolizes strength and is often associated with renewal and growth. It is also thought to enhance creativity and improve relationships."),
        9: ("Sapphire", "sapphire.jpg",
            "Sapphire is a beautiful blue gemstone that symbolizes wisdom, virtue, and good fortune. It is believed to bring spiritual enlightenment and inner peace. Sapphires have been used by royalty for centuries and are thought to protect against negative energies. They also represent loyalty and integrity."),
        10: ("Opal", "opal.jpg",
             "Opal is a unique gemstone that displays a play of colors, known as opalescence. It is associated with creativity and inspiration. Opal is believed to enhance imagination and bring about a sense of originality and innovation. It also symbolizes emotional expressiveness and is thought to bring good luck."),
        11: ("Topaz", "topaz.jpg",
             "Topaz is known for its various colors, including blue, yellow, and pink. It symbolizes joy, generosity, and abundance. Topaz is believed to bring good fortune and happiness to the wearer. It also enhances clarity of thought and helps with emotional balance. Topaz is often used to promote relaxation and alleviate stress."),
        12: ("Turquoise", "turquoise.jpg",
             "Turquoise is a blue-green stone that represents good fortune, success, and protection. It has been used in amulets and jewelry for centuries and is believed to bring peace and tranquility. Turquoise is also thought to enhance communication and bring about a sense of harmony and balance.")
    }
    return birthstones.get(month, ("Unknown", "unknown.jpg", "No benefits available."))


zodiac_descriptions = {
    "Aries": {
        "description": "Aries is known for being passionate, motivated, and confident leaders. They are enthusiastic, optimistic, and love challenges. Aries is ruled by Mars, which gives them a fiery and competitive nature. They are natural-born leaders, and their energy and courage often inspire those around them.",
        "element": "Fire",
        "image": "aries.jpg"
    },
    "Taurus": {
        "description": "Taurus is reliable, patient, practical, devoted, responsible, and stable. They appreciate the finer things in life and are known for their love of beauty, comfort, and luxury. Taurus is ruled by Venus, which makes them affectionate and sensual. They are dependable and hardworking, making them excellent partners and friends.",
        "element": "Earth",
        "image": "taurus.jpg"
    },
    "Gemini": {
        "description": "Gemini is gentle, affectionate, curious, adaptable, and quick to grasp ideas. They are known for their versatility and ability to communicate effectively. Gemini is ruled by Mercury, the planet of communication, which makes them witty and intellectual. They thrive on social interactions and are always eager to learn new things.",
        "element": "Air",
        "image": "gemini.jpg"
    },
    "Cancer": {
        "description": "Cancer is tenacious, highly imaginative, loyal, emotional, sympathetic, and persuasive. They are deeply intuitive and sentimental, often placing great importance on family and home. Cancer is ruled by the Moon, which gives them a nurturing and protective nature. They are empathetic and can be very loyal friends and partners.",
        "element": "Water",
        "image": "cancer.jpg"
    },
    "Leo": {
        "description": "Leo is creative, passionate, generous, warm-hearted, cheerful, and humorous. They are natural-born leaders and love to be in the spotlight. Leo is ruled by the Sun, which gives them a vibrant and charismatic personality. They are confident and enjoy being admired, often inspiring others with their enthusiasm and zest for life.",
        "element": "Fire",
        "image": "leo.jpg"
    },
    "Virgo": {
        "description": "Virgo is loyal, analytical, kind, hardworking, and practical. They are known for their attention to detail and their desire for order and perfection. Virgo is ruled by Mercury, which makes them intelligent and methodical. They are often very health-conscious and strive for a balanced and healthy lifestyle.",
        "element": "Earth",
        "image": "virgo.jpg"
    },
    "Libra": {
        "description": "Libra is cooperative, diplomatic, gracious, fair-minded, and social. They are known for their sense of balance and justice. Libra is ruled by Venus, which gives them a love for beauty, harmony, and the arts. They are charming and sociable, often seeking to create harmony in their relationships and surroundings.",
        "element": "Air",
        "image": "libra.jpg"
    },
    "Scorpio": {
        "description": "Scorpio is resourceful, brave, passionate, stubborn, and a true friend. They are known for their intensity and depth of emotions. Scorpio is ruled by Pluto and Mars, which give them a powerful and transformative nature. They are often very intuitive and can see beneath the surface, making them excellent problem-solvers.",
        "element": "Water",
        "image": "scorpio.jpg"
    },
    "Sagittarius": {
        "description": "Sagittarius is generous, idealistic, with a great sense of humor. They are known for their love of freedom and adventure. Sagittarius is ruled by Jupiter, the planet of expansion and optimism, which gives them a philosophical and open-minded outlook on life. They are enthusiastic and always ready for new experiences.",
        "element": "Fire",
        "image": "sagittarius.jpg"
    },
    "Capricorn": {
        "description": "Capricorn is responsible, disciplined, has self-control, and is a good manager. They are known for their ambition and determination. Capricorn is ruled by Saturn, which gives them a strong sense of duty and perseverance. They are practical and realistic, often achieving their goals through hard work and dedication.",
        "element": "Earth",
        "image": "capricorn.jpg"
    },
    "Aquarius": {
        "description": "Aquarius is progressive, original, independent, and humanitarian. They are known for their innovative and forward-thinking nature. Aquarius is ruled by Uranus, which gives them a desire for change and rebellion against the status quo. They are often seen as visionaries and are dedicated to making the world a better place.",
        "element": "Air",
        "image": "aquarius.jpg"
    },
    "Pisces": {
        "description": "Pisces is compassionate, artistic, intuitive, gentle, wise, and musical. They are known for their empathy and deep emotional understanding. Pisces is ruled by Neptune, which gives them a dreamy and imaginative nature. They are often very creative and find solace in artistic and spiritual pursuits.",
        "element": "Water",
        "image": "pisces.jpg"
    }
}

celebrities = {
    "Aries": ["Lady Gaga", "Robert Downey Jr.", "Emma Watson"],
    "Taurus": ["Adele", "David Beckham", "Dwayne Johnson"],
    "Gemini": ["Kanye West", "Angelina Jolie", "Johnny Depp"],
    "Cancer": ["Tom Hanks", "Selena Gomez", "Ariana Grande"],
    "Leo": ["Jennifer Lopez", "Chris Hemsworth", "Barack Obama"],
    "Virgo": ["Beyoncé", "Keanu Reeves", "Zendaya"],
    "Libra": ["Will Smith", "Kim Kardashian", "Hugh Jackman"],
    "Scorpio": ["Drake", "Katy Perry", "Ryan Gosling"],
    "Sagittarius": ["Taylor Swift", "Brad Pitt", "Miley Cyrus"],
    "Capricorn": ["Michelle Obama", "Denzel Washington", "Bradley Cooper"],
    "Aquarius": ["Oprah Winfrey", "Harry Styles", "Shakira"],
    "Pisces": ["Rihanna", "Justin Bieber", "Albert Einstein"]
}

compatibility_data = {
    "Aries": {
        "compatible": ["Leo", "Sagittarius", "Gemini", "Aquarius"],
        "incompatible": ["Cancer", "Capricorn", "Libra"],
        "description": {
            "Leo": "Aries and Leo both have a strong zest for life and a mutual respect, making them a fiery match. Their shared enthusiasm and determination create a dynamic and energetic relationship.",
            "Sagittarius": "Aries and Sagittarius share a love for adventure and a carefree attitude. They both value independence and spontaneity, making their relationship lively and exciting.",
            "Gemini": "Aries and Gemini have an energetic and dynamic relationship. Their mutual curiosity and love for new experiences keep things fresh and engaging.",
            "Aquarius": "Aries and Aquarius enjoy a mutual understanding and a shared sense of adventure. Their innovative ideas and willingness to take risks make them a great team.",
            "Cancer": "Aries and Cancer have very different emotional needs, which can lead to misunderstandings. Aries' assertiveness can clash with Cancer's sensitivity, creating tension.",
            "Capricorn": "Aries' impulsive nature clashes with Capricorn's cautious and disciplined approach. Their differing values and priorities can lead to conflicts.",
            "Libra": "Aries and Libra often struggle to balance Aries' assertiveness with Libra's need for harmony. Their opposing personalities can create challenges in finding common ground."
        }
    },
    "Taurus": {
        "compatible": ["Virgo", "Capricorn", "Cancer", "Pisces"],
        "incompatible": ["Leo", "Aquarius", "Sagittarius"],
        "description": {
            "Virgo": "Taurus and Virgo both value stability and practicality, creating a harmonious match. Their mutual dedication to their goals and reliability strengthen their bond.",
            "Capricorn": "Taurus and Capricorn share a grounded and ambitious nature. They both prioritize security and long-term success, making them a strong and supportive partnership.",
            "Cancer": "Taurus and Cancer find comfort and security in each other's company. Their shared love for home and family life creates a nurturing and stable relationship.",
            "Pisces": "Taurus and Pisces balance each other with practicality and sensitivity. Taurus provides stability while Pisces brings creativity and emotional depth to the relationship.",
            "Leo": "Taurus and Leo can clash due to Leo's need for attention and Taurus' stubbornness. Their differing approaches to life can create friction and misunderstandings.",
            "Aquarius": "Taurus and Aquarius have differing values and approaches to life. Taurus' desire for routine conflicts with Aquarius' need for change and innovation.",
            "Sagittarius": "Taurus and Sagittarius may struggle to find common ground due to different lifestyles. Taurus values stability while Sagittarius seeks adventure, leading to potential conflicts."
        }
    },
    "Gemini": {
        "compatible": ["Libra", "Aquarius", "Aries", "Leo"],
        "incompatible": ["Virgo", "Pisces", "Scorpio"],
        "description": {
            "Libra": "Gemini and Libra share intellectual interests and social activities. Their mutual love for communication and exploration makes their relationship stimulating and enjoyable.",
            "Aquarius": "Gemini and Aquarius enjoy lively conversations and innovative ideas. Their shared curiosity and open-mindedness lead to a dynamic and intellectually fulfilling partnership.",
            "Aries": "Gemini and Aries have an energetic and dynamic relationship. Their mutual curiosity and love for new experiences keep things fresh and engaging.",
            "Leo": "Gemini and Leo bring out the best in each other through fun and creativity. Their shared love for socializing and adventure makes their relationship lively and full of joy.",
            "Virgo": "Gemini and Virgo often have different approaches to life and communication. Virgo's practicality can clash with Gemini's spontaneity, leading to potential misunderstandings.",
            "Pisces": "Gemini and Pisces may struggle with emotional and practical differences. Gemini's intellectual approach can conflict with Pisces' emotional depth, creating challenges in understanding each other.",
            "Scorpio": "Gemini and Scorpio often find it challenging to connect deeply. Scorpio's intensity can overwhelm Gemini's more light-hearted nature, leading to potential conflicts."
        }
    },
    "Cancer": {
        "compatible": ["Scorpio", "Pisces", "Taurus", "Virgo"],
        "incompatible": ["Aries", "Libra", "Aquarius"],
        "description": {
            "Scorpio": "Cancer and Scorpio share a deep emotional connection and mutual understanding. Their intuitive and sensitive natures create a strong and supportive bond.",
            "Pisces": "Cancer and Pisces are both sensitive and intuitive, creating a nurturing bond. Their shared empathy and compassion foster a loving and harmonious relationship.",
            "Taurus": "Cancer and Taurus find comfort and security in each other's company. Their mutual love for home and family life creates a stable and nurturing partnership.",
            "Virgo": "Cancer and Virgo complement each other with their caring and practical natures. Virgo's reliability and Cancer's emotional support create a balanced and harmonious relationship.",
            "Aries": "Cancer and Aries have very different emotional needs, which can lead to misunderstandings. Aries' assertiveness can clash with Cancer's sensitivity, creating tension.",
            "Libra": "Cancer and Libra often struggle to balance Cancer's need for security with Libra's social nature. Their differing priorities can create challenges in finding common ground.",
            "Aquarius": "Cancer and Aquarius may find it difficult to understand each other's emotional worlds. Cancer's need for intimacy can clash with Aquarius' desire for independence, leading to potential conflicts."
        }
    },
    "Leo": {
        "compatible": ["Aries", "Sagittarius", "Gemini", "Libra"],
        "incompatible": ["Taurus", "Scorpio", "Capricorn"],
        "description": {
            "Aries": "Leo and Aries both have a strong zest for life and a mutual respect, making them a fiery match. Their shared enthusiasm and determination create a dynamic and energetic relationship.",
            "Sagittarius": "Leo and Sagittarius share a love for adventure and a carefree attitude. Their mutual optimism and desire for fun make their relationship lively and exciting.",
            "Gemini": "Leo and Gemini bring out the best in each other through fun and creativity. Their shared love for socializing and adventure makes their relationship lively and full of joy.",
            "Libra": "Leo and Libra enjoy a social and balanced relationship. Their mutual appreciation for beauty, art, and harmony fosters a loving and supportive partnership.",
            "Taurus": "Leo and Taurus can clash due to Leo's need for attention and Taurus' stubbornness. Their differing approaches to life can create friction and misunderstandings.",
            "Scorpio": "Leo and Scorpio often have power struggles due to their strong personalities. Their intense and passionate natures can lead to conflicts and challenges in their relationship.",
            "Capricorn": "Leo and Capricorn have different approaches to life, which can lead to conflicts. Leo's desire for recognition and Capricorn's focus on discipline may create challenges in finding common ground."
        }
    },
    "Virgo": {
        "compatible": ["Taurus", "Capricorn", "Cancer", "Scorpio"],
        "incompatible": ["Gemini", "Sagittarius", "Leo"],
        "description": {
            "Taurus": "Virgo and Taurus both value stability and practicality, creating a harmonious match. Their mutual dedication to their goals and reliability strengthen their bond.",
            "Capricorn": "Virgo and Capricorn share a grounded and ambitious nature. Their mutual focus on success and discipline creates a strong and supportive partnership.",
            "Cancer": "Virgo and Cancer complement each other with their caring and practical natures. Virgo's reliability and Cancer's emotional support create a balanced and harmonious relationship.",
            "Scorpio": "Virgo and Scorpio have a strong intellectual and emotional connection. Their mutual dedication and determination foster a deep and supportive relationship.",
            "Gemini": "Virgo and Gemini often have different approaches to life and communication. Virgo's practicality can clash with Gemini's spontaneity, leading to potential misunderstandings.",
            "Sagittarius": "Virgo and Sagittarius may struggle to find common ground due to different lifestyles. Virgo values stability while Sagittarius seeks adventure, leading to potential conflicts.",
            "Leo": "Virgo and Leo have different priorities, which can lead to misunderstandings. Virgo's focus on practicality can clash with Leo's desire for recognition, creating potential conflicts."
        }
    },
    "Libra": {
        "compatible": ["Gemini", "Aquarius", "Leo", "Sagittarius"],
        "incompatible": ["Cancer", "Capricorn", "Pisces"],
        "description": {
            "Gemini": "Libra and Gemini share intellectual interests and social activities. Their mutual love for communication and exploration makes their relationship stimulating and enjoyable.",
            "Aquarius": "Libra and Aquarius enjoy lively conversations and innovative ideas. Their shared curiosity and open-mindedness lead to a dynamic and intellectually fulfilling partnership.",
            "Leo": "Libra and Leo enjoy a social and balanced relationship. Their mutual appreciation for beauty, art, and harmony fosters a loving and supportive partnership.",
            "Sagittarius": "Libra and Sagittarius share a love for adventure and exploration. Their mutual optimism and desire for fun make their relationship lively and exciting.",
            "Cancer": "Libra and Cancer often struggle to balance Libra's social nature with Cancer's need for security. Their differing priorities can create challenges in finding common ground.",
            "Capricorn": "Libra and Capricorn have different approaches to life, which can lead to conflicts. Libra's desire for social interaction can clash with Capricorn's focus on discipline.",
            "Pisces": "Libra and Pisces may struggle with practical and emotional differences. Libra's intellectual approach can conflict with Pisces' emotional depth, creating challenges in understanding each other."
        }
    },
    "Scorpio": {
        "compatible": ["Cancer", "Pisces", "Virgo", "Capricorn"],
        "incompatible": ["Leo", "Aquarius", "Gemini"],
        "description": {
            "Cancer": "Scorpio and Cancer share a deep emotional connection and mutual understanding. Their intuitive and sensitive natures create a strong and supportive bond.",
            "Pisces": "Scorpio and Pisces are both sensitive and intuitive, creating a nurturing bond. Their shared empathy and compassion foster a loving and harmonious relationship.",
            "Virgo": "Scorpio and Virgo have a strong intellectual and emotional connection. Their mutual dedication and determination foster a deep and supportive relationship.",
            "Capricorn": "Scorpio and Capricorn share ambition and determination. Their mutual focus on success and discipline creates a strong and supportive partnership.",
            "Leo": "Scorpio and Leo often have power struggles due to their strong personalities. Their intense and passionate natures can lead to conflicts and challenges in their relationship.",
            "Aquarius": "Scorpio and Aquarius have different values and approaches to life. Scorpio's intensity can clash with Aquarius' need for independence, creating potential conflicts.",
            "Gemini": "Scorpio and Gemini often find it challenging to connect deeply. Scorpio's intensity can overwhelm Gemini's more light-hearted nature, leading to potential conflicts."
        }
    },
    "Sagittarius": {
        "compatible": ["Aries", "Leo", "Libra", "Aquarius"],
        "incompatible": ["Virgo", "Pisces", "Cancer"],
        "description": {
            "Aries": "Sagittarius and Aries share a love for adventure and a carefree attitude. Their mutual enthusiasm for new experiences and independence creates a dynamic and exciting relationship.",
            "Leo": "Sagittarius and Leo share a zest for life and a mutual respect. Their mutual optimism and desire for fun make their relationship lively and exciting.",
            "Libra": "Sagittarius and Libra share a love for adventure and exploration. Their mutual curiosity and appreciation for beauty and harmony foster a stimulating and enjoyable relationship.",
            "Aquarius": "Sagittarius and Aquarius enjoy lively conversations and innovative ideas. Their shared curiosity and open-mindedness lead to a dynamic and intellectually fulfilling partnership.",
            "Virgo": "Sagittarius and Virgo may struggle to find common ground due to different lifestyles. Sagittarius' desire for adventure can clash with Virgo's need for stability, creating potential conflicts.",
            "Pisces": "Sagittarius and Pisces often have different priorities and approaches to life. Sagittarius' need for independence can clash with Pisces' emotional depth, leading to potential misunderstandings.",
            "Cancer": "Sagittarius and Cancer often struggle to balance Sagittarius' desire for freedom with Cancer's need for security. Their differing priorities can create challenges in finding common ground."
        }
    },
    "Capricorn": {
        "compatible": ["Taurus", "Virgo", "Scorpio", "Pisces"],
        "incompatible": ["Aries", "Libra", "Leo"],
        "description": {
            "Taurus": "Capricorn and Taurus share a grounded and ambitious nature. Their mutual focus on success and stability creates a strong and supportive partnership.",
            "Virgo": "Capricorn and Virgo share a practical and disciplined approach to life. Their mutual dedication and reliability foster a deep and supportive relationship.",
            "Scorpio": "Capricorn and Scorpio share ambition and determination. Their mutual focus on success and discipline creates a strong and supportive partnership.",
            "Pisces": "Capricorn and Pisces balance each other with practicality and sensitivity. Capricorn provides stability while Pisces brings creativity and emotional depth to the relationship.",
            "Aries": "Capricorn and Aries often have conflicting approaches to life. Capricorn's cautious nature can clash with Aries' impulsive tendencies, creating potential challenges.",
            "Libra": "Capricorn and Libra have different values and approaches to life. Capricorn's focus on discipline can clash with Libra's desire for social interaction, leading to potential misunderstandings.",
            "Leo": "Capricorn and Leo often have different priorities and perspectives. Capricorn's practical approach can conflict with Leo's desire for recognition, creating potential conflicts."
        }
    },
    "Aquarius": {
        "compatible": ["Gemini", "Libra", "Sagittarius", "Aries"],
        "incompatible": ["Taurus", "Scorpio", "Cancer"],
        "description": {
            "Gemini": "Aquarius and Gemini enjoy lively conversations and innovative ideas. Their shared curiosity and open-mindedness lead to a dynamic and intellectually fulfilling partnership.",
            "Libra": "Aquarius and Libra share intellectual interests and social activities. Their mutual love for communication and exploration makes their relationship stimulating and enjoyable.",
            "Sagittarius": "Aquarius and Sagittarius share a love for adventure and exploration. Their mutual curiosity and appreciation for beauty and harmony foster a stimulating and enjoyable relationship.",
            "Aries": "Aquarius and Aries enjoy a mutual understanding and a shared sense of adventure. Their innovative ideas and willingness to take risks make them a great team.",
            "Taurus": "Aquarius and Taurus have differing values and approaches to life. Aquarius' need for change and innovation can clash with Taurus' desire for routine, creating potential conflicts.",
            "Scorpio": "Aquarius and Scorpio have different values and approaches to life. Aquarius' need for independence can clash with Scorpio's intensity, creating potential conflicts.",
            "Cancer": "Aquarius and Cancer may find it difficult to understand each other's emotional worlds. Aquarius' desire for freedom can clash with Cancer's need for security, creating potential conflicts."
        }
    },
    "Pisces": {
        "compatible": ["Cancer", "Scorpio", "Taurus", "Capricorn"],
        "incompatible": ["Gemini", "Sagittarius", "Libra"],
        "description": {
            "Cancer": "Pisces and Cancer are both sensitive and intuitive, creating a nurturing bond. Their shared empathy and compassion foster a loving and harmonious relationship.",
            "Scorpio": "Pisces and Scorpio share a deep emotional connection and mutual understanding. Their intuitive and sensitive natures create a strong and supportive bond.",
            "Taurus": "Pisces and Taurus balance each other with practicality and sensitivity. Taurus provides stability while Pisces brings creativity and emotional depth to the relationship.",
            "Capricorn": "Pisces and Capricorn balance each other with practicality and sensitivity. Capricorn provides stability while Pisces brings creativity and emotional depth to the relationship.",
            "Gemini": "Pisces and Gemini may struggle with practical and emotional differences. Pisces' emotional depth can conflict with Gemini's intellectual approach, creating potential misunderstandings.",
            "Sagittarius": "Pisces and Sagittarius often have different priorities and approaches to life. Pisces' need for emotional connection can clash with Sagittarius' desire for freedom, creating potential conflicts.",
            "Libra": "Pisces and Libra may struggle with practical and emotional differences. Pisces' emotional depth can conflict with Libra's intellectual approach, creating potential misunderstandings."
        }
    }
}


def identify_zodiac_and_birthstone(day, month):
    zodiac_sign = get_zodiac_sign(day, month)
    birthstone, birthstone_image, benefits = get_birthstone(month)
    zodiac_info = zodiac_descriptions.get(zodiac_sign,
                                          {"description": "No description available.", "element": "Unknown",
                                           "image": "unknown.jpg"})
    celebrity_list = celebrities.get(zodiac_sign, ["No famous personalities available."])
    return zodiac_sign, birthstone, birthstone_image, benefits, zodiac_info['description'], zodiac_info['element'], \
        zodiac_info['image'], celebrity_list


def check_compatibility(sign1, sign2):
    compatibility_info = compatibility_data.get(sign1, {})
    compatible_signs = compatibility_info.get("compatible", [])
    incompatible_signs = compatibility_info.get("incompatible", [])
    description = compatibility_info.get("description", {})

    if sign2 in compatible_signs:
        return f"{sign1} and {sign2} are compatible. {description.get(sign2, '')}"
    elif sign2 in incompatible_signs:
        return f"{sign1} and {sign2} are not compatible. {description.get(sign2, '')}"
    else:
        return f"Compatibility information for {sign1} and {sign2} is not available."


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    day1 = int(request.form['day1'])
    month1 = int(request.form['month1'])
    day2 = int(request.form['day2'])
    month2 = int(request.form['month2'])

    zodiac_sign1, birthstone1, birthstone_image1, benefits1, description1, element1, zodiac_image1, celebrities1 = identify_zodiac_and_birthstone(
        day1, month1)
    zodiac_sign2, birthstone2, birthstone_image2, benefits2, description2, element2, zodiac_image2, celebrities2 = identify_zodiac_and_birthstone(
        day2, month2)

    compatibility_result = check_compatibility(zodiac_sign1, zodiac_sign2)

    return render_template('results.html',
                           zodiac_sign1=zodiac_sign1, birthstone1=birthstone1, birthstone_image1=birthstone_image1,
                           benefits1=benefits1, description1=description1, element1=element1,
                           zodiac_image1=zodiac_image1, celebrities1=celebrities1,
                           zodiac_sign2=zodiac_sign2, birthstone2=birthstone2, birthstone_image2=birthstone_image2,
                           benefits2=benefits2, description2=description2, element2=element2,
                           zodiac_image2=zodiac_image2, celebrities2=celebrities2,
                           compatibility_result=compatibility_result)


if __name__ == '__main__':
    app.run(debug=True)
