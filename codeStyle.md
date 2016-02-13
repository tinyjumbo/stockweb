# I know we all prefer different styles but for teamwork and save others' time to add or modify your code, let's follow our own rules
General Rule:
1. 4 spaces as tab indentations

2. keep variable with meaning
   avoid names like a b

3. add comments before methods and functions

4. capitalize constants NAMES = ['Zach', 'Sicong Wang']

5. backend files please add @author and @dates

6. do not leave extra line by the end of files

Special Styles

1. JS 
function() 
{
    var a = 1;	
}

instead of 

function() {
    var a = 1;	
}

bookName
instead of bookname or book_name

Please follow unobtrusive programming style. (if you do not know what it is, google it.)
Also make sure all the functions work like API, which we can use it multi times. 
We can have a general script.js file like the first file. Later on, based on need, different views should maintain their own js file.

2. Python

book_name

instead of bookName or bookname

def getInput(book_name):
    book_name += 1
    return book_name

instead of 

def getInput(book_name):
    book_name+=1
    return book_nme

strings

"a" instead of 'a'

visibility 

special methods only called within a class should be defined as private.

3. SQL

capitalize all keywords

SELECT user_id FROM f_users WHERE name = 'jack';
