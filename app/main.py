import os
from os import walk
import time

# todo
# test no wordlists 

class redline():
    
   
    def __init__(self) -> None:
        self.wordlist_opt = '\033[91m[1] Load Wordlist\033[0m'
        self.website_opt = '\033[91m[2] Load Website\033[0m'
        self.download_opt = '\033[91m[3] Download Copy of Site\033[0m'
        self.webinfo_opt = '\033[91m[4] Get Website Information\033[0m'
        self.directory_opt = '\033[91m[5] Directory Scan\033[0m'
        
        self.website = ''
        self.wordlist = ''
        
        
    
    
    
    def main(self) -> None:
        self.menu()
    
    
    
    def menu(self) -> None:
        while True:
            os.system('clear')
            
            print(
                f"""{colors.FAIL}
                        ██████  ███████ ██████  ██      ██ ███    ██ ███████ 
                        ██   ██ ██      ██   ██ ██      ██ ████   ██ ██      
                        ██████  █████   ██   ██ ██      ██ ██ ██  ██ █████   
                        ██   ██ ██      ██   ██ ██      ██ ██  ██ ██ ██      
                        ██   ██ ███████ ██████  ███████ ██ ██   ████ ███████ 
                {colors.ENDC}"""
            )
            print(f'\n{self.wordlist_opt:<45}{self.website_opt:<40}{self.download_opt:<35}\n')
            print(f'{self.webinfo_opt:<45}{self.directory_opt:<40}') 
            menu_option = input('\n\033[93m> \033[0m')
            
            
            
            if menu_option == '1':
                
                if self.wordlist != '':
                    print('\n\033[93mWordlist Being Replaced!\033[0m')


                for (dirpath, dirnames, filenames) in walk('app/wordlists'):
                    
                    print('')
                    
                    for i in range(0, len(filenames)):
                        filename = filenames[i]
                        filename.replace('.txt', '')
                        print(f'\033[93m[{i + 1}] {filename}')    


                self.wordlist = input('\n\033[93mWordlist> \033[0m')
                
                self.wordlist = filenames[int(self.wordlist) - 1]
                
                self.wordlist_opt = '\033[92m[1] Load Wordlist (Loaded)\033[0m'
                
                if self.website != '':
                    self.directory_opt = '\033[92m[5] Directory Scan\033[0m'
                
                
            
            elif menu_option == '2':
                
                if self.website != '':
                    print('\n\033[93mWebsite Being Replaced!\033[0m')

                
                self.website = input('\n\033[93mWebsite URL> \033[0m')
                
                self.website_opt = '\033[92m[2] Load Website (Loaded)\033[0m'
                self.download_opt = '\033[92m[3] Download Copy of Site\033[0m'
                self.webinfo_opt = '\033[92m[4] Get Website Information\033[0m'
                
                if self.wordlist != '':
                    self.directory_opt = '\033[92m[5] Directory Scan\033[0m'
                    
            
            
            
            if menu_option == '3' and self.website != '':
                pass
            elif menu_option == '3' and self.website == '':
                print('\n\033[93mWebsite Not Loaded!\033[0m')
                time.sleep(1)
            
            if menu_option == '4' and self.website != '':
                pass
            elif menu_option == '4' and self.website == '':
                print('\n\033[93mWebsite Not Loaded!\033[0m')
                time.sleep(1)
                
            if menu_option == '5' and self.website != '' and self.wordlist != '':
                pass
            elif menu_option == '5' and self.website == '':
                print('\n\033[93mWebsite Not Loaded!\033[0m')
                time.sleep(1)
            elif menu_option == '5' and self.wordlist == '':
                print('\n\033[93mWordlist Not Loaded!\033[0m')
                time.sleep(1)
                    
                    
                


                
            

         
    
    
    
    
    
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
    
if __name__ == '__main__':
    redline = redline()
    redline.main()