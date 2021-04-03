import os

page_names = os.listdir("./content")
for x in page_names:

    path_origin = str("./content/" + x)
    
    top_html = open ('./templates/top.html').read()
    bottom_html = open ('./templates/bottom.html').read()
    middle_html = open (path_origin).read()

    combined = top_html  + middle_html + bottom_html

    path_destination= str("./docs/" + x)
    
    open (path_destination, 'w+').write(combined)