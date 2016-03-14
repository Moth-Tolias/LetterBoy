import re

print("Text Decorruptor v1 (c) Thomas Tootill, 2014")
print("Be sure to run this in IDLE, so you can copypaste the text in and out.")
TEXT = input("Put the text to be decorrupted here:")
TEXT = re.sub('[̍̎̄̅̿̑̆̐͒͗͑̇̈̊͂̓̈́͊͋͌̃	̂̌͐̀́̋̏̒̓̔̽̉	ͣͤͥͦͧͨ	̴̵̶̡̢̧̨̛ͩͪͫͬͭͮͯ̾͛͆̀́̚̕͘͏̸̷͜͟͢͝͞͠͡҉̖̗̘̙̜̝̞̟̠̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎͓͔͕͖͙͚̣ͅ]', '', TEXT)
print("")
print(TEXT)
print("")
input("Decorruption complete. Press Enter to quit.")
