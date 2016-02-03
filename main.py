# https://www.syncfusion.com/resources/techportal/ebooks

import urllib, re, urllib2, pdb
from BeautifulSoup import *

dl_link = "http://files2.syncfusion.com/Downloads/Ebooks/"


def download_file(download_url, title):
    response = urllib.urlopen(download_url)
    file = open("%s.pdf" % title, 'w')
    file.write(response.read())
    file.close()
    

def main():
    
    url = 'https://www.syncfusion.com/resources/techportal/ebooks'
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    print("Downloading books from %s\n" % url)
    
    h3_tags = soup('a', href=True)
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
                pdf_name = pdf_name.replace('GIS_', 'GIS ')
                pdf_name = pdf_name.replace('Part_', 'Part ')
                pdf_name = pdf_name.replace('Csharp', 'C_Sharp')
                pdf_name = pdf_name.replace('SQL_on', 'SQL_On')
                pdf_name = pdf_name.replace('.Forms', '_Forms')
                pdf_name = pdf_name.replace('Phone_8', 'Phone8')
                pdf_name = pdf_name.replace('Prism_4', 'Prism4')
                pdf_name = pdf_name.replace('strap_3', 'strap3')
                pdf_name = pdf_name.replace('Message_Queuing_with_RabbitMQ', 'RabbitMQ')
                pdf_name = pdf_name.replace('8.1', '8_1')
                pdf_name = pdf_name.replace('Windows_Azure_SQL_Reporting', 'WindowsAzureSqlReporting')
                pdf_name = pdf_name.replace('Azure_Websites', 'Azure')
                pdf_name = pdf_name.replace('SharePoint_2013_App_Model', 'SharePoint')
                pdf_name = pdf_name.replace('_Expressions', 'Expressions')
                pdf_name = pdf_name.replace('Functional_Programming_Succinctly', 'functional_programming_succinctly')
                pdf_name = pdf_name.replace('Localization_for_.NET_', 'Localization_')
                pdf_name = pdf_name.replace('Analysis_Services_Succinctly','Analysis_Services Succinctly')
                pdf_name = pdf_name.replace('Unit_Testing','UnitTesting')
                pdf_name = pdf_name.replace('Windows_Store_Apps','WindowsStoreApps')
                pdf_name = pdf_name.replace('-C_Succinctly','-C Succinctly')
                pdf_name = pdf_name.replace('ASP.NET_MVC_4_Mobile_Websites','aspnetmvc4')
                
                
                pdf_link = dl_link + pdf_name + ".pdf"

                # Download book
                try:
                    download_file(pdf_link, pdf_name)
                    print 'Downloaded %s' % pdf_name
                    dl_counter += 1
                except Exception, e:
                    print str(e)
                    failed_dls.append(pdf_link)

    if len(failed_dls) > 0:
        print '#################'
        print ''
        print 'Failed DLs'
        for fail_dl in failed_dls:
            print fail_dl

    print '#################'
    print ''
    print 'Downloaded books: %s' % dl_counter
    print 'Failed Downloads: %s' % len(failed_dls)

            
if __name__ == "__main__":
    main()
