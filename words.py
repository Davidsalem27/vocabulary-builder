import tkinter as tk
import random
import time
import copy
NUM_WORDS_QUIZ=5
##easy words=level>7, mid words=level>4, hard words=level>0
class Main_menu_GUI():
    def __init__(self):
        self.master=tk.Tk()
        self.master.title('Main menu')
        self.master.geometry('800x600')
        topMenu = tk.Menu(self.master)
        self.master.config(menu=topMenu)
        self.main_frame=tk.Frame(self.master)
        self.main_frame.pack()
        self.add_word_button=tk.Button(self.main_frame,text='Add word menu',
                                       command=self.add_word_menu)
        self.add_word_button.pack()
        self.quiz_button=tk.Button(self.main_frame,text='Turn on Quiz',
                                   command=self.quiz_starter)
        self.quiz_button.pack()
        self.display_button=tk.Button(self.main_frame,text='Display all words',
                                      command=self.display_words)
        self.display_button.pack()
        sub_menu=tk.Menu(topMenu)
        topMenu.add_cascade(menu=sub_menu,label='what')
        sub_menu.add_command(label='Add Word',command=self.add_word_menu)
        sub_menu.add_command(label='Quiz', command=self.quiz_starter)

        self.master.mainloop()

    def add_word_menu(self):
        x=Add_Word('')
        add_word_GUI(x)
    def quiz_starter(self):
        self.quiz=Quiz()
    def display_words(self):
        x=Displaywords()
        DisplayGui(x)
class main_menu_LOGIC():
    def __init__(self):
        pass

class Add_Word():
    def __init__(self,name):
        self.name = name
    def adding_new_word(self,word_name,word_meaning):
        """
        function thats adds new words to text file
        :param word_name:
        :param word_meaning:
        :return:
        """
        f= open("test.txt","a+")
        f.write('*start* '+ word_name +' *level*'+ '0  Meaning=' + word_meaning + '*end*')
        f.write('\n\r')
        f.close()

class add_word_GUI():
    def __init__(self,name):
        self.name=name
        self.main_frame = tk.Toplevel()
        self.main_frame.geometry('800x600')
        self.word_name=tk.Entry(self.main_frame)
        self.word_meaning=tk.Text(self.main_frame)
        self.add_word_button=tk.Button(self.main_frame,text='Add Word',font=30,command=self.add_word)
        self.headline=tk.Label(self.main_frame,text='Add a new word to the Database',font=40)
        self.packing_func()
        self.main_frame.mainloop()
    def packing_func(self):
        self.headline.pack()
        self.word_name.pack()
        self.word_meaning.pack()
        self.add_word_button.pack()
    def add_word(self):
        word_name=self.word_name.get()
        word_meaning=self.word_meaning.get("1.0", tk.END[:-1])
        if word_name=='' or word_meaning=='':
            return
        self.name.adding_new_word(word_name,word_meaning)
        self.word_name.delete(0, tk.END)
        self.word_meaning.delete("1.0", tk.END)


class Displaywords():
    def __init__(self):
        self.list_of_words=[]
        self.text_reader()
    def text_reader(self):
        """
        function that loads all pre existing words from text file
        """
        f = open("test.txt", "r+")
        text = f.read()
        total = text.count('*start*')
        ind_word, ind_meaning,ind_level, counter = 0, 0, 0,0
        while counter < total:
            meaning,word = '',''
            if counter == 0:
                ind_word = text.index('*start*', ind_word)
                ind_level= text.index('*level*',ind_level)
            else:
                ind_word = text.index('*start*', ind_word + 1)
                ind_level = text.index('*level*', ind_level+1)
            word = text[ind_word + 7:ind_level - 1]
            self.list_of_words.append(word)
            counter += 1
        f.close()
class DisplayGui():
    def __init__(self,log):
        self.main_frame = tk.Toplevel()
        self.main_frame.geometry('800x600')
        self.list_of_words=log.list_of_words
        self.new_displey=''
        self.display_change()
        self.main_label=tk.Label(self.main_frame,text=self.new_displey,font=30)
        self.main_label.pack()
    def display_change(self):
        for i in range(len(self.list_of_words)):
            self.new_displey+=str(i+1)+ '.' + self.list_of_words[i] + '\n'


