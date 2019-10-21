# Victor Velasco (WebPageGenerator) 10/7/19

def main():
    name = input('Enter your name: ')
    description = input('Describe yourself: ')

    # Create file
    html_file = open('my_page.html', 'w') # 'w' = Write permission

    # Write HTML code
    write_html(html_file, name, description)

    # Close file
    html_file.close()

def write_html(html_file, name, description):
    html_file.write('<html>\n')
    write_head(html_file)
    write_body(html_file, name, description)
    html_file.write('</html>\n')
    
def write_head(html_file):
    html_file.write('<head>\n')
    html_file.write('<title>My Personal Web Page</title>\n')
    html_file.write('</head>\n')

def write_body(html_file, name, description):
    html_file.write('<body>')
    html_file.write('\t<center>\n')
    html_file.write('\t\t<h1>')
    html_file.write(name)
    html_file.write('</h1>\n')
    html_file.write('\t</center>\n')
    html_file.write('\t<hr>\n\t')
    html_file.write(description)
    html_file.write('\t<hr>\n\t')
    html_file.write('</body>\n')

# Call main
main()
