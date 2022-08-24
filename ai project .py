#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df1 = pd.read_csv("dataset1.csv")
df1.head()


# In[5]:


df1.shape


# In[6]:


df2 = df1


# In[8]:


df2.head()


# In[11]:


dummies1 = pd.get_dummies(df2.apply_sunscreen)


# In[13]:


dummies2 = pd.get_dummies(df2.nutritiest_food)


# In[14]:


dummies3 = pd.get_dummies(df2.beauty_supplements)


# In[15]:


dummies4 = pd.get_dummies(df2.cleansing_before_bed)


# In[16]:


dummies5 = pd.get_dummies(df2.use_moisturizer)


# In[18]:


dummies6 = pd.get_dummies(df2.exercise)


# In[19]:


dummies7 = pd.get_dummies(df2.use_natural_ingrediant_skin_products)


# In[20]:


df3 = pd.concat([df2,dummies1,dummies2,dummies3,dummies4,dummies5,dummies6,dummies7],axis="columns")


# In[21]:


df3.head()


# In[23]:


df4 = df3.drop(["apply_sunscreen","nutritiest_food","beauty_supplements","cleansing_before_bed","use_moisturizer","exercise","use_natural_ingrediant_skin_products"],axis="columns")
df4.head()


# In[24]:


X = df4.drop("chance_of_skin_disease",axis = "columns")
X.head()


# In[25]:


Y = df4.chance_of_skin_disease
Y.head()


# In[26]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state=10)


# In[28]:


from sklearn.linear_model import LinearRegression
lr_clf = LinearRegression()
lr_clf.fit(X_train,Y_train)
lr_clf.score(X_test,Y_test)


# In[34]:


def skin_disease_chance(water,apply_sunscreen,nutritiest_food,beauty_supplements,cleansing_before_bed,sleep,use_moisturizer,exercise,use_natural_ingrediant_skin_products):
    as_index = np.where(X.columns==apply_sunscreen)[0][0]
    nf_index = np.where(X.columns==nutritiest_food)[0][0]
    bs_index = np.where(X.columns==beauty_supplements)[0][0]
    cbb_index = np.where(X.columns==cleansing_before_bed)[0][0]
    um_index = np.where(X.columns==use_moisturizer)[0][0]
    e_index = np.where(X.columns==exercise)[0][0]
    unisp_index = np.where(X.columns==use_natural_ingrediant_skin_products)[0][0]
    
    
    x = np.zeros(len(X.columns))
    x[0] = water
    x[1] = sleep
    if as_index >= 0:
        x[as_index] = 1
        
    if nf_index >= 0:
        x[nf_index] = 1
    
    if bs_index >= 0:
        x[bs_index] = 1
        
    if cbb_index >= 0:
        x[cbb_index] = 1
    
    if um_index >= 0:
        x[um_index] = 1
        
    if e_index >= 0:
        x[e_index] = 1
        
    if unisp_index >= 0:
        x[unisp_index] = 1
        
    return lr_clf.predict([x])[0]


# In[46]:


skin_disease_chance(6,"no","no","yes","yes",3,"yes","no","yes")


# In[52]:


import time
from tqdm import tqdm

def loading():
    for i in tqdm(range(10), desc = 'LOADING PLEASE WAIT '):
        time.sleep(0.5)


def StartingDesign():
    border()
    print('--> This is Dermatologist Consultancy Expert System')
    border()
def cosd():
    print("how much water you drink in a day")
    i1 = int(input())
    print("do you apply sunscreen  yes/no")
    i2 = input()
    print("do you eat nutritiest food  yes/no")
    i3 = input()
    print("do you use beauty supplements  yes/no")
    i4 = input()
    print("do you apply cleansing before bed yes/no")
    i5 = input()
    print("how much you sleep in a day")
    i6 = int(input())
    print("do you use skin moisturizer  yes/no")
    i7 = input()
    print("do you excercise on daily basis  yes/no")
    i8 = input()
    print("do you use natural skin products  yes/no")
    i9 = input()
    print(skin_disease_chance(i1,i2,i3,i4,i5,i6,i7,i8,i9))
    