class Quiz():
    def __init__(self):
        self.counter=1
        self.dict={}
        self.list_words=[]
        self.list_easy_words=[]
        self.list_mid_words = []
        self.list_hard_words = []
        self.text_reader()
        self.group_divider()
        self.main_loop()

    def group_divider(self):
        for i in self.list_words:
            if i.level>=8:
                self.list_easy_words.append(i)
            if i.level>=5:
                self.list_mid_words.append(i)
            else:
                self.list_hard_words.append(i)

    def main_loop(self):
        counter=1
        origin=[]
        while True:
            if counter==4:
                counter=1
            if counter==3:
                origin=self.list_words
            if counter==2:
                origin=self.list_hard_words+self.list_mid_words
            if counter==1:
                origin=self.list_hard_words
            quizzing_words = self.randomizer(origin)
            self.quiz = quiz_GUI(quizzing_words)
            time.sleep(72000)
    def randomizer(self,origin):
        counter=0
        quizzing_words=[]
        names=[]
        while counter<NUM_WORDS_QUIZ:
            pos_word=random.choice(origin)
            if pos_word not in quizzing_words:
                quizzing_words.append(pos_word)
                names.append(pos_word.name)
                counter+=1
        return quizzing_words

    def text_reader(self):
        """
        function that loads all pre existing words from text file
        """
        f = open("test.txt", "r+")
        text = f.read()
        total = text.count('*start*')
        dict = {}
        ind_word, ind_meaning,ind_level, counter = 0, 0, 0,0
        while counter < total:
            meaning,word = '',''
            if counter == 0:
                ind_word = text.index('*start*', ind_word)
                ind_meaning = text.index('Meaning=', ind_meaning)
                ind_level= text.index('*level*',ind_level)
            else:
                ind_word = text.index('*start*', ind_word + 1)
                ind_meaning = text.index('Meaning=', ind_meaning + 1)
                ind_level = text.index('*level*', ind_level+1)
            word = text[ind_word + 7:ind_level - 1]
            meaning = text[ind_meaning + 8:text.index('*end*', ind_meaning)]
            level=text[ind_level+7:ind_level+8]
            if word not in self.dict:
                self.dict[word.strip()] = meaning.strip() #adds to the dict the name and meaning
                self.list_words.append(Word(word.strip(),meaning.strip(),int(level))) #creating the objects
            counter += 1
        f.close()
    def level_updater(self,word):
        f = open("test.txt", "w+")
        text = f.read()
        word_ind=text.index(word.name)
        ind_level=text.index('*level*',word_ind)
        word.level=text[ind_level + 7:ind_level + 8]
        f.close()




class quiz_GUI():
    def __init__(self,quizzing_words):
        self.main_frame= tk.Toplevel()
        self.main_frame.geometry('800x600')
        self.top_frame = tk.Frame(self.main_frame)
        self.bottom_frame = tk.Frame(self.main_frame)
        self.word_on_screen=tk.StringVar()
        self.word_frame = tk.Label(self.top_frame, textvariable=self.word_on_screen,font=60)
        self.reveal_button = tk.Button(self.main_frame, text='Reveal')
        self.upper_text = tk.Label(self.top_frame, text='What is?',font=30)
        self.frame_num=tk.StringVar()
        self.num_page=0
        self.words = quizzing_words
        self.frame_num.set(str(self.num_page+1)+"/5")
        self.frame_num_label=tk.Label(self.bottom_frame,textvariable=self.frame_num)
        self.previous_button=tk.Button(self.bottom_frame,text='Previous')
        self.next_button = tk.Button(self.bottom_frame, text='Next', command=self.next_page)
        self.previous_button = tk.Button(self.bottom_frame, text='Previous', command=self.prev_page)
        self.reveal_button = tk.Button(self.main_frame, text='Reveal', command=self.reveal_page)
        self.word_on_screen.set(self.words[self.num_page].name)

        self.make_main_quiz()
        self.main_frame.mainloop()


    def make_main_quiz(self):
        self.top_frame.pack()
        self.word_frame.pack()
        self.upper_text.pack()

        self.bottom_frame.pack()
        self.next_button.pack()
        self.previous_button.pack()
        self.reveal_button.pack()
        self.frame_num_label.pack()
    def next_page(self):
        if self.num_page<len(self.words)-1:
            self.num_page += 1
            print(self.words[self.num_page].name)
            self.word_on_screen.set(self.words[self.num_page].name)
            self.frame_num.set(str(self.num_page + 1) + "/5")

    def prev_page(self):
        if self.num_page !=0:
            self.num_page -= 1
            self.word_on_screen.set(self.words[self.num_page].name)
            self.frame_num.set(str(self.num_page+1) + "/5")

    def reveal_page(self):
        self.new_window = tk.Toplevel(self.main_frame)
        self.new_window.title("New Window")
        self.new_window.title(self.words[self.num_page].name)
        self.new_window.geometry("600x400")
        tk.Label(self.new_window,
              text=self.words[self.num_page].meaning,font=50).pack()
        yes_button=tk.Button(self.new_window,text='right',command=self.up_level)
        neutral_button = tk.Button(self.new_window,text='familiar',command=self.new_window.destroy)
        no_button = tk.Button(self.new_window,text='no idea',command=self.down_level)
        yes_button.pack()
        neutral_button.pack()
        no_button.pack()
    def up_level(self):
        self.new_window.destroy()
        self.words[self.num_page].set_level(1)
        self.words[self.num_page].level_updater(1)

    def down_level(self):
        self.new_window.destroy()
        self.words[self.num_page].set_level(-1)
        self.words[self.num_page].level_updater(-1)
class Word():
    def __init__(self,name,meaning,level):
        self.name=name
        self.meaning=meaning
        self.level=level
    def get_meaning(self):
        return self.meaning
    def set_meaning(self,new_meaning):
        self.meaning=new_meaning
    def get_level(self):
        return self.level
    def set_level(self,new_level):
        self.level=new_level+self.level

    def level_updater(self,change):
        f = open("test.txt", "r+")
        old_text = f.read()
        word_ind=old_text.index(self.name)
        ind_level=old_text.index('*level*',word_ind)
        new_text = copy.deepcopy(old_text)
        f.close()
        g = open("test.txt", "w+")
        new_text = new_text[:ind_level + 7] + str(self.level + change) + new_text[ind_level + 8:]
        g.write(new_text)
        g.close()











if __name__=='__main__':
    main1=Main_menu_GUI()



