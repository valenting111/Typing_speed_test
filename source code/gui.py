from tkinter import *
import time


class CustomGui():
    def __init__(self, size_window, fg_color, bg_color, results_color, generation_func):
        self.my_window = Tk()
        self.my_window.title("Typing skills")
        self.my_window.geometry(size_window)
        self.my_window.bind('<Return>', self.return_cmd)
        self.my_window['bg'] = bg_color

        self.label1 = Label(self.my_window, text="\n Let's test your typing speed \n",
                            bg=bg_color, fg=fg_color, font="none 20 bold", anchor=CENTER)

        self.label_cd = Label(self.my_window, bg=bg_color, fg=fg_color, font="none 20 bold")

        self.button1 = Button(self.my_window,
                              {"text": "New sentence", "command": lambda: [self.countdown(), self.clear_entry()],
                               "bg": bg_color, "fg": fg_color, "bd": 4})
        self.button1.config(width=25, height=2, font="none 16 bold")

        self.user_entry = Entry(self.my_window, width=200, justify='center', font="none 14 bold")
        self.user_entry.bind('<Key>', self.type_text_cmd)

        self.label_random_sent = Label(self.my_window, text='Random sentence will appear here',
                                       justify='center', height=2, width=200, bg='white', font="none 16 bold")

        self.label_results = Label(self.my_window, text='', bg=bg_color, fg=results_color,
                                   justify='left', height=2, width=100, font="none 20 bold")

        self.first_key = True
        self.start_time = 0
        self.elapsed_time = 0
        self.generation_func = generation_func
        self.random_sent = self.generation_func()
        self.pack_widgets()

    def pack_widgets(self):
        self.label1.pack()
        self.button1.pack()
        self.label_cd.pack()
        self.label_random_sent.pack()
        self.user_entry.pack()
        self.label_results.pack()

    def compare_sentences(self, sent1, sent2, elapsed_time):
        split1 = sent1.split()
        split2 = sent2.split()
        n_correct = 0
        for idx, word in enumerate(split1):
            if idx < len(split2):
                if word.lower() == split2[idx].lower():
                    n_correct += 1
        try:
            accuracy = n_correct / len(split1)
            wpm = int(60 * len(split2) / elapsed_time)
        except ZeroDivisionError:
            print('Tried to divide by zero for accuracy or wpm computation')
            accuracy = 0
            wpm = 0
        return accuracy, wpm

    # the binding requires a hidden argument event
    def return_cmd(self, event):
        self.elapsed_time = time.time() - self.start_time
        user_sent = self.user_entry.get()
        accuracy, wpm = self.compare_sentences(self.random_sent, user_sent, self.elapsed_time)

        self.label_results['text'] = f'Results: Accuracy: {accuracy * 100}% Time elapsed: {self.elapsed_time}s. Wpm: {wpm} '
        self.first_key = True
        self.random_sent = self.generation_func()

    def type_text_cmd(self, event):
        if self.first_key:
            self.start_time = time.time()
            self.first_key = False

    def clear_entry(self):
        self.user_entry.delete(0, "end")
        self.label_results['text'] = ''
        self.label_random_sent['text'] = ''

    def countdown(self, count=3):

        self.label_cd['text'] = count

        if count > 0:
            # call countdown again after 1000ms (1s)
            self.my_window.after(1000, self.countdown, count - 1)
        else:
            self.label_cd['text'] = 'GO!'
            self.label_random_sent['text'] = self.random_sent

    def show(self):
        self.my_window.mainloop()