def question():
    print('Choose one of the following:')
    border()
    print('\n1: List the problems which usually people have these days')
    print('2: view treatment(history based) by input diseases (expert)')
    print('3: Ask dorctor (expert system) for suggestions/consultancy ')
    print('4: To know how much chance you have to get skin disease')
    print('5: Exit\n')
    border()
    choice1 = int(input('Enter your choice: '))
    if (choice1 == 1):
        loading()
        list()
    elif (choice1 == 2):
        loading()
        View_Treatment()
    elif (choice1 == 3):
        loading()
        doctorSelection()
    elif (choice1 == 4):
        cosd()
    elif(choice1==5):
        print()

    else:
        #-----------------------

        print('wrong input. please try again')
        question()

def list():
    print('Here is the list of problems which usually people have these days....')
    print('1: oily skin \n2: dry skin \n3: Acne')
    print('4: rashes \n5: open pores \n6: hives')
    print('7: dark spots\n8: melasma')
    print('----------------------------------------')
    print('----------------------------------------')
    choice2 = input('input any key to continue: ')
    question()
def Simplelist():
    print('Here is the list of problems which usually people have these days....')
    print('1: oily skin \n2: dry skin \n3: Acne')
    print('4: rashes \n5: open pores \n6: hives')
    print('7: dark spots\n8: melasma')
    print('----------------------------------------')
    print('----------------------------------------')

def View_Treatment():
    border()
    print('********View Treatments(history based)********' )
    border()
    print('input any disease name: ')
    treatmentview = input()
    if (treatmentview == '4' or treatmentview == 'i am having rashes' or treatmentview == 'rashes' or treatmentview == 'RASHES'):
       
        Rashes()
        re_confermation_continue_or_not()
    elif(treatmentview == '3' or treatmentview == 'Acne' or treatmentview == 'acne' or treatmentview == 'ACNE'):
        Acne()
        re_confermation_continue_or_not()
    elif(treatmentview == '1' or treatmentview == 'oily skin' or treatmentview == 'Oily Skin' or treatmentview == 'Oily skin' or treatmentview == 'OILY SKIN'):
        Oily_Skin()
        re_confermation_continue_or_not()
    elif(treatmentview == '2' or treatmentview == 'dry skin' or treatmentview == 'Dry Skin' or treatmentview == 'DRY SKIN'):
        Dry_Skin()
        re_confermation_continue_or_not()
    elif(treatmentview == '5' or treatmentview == 'Open Pores' or treatmentview == 'open pores' or treatmentview == 'pores' or treatmentview == 'PORES' ):
        Open_Pores()
        re_confermation_continue_or_not()
    elif(treatmentview == '6' or treatmentview == 'Hives' or treatmentview == 'hives' or treatmentview == 'HIVES'):    
        Hives()
        re_confermation_continue_or_not()
    elif(treatmentview == '7' or treatmentview == 'dark sports' or treatmentview == 'dark spot' or treatmentview == 'Dark Spot' or treatmentview == 'darkspot'):
        Dark_spots()
        re_confermation_continue_or_not()
    elif(treatmentview == '8' or treatmentview == 'melasma' or treatmentview == 'Melasma' or treatmentview == 'MELASMA' or treatmentview == 'milasma'):
        Melasma()
        re_confermation_continue_or_not()
    elif(treatmentview == '9' or treatmentview == 'main menu' or treatmentview == 'exit' ):
        View_Treatment()
        re_confermation_continue_or_not()
    else:
        print('\nwrong data entered please try again...\n ')
        border()
        print('1: show suggestion\n2: try again without suggestion\n3: exit')
        border()
        exit1=input('input your choice: ')
        if(exit1 == '1' or exit1 == 'show suggestion' or exit1 == 'show'):
            loading()
            Simplelist()
            View_Treatment()
        elif(exit1=='3' or exit1 == 'exit'):
            print()
        else:
            View_Treatment()
