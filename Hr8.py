'''
Created on Aug 13, 2015

@author: hnjamba
'''

def helloGreet(personName):
    print "Hello {}, how are you doing".format(personName)
    
def print_address(name, address):
    print name
    print address
    

def welcome(first, last, middle = ''):
    print "Welcome {} {} {}!".format(first, middle, last)
    fullName = first + ' ' + middle + ' ' + last
    return fullName

def varied_args(param1, param2, **kwargs):
    print param1
    print param2
    print kwargs

def test_args(first, second, *args):
    print first
    print second
    print args
    
def main():
    helloGreet("Hannah")
    
    placeName = "Heich Cyber Cafe"
    placeAddress = "Lower Kabete Kiambu \nWangige Shopping Center"
    print_address(address = placeAddress, name = placeName)
    
    personFullName = welcome(last = "Gimel", first = "James")
    print personFullName
    
    varied_args(param1="Hello", param2="World", item_three="How are you", item_four="Hope fine")
    
    test_args(1, 2, 3, 4, 5)
    
if __name__ == "__main__":
    main()