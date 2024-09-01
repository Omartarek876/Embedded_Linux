from sites import urls , firefox 


def print_menu() : 
    print("### the fav websites : ")
    for name in urls.keys() :
         print(f"- {name}") 
  

def main() : 
     print_menu()
     site = 0
     
     while(True) : 
        site = input("### enter the site you want to visit : ")
        if site == 'e':
            print("### Exit choice")
            break   
        firefox(site)
        print_menu()



if __name__ == "__main__":
    main()