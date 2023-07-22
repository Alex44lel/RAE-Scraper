from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time
import json 

alphabet = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'i',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'ñ',
    'ñ': 'o',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
    'z': None
}
driver = webdriver.Chrome()
start_time = time.time()

def write_to_json(word):
    with open('words.json', 'a', encoding='utf8') as f:
        json.dump(word, f, ensure_ascii=False)
        f.write(',\n')  # write a newline after each word

current_word = "a"
current_link = "https://dle.rae.es/hola"
testCases = 0


try:
   
    while True:

        driver.get(current_link)
        search_bar = driver.find_element(By.ID,"wq")
        search_bar.send_keys(current_word)

        try:
           # if the element is present, then check if it's visible
            suggestion_elem = WebDriverWait(driver, 0.8).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div.autocomplete-suggestions")))
        except NoSuchElementException:
            suggestion_elem = None
        except TimeoutException:
            suggestion_elem = None

        words = 0
        suggestions = 0
        suggested_words = []

        if suggestion_elem:
            child_divs =WebDriverWait(suggestion_elem, 1).until(EC.visibility_of_all_elements_located((By.TAG_NAME,"div") )) 
            #check if there are words to add and if there are recommendations
            for div in child_divs:
                b_element = div.find_element(By.TAG_NAME,"b")
                b_text = b_element.text
                div_text = div.text

                if b_text == div_text:
                    write_to_json(b_text)
                    words +=1
                else:
                    suggested_words.append(div_text)
                    suggestions +=1

        #we aint sure there are less than ten suggestions
        if suggestions + words == 10:   
            #add next letter
            print("SUG EXISTS MORE THAN ONE - ADD letter")
          
            current_word = current_word + "a"
        
        elif suggestions < 10 and suggestions > 0:
            #manejar caso en el que es Z
            
            for i in suggested_words:
                write_to_json(i)
            #try next character
            print("SUG 1 - next letter")

            if current_word[-1] != "z":
                current_word =  current_word[:-1] + alphabet[current_word[-1]]
               
            else:
                #delete last character and change the second to last to the next one
                current_word = current_word[:-1]
                current_word =  current_word[:-1] + alphabet[current_word[-1]]
                

        #if no suggestions
        else:
            
            if (len(current_word)==1):
                
                write_to_json(current_word)
                current_word = current_word + "a"
            elif current_word[-2:] == "zz":
                current_word = current_word[:-2]
                current_word =  current_word[:-1] + alphabet[current_word[-1]]
            #if we are in the last letter of the alphabet
            elif current_word[-1] == "z":
                print("SUG 0 - Z")
                #delete last character and change the second to last to the next one
                current_word = current_word[:-1]
                current_word =  current_word[:-1] + alphabet[current_word[-1]]
                
            else:
                #try next character
                print("SUG 0 - next letter")
                current_word =  current_word[:-1] + alphabet[current_word[-1]]
                
        if(current_word == "zz"):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'The code took {elapsed_time} seconds to execute')
            driver.quit()
        
        current_link = "https://dle.rae.es/" + current_word
        testCases +=1
        print(words)
       

except Exception as e:
    print(current_word)
    print(f"An error occurred: {e}")
    driver.quit()
    

