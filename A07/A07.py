import threading
import queue

class E1(threading.Thread):
    def __init__(self, queue):
        """

        :param queue: Die queue welche auch der verbraucher thread hat
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        number = 2  #eine lokale variable, beginnt ab 2 da 0,1,2 keine Primzahlen sind
        b = True
        while number < 1000:#bIS 10000 sucht das Programm nach Primzahlen
            number += 1 #+1 zaehler
            b = True    #lokale variable zum pruefen ob die zahl eine prmzahl ist
            for i in range(2, number):  #for schleife zum pruefen ob primzahl
                if number % i == 0:
                    b = False   #falls keine primzahl(ohne rest dividierbar)
                    break
            if b == True:   #falls es doch eine primzahl ist bleibt b true und somit wird
                            #hier dann auch queue.put benuzt um den verbraucher zu
                            # benachrichtigen
                self.queue.put(number)
                self.queue.join()
        number = "fertig"   #den verbraucher benachrichtigen das die zaehlung vorbai ist
        self.queue.put(number)  #den verbraucher benachrichtigen das die zaehlung
                                # vorbai ist

class V1(threading.Thread):
    def __init__(self, queue):
        """

        :param queue: Die queue welche auch der verbraucher thread hat
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        tf = open("output.txt", "w")    #oeffnen des text files, "w" ->
                                        # falls keins vorhanden -> neu erstellen
                                        #falsl doch -> ueberschreiben
        while True:
            number = self.queue.get()   #erhaellt die variable aus der queue und
                                        # signalisiert das der erzeuger weitermachen kann
            if(number == "fertig"):     #prueft ob die zaehlung vorbei ist
                break
            print("Primzahl: %d" % number)  #ausgabe in die konsole
            self.queue.task_done()
            tf.write("Primzahl: " + str(number) + "\n") #schreiben in das text file

if __name__ == "__main__":
    queue = queue.Queue()
    t1 = E1(queue)
    t2 = V1(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()