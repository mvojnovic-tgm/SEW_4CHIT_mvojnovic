import threading
import string
import random

#Die zwei Variablen die am Ende zur augabe dienen
encrypted = []
decrypted = []

#Fuer die dict einmal eine Liste mit gross und klein Buchstaben und Ziffern
all = string.ascii_letters+string.digits
#Und noch einmal doe selbe nur ungeordnet
all_random = ''.join(random.sample(all, len(all)))
#hier als Dict zusammengefasst
all_dict = dict(zip(all, all_random))


class A02_Thread(threading.Thread):

    def __init__(self, chars, s):
        """

        :param chars: eine Liste mit den zuverschluesselten chars
        :param s: ob ver oder entschluesselt werden soll
        """
        threading.Thread.__init__(self)
        self.chars = chars
        self.s = s
    def run(self):
        while True:
            if(self.s=="e"):
                for i in range(len(self.chars)):
                    if (self.chars[i] != " "):
                        self.chars[i] = all_dict[self.chars[i]]
                    encrypted.append(self.chars[i])
            else:
                for i in range(len(self.chars)):
                    if (self.chars[i] != " "):
                        self.chars[i] = list(all_dict.keys())[list(all_dict.values()).index(self.chars[i])].upper()
                    decrypted.append(self.chars[i])
            break

def a02_input():
    """

    :return: returnt den eingegebenen text und die anzahl  der threads
    """
    text = input("What text do you want encrpted: ")
    number = int(input("How much threads to use for the encrypt: "))
    return [text,number]

def a02_check(text,number):
    """

    :param text: der eingegebene text
    :param number: die Anzahl der Threads
    :return: Eine Liste mit Listen mit den chars fuer die einzelnen threads
    """

    number = int(number)

    scale = int(len(text) / number)

    mod = len(text) % number

    list = []

    i = 0
    for i in range(0, number):
        list.append(text[int(i * scale):int(i * scale + scale)])

    if mod != 0:
        list[number - 1] = list[number - 1] + (text[len(text) - mod:len(text)])

    print(list)

    re_list = []

    #bug fixes, dont judg me
    for i in range(len(list)):
        help = []
        for x in range(len(list[i])):
            help.append(list[i][x])
        re_list.append(help)
    return re_list


#print(A02_check(text,number))

def a02_print():
    for item in encrypted:
        print(item, end="")
    print("")
    for item in decrypted:
        print(item, end="")

def a02_main():
    my_input = a02_input()

    text = my_input[0]
    number = my_input[1]

    ftt = a02_check(text, number)
    thread_list = []
    #erzeugt threads fuer die verschluesselung
    for i in range(0,number):
        t = A02_Thread(ftt[i],"e")
        t.start()
        t.join()
        thread_list.append(t)
    #erzeugt threads fuer die entschluesselung
    for i in range(0,number):
        t = A02_Thread(ftt[i],"d")
        t.start()
        t.join()
        thread_list.append(t)
    a02_print()

a02_main()