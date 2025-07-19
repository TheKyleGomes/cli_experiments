# Emoji Mood Converter v1.0

import string

# Line Formatting
line_size = 100

def print_line(char = "-"):
    print(char * line_size)

# Print Header
print_line()
print("")
print(" "*29 + "😃 🔄 🎭  EMOJI WORD CONVERTER  😃 🔄 🎭")
print("")
print_line()

# Tool Tips
print("")
print(" "*22 + "📑   Here are some of the words this tool supports:   📑")
print("      Love  ●  Pizza  ●  Happy  ●  Sad  ●  Angry  ●  Cat  ●  Dog  ●  Fire  ●  Star  ●  Party")
print("")
print_line()

# Input
print("")
sentence = input(" "*27 + "🤔   What would you like me to translate?   🤔" + "\n"
"                           ➡️    ").lower()
print("")
print_line()

# Output Logic
output = ""

emoji_groups = {
# Emotions
"😂 ": ["funny", "laugh", "lol", "lmao", "rofl", "hilarious", "giggle", "giggles", "haha", "hahaha", "ahaha", "aha", "hehe"],
"😀 ": ["happy", "happiness", "happiest", "happier", "joy", "joyful", "glad"],
"🤯 ": ["mindblown", "shock", "crazy", "unbelievable", "wow", "insane"],
"🤔 ": ["thinking", "think", "hmm", "maybe", "perhaps", "consider", "ponder", "wonder", "pondering", "wondering"],
"😴 ": ["tired", "sleepy", "sleep", "nap", "rest", "zzz", "zzzzz", "exhausted", "yawn"],
"😎 ": ["cool", "chill", "awesome", "rad", "swagger", "boss", "stylish"],
"😢 ": ["sad", "cry", "tears", "upset", "sorrow", "depressed", "hurt", "depression"],
"😡 ": ["angry", "mad", "furious", "rage", "raging", "grr", "annoyed", "pissed"],
"🤢 ": ["gross", "ew", "eww", "disgust", "disgusting", "nasty", "vomit", "vomiting", "sick", "nauseous", "nausea"],
"💀 ": ["dead", "rip", "death", "skull", "dying", "lifeless", "gone"],
"👽 ": ["alien", "aliens", "ufo", "ufos", "extraterrestrial", "weird", "weirdo", "space", "galaxy", "galaxies"],
# People
"👩 ": ["woman", "women", "girl", "girls", "female", "females", "lady", "ladies", "she", "her", "hers"],
"👨 ": ["man", "men", "boy", "boys", "male", "males", "gentleman", "gentlemen", "he", "him", "his"],
"👩👨👩 ": ["people", "they", "them"],
"👶 ": ["baby", "babies", "toddler", "toddlers"],
"ℹ ": ["i", "im", "me", "myself"],
"& ": ["and", "together"],
# Food
"🍽 ": ["food"],
"🍕 ": ["pizza", "slice", "pepperoni", "pizzas", "margarita", "dominos"],
"🧀 ": ["cheese", "cheesy"],
"🍔 ": ["burger", "burgers", "hamburger", "hamburgers", "beef", "cheeseburger", "bun"],
"🍟 ": ["fries", "chips", "frenchfries", "mcds", "mcdonalds"],
"🍦 ": ["icecream", "icecreams", "dessert", "desserts", "sweet", "sweets", "cone"],
"🍎 ": ["apple", "apples", "fruit"],
"🍌 ": ["banana", "bananas"],
"🍇 ": ["grape", "grapes"],
"🍓 ": ["strawberry", "strawberries"],
"🍉 ": ["watermelon"],
"🌮 ": ["taco", "tacos"],
"🍗 ": ["chicken", "drumstick"],
"🍣 ": ["sushi"],
"🥚 ": ["egg", "eggs"],
# Animals
"🐱 ": ["cat", "cats", "kitty", "kitten", "kittens", "meow", "feline"],
"🐶 ": ["dog", "dogs", "puppy", "puppies", "hound", "hounds", "woof", "bark", "pup", "doggo"],
"🐰 ": ["rabbit", "bunny"],
"🦊 ": ["fox", "foxes"],
"🐻 ": ["bear", "bears"],
"🐼 ": ["panda", "pandas"],
"🦁 ": ["lion", "lions"],
"🐯 ": ["tiger", "tigers"],
"🐵 ": ["monkey", "monkeys"],
"🦄 ": ["unicorn", "unicorns"],
"🐸 ": ["frog", "frogs"],
# Locations
"🌍 ": ["earth", "world", "planet", "globe"],
"🏝️ ": ["island", "islands", "holiday"],
"🏔️ ": ["mountain", "mountains"],
"🏜️ ": ["desert", "deserts"],
"🏖️ ": ["beach", "beaches"],
# Transport
"🚗 ": ["car", "cars", "drive", "driving", "vehicle", "vehicles"],
"🚌 ": ["bus", "buses"],
"🚲 ": ["bike", "bikes", "bicycle", "bicycles", "cycle", "cycling"],
"✈️ ": ["plane", "planes", "airplane", "airplanes", "flight", "flights"],
"🚢 ": ["ship", "ships", "boat", "boats", "cruise", "cruises"],
"🚆 ": ["train", "trains"],
# Nature
"🌞 ": ["sun", "sunny", "sunshine", "summer"],
"🌧️ ": ["rain", "rainy", "raining", "gloomy"],
"❄️ ": ["snow", "snowy", "snowing", "winter"],
"🌪️ ": ["storm", "storms", "tornado", "tornadoes", "cyclone", "cyclones"],
"🌈 ": ["rainbow", "rainbows", "pride", "lgbt", "lgbtq", "lgbtqa"],
"🍂 ": ["autumn"],
"🌲 ": ["tree", "trees", "forest", "forests", "wild", "wilderness"],
"🌸 ": ["flower", "flowers", "blossom", "spring"],
"🧊 ": ["ice", "cold", "freeze", "freezing"],
# Professions
"👩‍⚕️ ": ["nurse", "nurses", "doctor", "doctors", "medic", "medics"],
"👨‍🍳 ": ["chef", "chefs", "cook", "cooks", "cooking"],
"👩‍🏫 ": ["teacher", "teachers", "teaching", "professor", "professors", "educator", "educators"],
"👨‍💻 ": ["programmer", "programmers", "coder", "coders", "dev", "devs", "developer", "developers", "hacker"],
"👮 ": ["police", "policeman", "cop", "cops", "officer", "officers"],
"🧑‍🚀 ": ["astronaut", "astronauts", "space", "rocket"],
# Actions
"💃 ": ["dance", "dancing", "disco", "groove", "salsa", "tango"],
"🚶‍♂️ ": ["walk", "walking", "stroll", "strolling", "hike", "hiking"],
"🏃‍♀️ ": ["run", "running", "jog", "jogging", "sprint", "sprinting", "race", "racing", "rush", "rushing", "hurry"],
"🤸‍♂️ ": ["jump", "jumping", "hop", "hopping", "leap", "leaping", "bounce", "bouncing", "cartwheel", "cartwheels"],
"🤾‍♀️ ": ["throw", "throwing", "toss", "tossing"],
"🕺 ": ["festivity", "festive", "boogie"],
"✈️ ": ["fly", "flying", "soar", "soaring", "glide", "gliding", "hover", "hovering"],
"🧗‍♂️ ": ["climb", "climbing", "ascend", "ascending"],
"🚴‍♂️ ": ["bike", "biking", "cycle", "cycling", "pedal", "pedaling", "ride", "riding"],
"🏊‍♂️ ": ["swim", "swimming", "dive", "diving"],
# Others
"❤️ ": ["love", "loves", "heart", "hearts", "adore", "adores", "passion", "crush", "romance", "romantic", "affection"],
"🔥 ": ["fire", "fires", "burn", "burning", "lit", "hot", "heat", "flame", "blaze"],
"⭐ ": ["star", "shine", "sparkle", "stars"],
"🎉 ": ["party", "parties", "partying", "celebrate", "celebrating", "celebration", "fun", "congrats", "congratulations"],
"💩 ": ["poop", "crap", "shit", "dookie", "stink", "bad", "terrible", "horrible"],
"💡 ": ["idea", "invent", "inventing", "inventor"],
"📚 ": ["study", "studying", "book", "books", "read", "reading", "learn", "learning", "school", "schools", "college", "colleges", "homework"],
"🏠 ": ["home", "homes", "house", "houses", "apartment", "apartments", "living", "residence", "shelter"],
"🚀 ": ["rocket", "rockets", "launch", "launching", "moon", "moons", "mission", "missions", "fly"],
"🧠 ": ["smart", "smarts", "brain", "brains", "think", "thinking", "genius", "solution", "solutions", "intelligent"],
"➕ ": ["plus", "more", "add"],
"➖ ": ["minus", "less", "remove"],
"☮ ": ["peace"],
"🛑 ": ["stop"],
"💥 ": ["boom", "booms", "pow", "explosion", "explosions"],
"❓ ": ["question", "questions"],
"💨 ": ["fart", "farts", "farting"],
"💦 ": ["wet", "moist"],
"🔇 ": ["mute"],
"☢ ": ["radioactive"],
"⚠ ": ["danger", "dangerous", "caution", "cautious"],
"♻ ": ["recycle", "recycling"],
"🌐 ": ["web", "internet", "www"],
"▶ ": ["play"],
"⏸ ": ["pause"],
"🔴 ": ["red"],
"🟠 ": ["orange"],
"🟡 ": ["yellow"],
"🟢 ": ["lime", "green"],
"🔵 ": ["blue"],
"🟣 ": ["purple"],
"🟤 ": ["brown"],
"⚫ ": ["black"],
"⚪ ": ["white"]
}

emoji_dict = {}
for emoji, words in emoji_groups.items():
    for word in words:
        emoji_dict[word] = emoji

for word in sentence.split():
    cleaned = word.strip(string.punctuation)
    output += emoji_dict.get(cleaned, cleaned) + " "

# Print Output
print(" "*27 + "📨   Translated:   " + output.strip())
print_line()

# Print Footer
print(" "*25 + "❤️️   Thanks for using this tool by TheKyleGomes   ❤️")
print_line()