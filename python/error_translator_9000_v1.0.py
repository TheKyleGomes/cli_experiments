# Error Translator 9000 v1.0

import string

# Line Formatting
line_size = 100

def print_line(char = "-"):
    print(char * line_size)

# Print Header
print_line()
print("")
print("     ➜  ERROR TRANSLATOR 9000  🧨 💥 ❌")
print("")
print_line()

# Input
print("")
sentence = input("     ➜  Please input the 💥 ERROR 💥:  ").lower()
print("")
print_line()

# Output Logic
output = ""

error_groups = {
# Syntax / Parsing Errors
"SyntaxError": ["You broke the rules of Python grammar. 🧠 Maybe you forgot a colon, quote or bracket."],
"IndentationError":["Your code's all over the place! 📏 Python is picky about indentation."],
"TabError":["Tabs and spaces are fighting again. 😤 Pick one and stick with it."],
"EOFError":["You just... stopped talking mid-sentence 🤯 Maybe missing a ""."],
# Name & Attribute Errors
"NameError": ["Who's that? Never heard of it. 😱 You used a variable that doesn't exist."],
"AttributeError":["That thing doesn't do that. 🧱 You're calling a method, property or similar that isn't there."],
"UnboundLocalError":["You used a local variable before giving it a value. 🚨"],
# Type & Value Errors
"TypeError": ["You can't do that with those. 🍌 + 📦 You're adding a number to a string or similar. OR... 🤔 You used a function/class the wrong way."],
"ValueError": ["That value makes no sense here. 😕 Like an int containing a string or similar."],
"IndexError": ["That index doesn't exist. 📦 You went too far in a list/array."],
"KeyError": ["That key's not in the dictionary. 🔑"],
"OverflowError": ["That number is WAY too big. 🌋"],
"ZeroDivisionError":["You tried to divide by zero. Are you ok? 🤯"],
# Import & Module Errors
"ImportError":["I can't find that module. 🧳 You tried to import something that doesn't exist."],
"ModuleNotFoundError":["That module straight up doesn't exist. ❌"],
"ImportWarning":["You imported something sketchy. ❗"],
# Input/Output Errors
"FileNotFoundError":["There's no file with that name. 📁"],
"IsADirectoryError":["You tried to open a folder like it's a file. 📁"],
"NotADirectoryError":["That's not a folder. Don't treat it like one. 🙅‍♂️"],
"PermissionError":["You're not allowed to do that. 🛑 Probably need admin or file is locked."],
"IOError":["Something went wrong with reading/writing. 📡 Very generic."],
# Math & Logic Error
"ArithmeticError":[""],
"FloatingPointError":[""],
"MemoryError":[""],
"RecursionError":[""],
# Permission & Access Errors
"PermissionError":[""],
"BlockingIOError":[""],
"TimeoutError":[""],
# Assertion & Runtime Checks
"AssertionError":[""],
"RuntimeError":[""],
"NotImplementedError":[""],
"StopIteration":[""],
"StopAsyncIteration":[""],
# OOP & Advanced Errors
"LookupError":[""],
"NameError":[""],
"EnvironmentError":[""],
# Network / OS / System Errors
"OSError":["Something failed at the OS level. 💻 Broad category."],
"ConnectionError":["Something went wrong with the network. 📡"],
"BrokenPipeError":["A connection was cut unexpectedly. 🔌"],
"ConnectionAbortedError":["The connection was killed before it was ready. ❌"],
"ConnectionRefusedError":["The other side said no. 🙅‍♂️"],
"ConnectionResetError":["They hung up on you. 📞💔"],
# Other Rare Ones
"BufferError":["There was a problem with a memory buffer. 💾"],
"SystemExit":["sys.exit() was called. This is not a crash, just a quit. 😊"],
"KeyboardInterrupt":["Ctrl+C! The user cancelled it. 💻"],
"GeneratorExit":["A generator got closed too early. ❌"]
}