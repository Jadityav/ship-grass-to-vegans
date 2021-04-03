import os

def importing_names():

    page_names = os.listdir("./content")
    return (page_names)

# combining templates
def templates():
     
    top_html = open ('./templates/top.html').read()
    bottom_html = open ('./templates/bottom.html').read()
    return (top_html, bottom_html)

# loop for compiling htmls
def main(page_names, top_html, bottom_html):
    
    for x in page_names:
        path_origin = str("./content/" + x)
        
        middle_html = open (path_origin).read()

        combined = top_html  + middle_html + bottom_html

        path_destination= str("./docs/" + x)
                    
        open (path_destination, 'w+').write(combined)

# storing returns in variables
page_names= importing_names()
top_html, bottom_html = templates()

# using vairables in main function
main(page_names, top_html, bottom_html)