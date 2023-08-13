from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import wget
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from pickle import load
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tkinter as tk


base_model = InceptionV3(weights = 'inception_v3_weights_tf_dim_ordering_tf_kernels.h5')
vgg_model = Model(base_model.input, base_model.layers[-2].output)

def preprocess_img(img_path):
    #inception v3 excepts img in 299*299
    img = load_img(img_path, target_size = (299, 299))
    x = img_to_array(img)
    # Add one more dimension
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    return x

def encode(image):
    image = preprocess_img(image)
    vec = vgg_model.predict(image)
    vec = np.reshape(vec, (vec.shape[1]))
    return vec

pickle_in = open("wordtoix.pkl", "rb")
wordtoix = load(pickle_in)
pickle_in = open("ixtoword.pkl", "rb")
ixtoword = load(pickle_in)
max_length = 74

def greedy_search(pic):
    start = 'startseq'
    for i in range(max_length):
        seq = [wordtoix[word] for word in start.split() if word in wordtoix]
        seq = pad_sequences([seq], maxlen = max_length)
        yhat = model.predict([pic, seq])
        yhat = np.argmax(yhat)
        word = ixtoword[yhat]
        start += ' ' + word
        if word == 'endseq':
            break
    final = start.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final

def beam_search(image, beam_index = 3):
    start = [wordtoix["startseq"]]
    # start_word[0][0] = index of the starting word
    # start_word[0][1] = probability of the word predicted
    start_word = [[start, 0.0]]
    while len(start_word[0][0]) < max_length:
        temp = []
        for s in start_word:
            par_caps = pad_sequences([s[0]], maxlen=max_length)
            e = image
            preds = model.predict([e, np.array(par_caps)])  
            # Getting the top <beam_index>(n) predictions
            word_preds = np.argsort(preds[0])[-beam_index:]
            # creating a new list so as to put them via the model again
            for w in word_preds:
                next_cap, prob = s[0][:], s[1]
                next_cap.append(w)
                prob += preds[0][w]
                temp.append([next_cap, prob])                 
        start_word = temp
        # Sorting according to the probabilities
        start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
        # Getting the top words
        start_word = start_word[-beam_index:]   
    start_word = start_word[-1][0]
    intermediate_caption = [ixtoword[i] for i in start_word]
    final_caption = []
    for i in intermediate_caption:
        if i != 'endseq':
            final_caption.append(i)
        else:
            break
    final_caption = ' '.join(final_caption[1:])
    return final_caption

model = load_model('new-model-1.h5')
top=tk.Tk()
top.geometry('800x600')
top.title('Image Recognizer')
top.configure(background='#CDCDCD')
label2=Label(top,background='#CDCDCD', font=('Helvetica',15))
label1=Label(top,background='#CDCDCD', font=('Helvetica',15))
label=Label(top,background='#CDCDCD', font=('Helvetica',15))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    enc = encode(file_path)
    image = enc.reshape(1, 2048)
    greedy = greedy_search(image)
    print(greedy)
    label.configure(foreground='#000', text= 'Greedy: ' + greedy.title())
    label.pack(side=BOTTOM,expand=True)
    beam_3 = beam_search(image)
    print(beam_3)
    label1.configure(foreground='#011638', text = 'Beam_3: ' + beam_3.title())
    label1.pack(side = BOTTOM, expand = True)
    beam_5 = beam_search(image, 5)
    print(beam_5)
    label2.configure(foreground='#228B22', text = 'Beam_5: ' + beam_5.title())
    label2.pack(side = BOTTOM, expand = True)
    final = greedy+" "+beam_3+" "+beam_5
    print(final)
    finall = set(final.split(' '))
    print(finall)
    rest = ['bikinis','gun','weapon','guns','weapons','knife']
    for i in finall:
        print(i)
        if i in rest:
            tk.messagebox.showinfo("Restricted Content!","This image contains abusive or restricted content and will be taken down")
            break
    
def show_classify_button(file_path):
    classify_b = Button(top,text="Generate",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('Helvetica',10,'bold'))
    classify_b.place(relx=0.79,rely=0.50)
    
def open_file(file_path):
    try:
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/1.75),(top.winfo_height()/1.75)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        show_classify_button(file_path)
    except:
        tk.messagebox.showinfo("Error!","This file is not supported or either you have entered url in wrong format")
    
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        open_file(file_path)
    except:
        tk.messagebox.showinfo("Error!","This file is not supported or either you have entered url in wrong format")

def fetch_image():
    try:
        pic_url = entry.get()
        file_path = wget.download(pic_url)    
        open_file(file_path)
    except:
        tk.messagebox.showinfo("Error!","This file is not supported or either you have entered url in wrong format")
    
entry = tk.Entry(top)
entry.insert(0,"Enter a url")
entry.place(relx=0.1,rely=0.48)

fetch = Button(text="Fetch Image",command=fetch_image,padx=10,pady=5)
fetch.configure(background='#364156', foreground='white',font=('Helvetica',10,'bold'))
fetch.place(relx=0.105,rely=0.52)

upload=Button(top,text="Select Image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('Helvetica',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label2.pack(side = BOTTOM, expand = True)
heading = Label(top, text="Upload an Image",pady=20, font=('Helvetica',22,'bold'))
heading.configure(background='#CDCDCD',foreground='#833AB4')
heading.pack()
top.mainloop()