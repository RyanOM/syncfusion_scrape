# https://www.syncfusion.com/resources/techportal/ebooks

import urllib, re, urllib2, pdb
from BeautifulSoup import *

dl_link = "http://files2.syncfusion.com/Downloads/Ebooks/"


def download_file(download_url, title):
    response = urllib2.urlopen(download_url)
    file = open("%s.pdf" % title, 'w')
    file.write(response.read())
    file.close()
    

def main():
    
    #url = raw_input('Enter URL - ')
    url = 'https://www.syncfusion.com/resources/techportal/ebooks'
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    h3_tags = soup('a', href=True)
    failed = []
    failed_dls = []
    dl_counter = 0

    for tag in h3_tags:
        if len(re.findall('/details/ebooks/', tag.attrMap['href'])) > 0:
            a_tag = tag.text
            if a_tag != '':
                book_name = ''.join(a_tag.splitlines())
                pdf_name = book_name.replace(' ', '_')

                # Replace #, . or + chars
                pdf_name = pdf_name.replace('#', 'sharp')
                pdf_name = pdf_name.replace('+', 'plus')

                # Replace special names. Some patterns are too specific ....
                pdf_name = pdf_name.replace('.js', 'js')
                pdf_name = pdf_name.replace('Git', 'GIT')
                pdf_name = pdf_name.replace('GIS', 'GIS% ')
                pdf_name = pdf_name.replace('Part_', 'Part%20')
                pdf_name = pdf_name.replace('Csharp', 'C_Sharp')
                pdf_name = pdf_name.replace('SQL_on', 'SQL_On')
                pdf_name = pdf_name.replace('.Forms', '_Forms')
                pdf_name = pdf_name.replace('Phone_8', 'Phone8')
                pdf_name = pdf_name.replace('Prism_4', 'Prism4')
                pdf_name = pdf_name.replace('strap_3', 'strap3')
                pdf_name = pdf_name.replace('Message_Queuing_with_RabbitMQ', 'RabbitMQ')
                pdf_name = pdf_name.replace('8.1', '8_1')
                pdf_name = pdf_name.replace('Windows_Azure_SQL_Reporting', 'WindowsAzureSqlReporting')

                try:
                    pdf_link = dl_link + pdf_name + ".pdf"

                    # Download book
                    try:
                        download_file(pdf_link, pdf_name)
                        print 'Downloaded %s' % pdf_name
                        dl_counter += 1
                    except:
                        failed_dls.append(pdf_link)

                except:
                    failed.append(a_tag)

    print '#################'
    print ''
    print 'Failed DLs'
    for fail_dl in failed_dls:
        print fail_dl

    if len(failed) > 0:
        print '#################'
        print ''
        print 'Failed links'
        for fail in failed:
            print fail

    print '#################'
    print ''
    print 'Downloaded books: %s' % dl_counter
    print 'Failed Downloads: %s' % len(failed_dls)

            
if __name__ == "__main__":
    main()