def re_confermation_continue_or_not():
    print('1: search for more\n2: main menu')
    confirmation = input('input your choice: ')
    if(confirmation == '1' or confirmation == 'more'):
        View_Treatment()
    elif(confirmation == '2' or confirmation == 'mainmenu' or confirmation == 'main menu' ):
        loading()
        question()
        loading()
    else:
        re_confermation_continue_or_not()
    
def Rashes():
    border()
    print("\t\t\t-->problem: Rashes")
    border()
    print("on examination we recomend that:\n1) Avoid scrubbing you skin.\n2) Use cleanser and apply it gently. \n3) Use warm (not too hot) water for cleaning, Just dry it don't rub.")
    border()
def rashesinve():
    print('did you having any elergy? (y/n)')
    s1 = input()
    print('did you work more than 5 hours a day? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n') or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO'):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Rashes()
        xx = input()
        question()
   
       
def generatesuggestion():
    for i in tqdm(range(10), desc = 'generating consulation advice'):
        time.sleep(0.5)
   
   
def Acne():
    border()
    print("\t\t\t-->problem: Acne")
    border()
    print("on examination we recomend that:\n1) You need antibiotics to reduce bacteria on your skin.\n2) This is an over-the-counter (OTC) cream that kills bacteria and helps you to acne free skin.")
    border()
def acneinve():
    print('did you having any skin elergy? (y/n)')
    s1 = input()
    print('did you any other skin infection? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n') or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO'):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Acne()
        xx = input()
        question()
   
     
   
   
def Oily_Skin():
    border()
    print("\t\t\t-->problem: Oily Skin")
    border()
    print("on examination we recomend that:\n1) Wash your skin regularly.\n2) Apply a skin tonner.\n3) Use Facial Mask. \n4) Apply moisturizer.")
    border()
def oilyskininve():
    print('did you stay out for more than 8 hours a day? (y/n)')
    s1 = input()
    print('did you work more than 5 hours a day? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Oily_Skin()
        xx = input()
        question()
   
   
   
   
def Dry_Skin():    
    border()
    print("\t\t\t-->problem: Dry Skin")
    border()
    print("on examination we recomend that:\n1) Taking bath to 5 or 10 minutes.\n2) Wash your skin with gentle and fragrance free cleanser. \n3) Slather/spread the moisturizer immediately after drying your skin.")
    border()
def dryskininve():
    print('did you stay out for more than 8 hours a day? (y/n)')
    s1 = input()
    print('did you work more than 5 hours a day? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Dry_Skin()
        xx = input()
        question()
   
     
   
 
def Open_Pores():
    border()
    print("\t\t\t-->problem: Open Pores")
    border()
    print("on examination we recomend that:\n1) you should use non-comedogenic skin care products.\n2) Use warm water to wash your face.\n3) Clean your face twice a day.")
    border()
def openporesinve():
    print('do you have oily skin? (y/n)')
    s1 = input()
    print('do you have any genetic disease of skin? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Open_Pores()
        question()
        xx = input()
        question()
   
     
   
 
   
   
def Hives():
    border()
    print("\t\t\t-->problem: Hives")
    border()
    print("on examination we recomend that:\n1) If your symptoms are mild, you may not need treatment.\n2) Avoid overheating.\n3) Wear loose-fitting, cotton clothes.\n4) Apply a cold compress, such as ice cubes wrapped in a washcloth, to the itchy skin several times a day.\n5) Prevent dry skin by using a fragrance free moisturizer several times a day.")
    border()
def hivesinve():
    print('do you scratch your skin? (y/n)')
    s1 = input()
    print('did you have any skin infection? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Hives()
        xx = input()
        question()
   
     
   
 
   
   
def Dark_spots():
    border()
    print("\t\t\t-->problem: Dark Spots")
    border()
    print("on examination we recomend that:\n1) Dark spots on the skin do not require treatment.\n2) If u want to remove your dark spots then wo have to do a laser treatment.\n3) Or you have to take a chemical peels.")
    border()
def darkspotinve():
    print('do you work on laptop or mobile for more than 5 hours a day? (y/n)')
    s1 = input()
    print('do you have deficiency of blood? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Dark_spots()
        xx = input()
        question()
   
     
   
 
   
   
def Melasma():
    border()
    print("\t\t\t-->problem: Melasma")
    border()
    print("on examination we recomend that:\n1) Triple combination cream (hydroquinone, tretinoin, and corticosteroid) the most effective treatment for melasma.\n2) Also you can use Chemical peels to come over with melasma.\n3) Or you have to take a chemical peels.")
    border()
def melasmainve():
    print('do you have deficiency of vitamin C and D? (y/n)')
    s1 = input()
    print('do you work in any type of ultra voilent location? (y/n)')
    s2=input()
    if(s1 == 'n' and s2 == 'n' or (s1 == 'no' and s2 == 'no') or (s1 == 'NO' and s2 == 'NO')):
        loading()
        doctorSelection()
    else:
        generatesuggestion()
        Melasma()
        xx = input()
        question()
   
     
   
 
def doctorSelection():
    print('First answer few questions')
    border()
    print('input your gender: ')
    gender = input('')
    name = input('input your name: ')
    category(gender, name)


def category(gender, name):
    print('okay so Mr/Mrs ---',name.upper(), '---')
    print('input your age:')
    age = int(input())
    if(age<=0):
        print('enter valid age please')
    elif(age >= 1 and age <= 18):
        print('you will be examined by the dermatologist consultant of children...')
        Child_Consultancy()
    elif(age > 18 and age <= 150):
        print('you will be examined by the dermatologist consultant of adults...')
        Adult_Consultancy()
    else:
        print('wrong input...')
        print('make sure that this softwere is only for under 150 year of age people')
        category('', 'client')

def loadingdoc():
    for i in tqdm(range(10), desc = 'Connecting to respective consultant '):
        time.sleep(0.5)

def Child_Consultancy():
    loadingdoc()
    child_problems()

    
def Adult_Consultancy():
    loadingdoc()
    adult_problems()

def child_problems():
    print('--------------------------------------------------------------------------------')
    print('\tHy i-m your consultant. My name is Sohaib. How may i help you')
    print('--------------------------------------------------------------------------------')
    print('\ninput your problem/issue need to be consulted')
    problem = input()
    if(problem == 'rashes' or problem == 'Rashes' or problem == 'RASHES' or problem == 'rashis' or problem == 'i am having rashes'):
        rashesinve()
        x=input()
    elif(problem == 'acne' or problem == 'Acne' or problem == 'ACNE' or problem == 'i am having acne' ):
        acneinve()
        x=input()
    elif(problem == 'Oily Skin' or problem == 'oilyskin' or problem == 'OILY SKIN' or problem == 'oily skin' or problem == 'i am having oily skin'):
        oilyskininve()
        x=input()
    elif(problem == 'dry skin' or problem == 'Dry Skin' or problem == 'DRY SKIN' or problem == 'dryskin' or problem == 'i am having dry skin'):
        dryskininve()
        x=input()
    elif(problem == 'open pores' or problem == 'open pore' or problem == 'Open Pores' or problem == 'openpores' or problem == 'i am having open pores'):
        openporesinve()
        x=input()
    elif(problem == 'hives' or problem == 'HIVES' or problem == 'Hives' or problem == 'hive' or problem == 'i am having hives'):
        hivesinve()
        x=input()
    elif(problem == 'Dark spots' or problem == 'dark spots' or problem == 'dark spot' or problem == 'darkspot' or problem == 'i am having dark spots'):
        darkspotinve()
        x=input()
    elif(problem == 'melasma' or problem == 'milasma' or problem == 'MELASMA' or problem == 'MILASMA' or problem == 'i am having melasma'):
        melasmainve()
        x=input()
    else:
        print('wrong input....')
        border()
        print('1: do you want suggestions in input\n2: try again without suggestion\n3: exit the softwere\ninput your choice: ')
        x=input()
        if x == '1' or x == 'sugestions' or x == 'suggestion' or x == 'suggestions':
            generatingSuggestion()
            suggestionlsit()
            child_problems()
            print('suggestion list')
        elif x == '2' or x == 'try again':
            child_problems()
        elif x == '3' or x == 'exit':
            print()
        else:
            child_problems()
def adult_problems():
    print('--------------------------------------------------------------------------------')
    print('\tHy i-m your consultant. My name is Muzzamil. How may i help you')
    print('--------------------------------------------------------------------------------')
    print('\ninput your problem/issue need to be consulted')
    problem = input()

    if(problem == 'rashes' or problem == 'Rashes' or problem == 'RASHES' or problem == 'reshes' or problem == 'i am having rashes'):
        print()
        rashesinve()
        x=input()
    elif(problem == 'acne' or problem == 'Acne' or problem == 'ACNE' or problem == 'i am having acne' ):
        print()
        acneinve()
        x=input()
    elif(problem == 'Oily Skin' or problem == 'oilyskin' or problem == 'OILY SKIN' or problem == 'oily skin' or problem == 'i am having oily skin'):
        print()
        oilyskininve()
        x=input()
    elif(problem == 'dry skin' or problem == 'Dry Skin' or problem == 'DRY SKIN' or problem == 'dryskin' or problem == 'i am having dry skin'):
        print()
        dryskininve()
        x=input()
    elif(problem == 'open pores' or problem == 'open pore' or problem == 'Open Pores' or problem == 'openpores' or problem == 'i am having open pores'):
        print()
        openporesinve()
        x=input()
    elif(problem == 'hives' or problem == 'HIVES' or problem == 'Hives' or problem == 'hive' or problem == 'i am having hives'):
        print()
        hivesinve()
        x=input()
    elif(problem == 'Dark spots' or problem == 'dark spots' or problem == 'dark spot' or problem == 'darkspot' or problem == 'i am having dark spots'):
        print()
        darkspotinve()
        x=input()
    elif(problem == 'melasma' or problem == 'milasma' or problem == 'MELASMA' or problem == 'MILASMA' or problem == 'i am having melasma'):
        print()
        melasmainve()
        x=input()
    else:
        print('wrong input....')
        border()
        print('1: do you want suggestions in input\n2: try again without suggestion\n3: exit the softwere\ninput your choice: ')
        x=input()
        if x == '1' or x == 'sugestions' or x == 'suggestion' or x == 'suggestions':
            generatingSuggestion()
            suggestionlsit()
            adult_problems()
           
        elif x == '2' or x == 'try again':
            adult_problems()
        elif x == '3' or x == 'exit':
            print()
        else:
            adult_problems()

def suggestionlsit():
   
    print('the inputs can be...')
    border()
    print('rashes')
    print('acne')
    print('oily skin')
    print('dark skin')
    print('open pores')
    print('hives')
    print('dark spots')
    print('melasma\n\n')
    border()
def generatingSuggestion():
    for i in tqdm(range(10), desc = 'Generating Suggestions please wait -->'):
        time.sleep(0.5)
    
    
def agee():
    age = int(input('input age: '))
    if(age<=0):
        print('enter valid age please')
    elif(age >= 1 and age <= 18):
        print('you will be examined by the dermatologist consultant of children...')
        Child_Consultancy()
    elif(age > 18 and age <= 150):
        print('you will be examined by the dermatologist consultant of adults...')
        agee()
    else:
        print('wrong input...')
        print('make sure that this softwere is only for under 150 year of age people')
        agee()


StartingDesign()
question()
print('thankyou for your precious time!')


# In[ ]:




