"""
use www.uszip.com

example url: http://www.uszip.com/zip/02492

-prompt the user for a zip code
-print the name and population of the corresponding city

sample city name html:
<!-- place name / title -->
    <hgroup>
        <div style="position:relative;float:right;top:2px;right:-3px">  
            <div class="fb-like" data-href="" data-width="" data-height="" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="true" data-send="false"></div></div><div style="position:relative;float:right;top:4px;right:-25px">  
            <div class="g-plusone" data-size="medium" data-count="true">
        </div>      
        <script type="text/javascript">        
        window.___gcfg = {lang: 'en-GB'};          
        (function() {         var po = document.createElement('script'); 
            po.type = 'text/javascript'; po.async = true;            
            po.src = 'https://apis.google.com/js/platform.js';          
            var s = document.getElementsByTagName('script')[0]; 
            s.parentNode.insertBefore(po, s);         })();     
        </script>
        </div>                             
        <h3>
            <strong>98033</strong> is the zip code for
        </h3>
        <h2>
            <strong>Kirkland, 
                <a href="state.php?state=WA">WA</a>
            </strong>
        </h2>
    </hgroup>

sample population html:
<!-- geographic data / map -->
    <dl class="zip-stats zip-stats-left">
        <dt class="fw">Also in this location:</dt>
        <dt class="l2 fw">
            <strong>Bellevue, 
                <a href="state.php?state=WA">WA</a>
            </strong>
        </dt>
        <hr>
            <dt>Total population</dt>
        <dd>34,338
            <span class="trend trend-up" title="+3,945 (+11.49% since 2000)">&#9650;</span>
        </dd>
"""
import requests
import mysql.connector

def get_zip_pages(base_url, zip_list):
    """
    Returns raw html for all US zip code pages linked to the base url as a dictionary.

    Input:
        base_url: string, the url which links to zip code information when that zip code is suffixed to the url.
    Output:
        html_dict: dictionary, {str(zip_code):str(raw_html)}

    """
    html_dict = {}
    for zip_code in zip_list:
        try:
            url = extend_url(base_url, zip_code)
            html = get_page(url)
            if html:
                html_dict[str(zip_code)] = get_page(url)
                print "Successfully crawled %s." % url
            else:
                print "No zip code info at %s" % url
        except: 
            print ConnectionError, "Failed to connect to %s." % url 
    return html_dict

def generate_zip_list(zip_min=1001, zip_max=1050, length=5):
    """
    Returns a list of [length]-digit zip codes. Default to US state zip code parameters (exclude PR and IRS).
    """
    zip_list = []
    for zip_code in range(zip_min, zip_max + 1):
        try:
            zip_code = full_zip(str(zip_code))
            try:
                zip_list.append(zip_code)
            except:
                continue
        except:
            print RuntimeError, "Failed to extend %s to the desired length." % str(zip_code)
    return zip_list

def full_zip(zip_string, length=5):
    """
    Extends a zip code to the desired length with leading 0s. Default to 5-digits.
    """
    while len(zip_string) < length:
        zip_string = '0' + zip_string
    return zip_string

def extend_url(base_url, extension):
    """
    Returns base_url with extension appended with a backslash.
    """
    return base_url + str(extension)

def get_page(url):
    """
    Returns the source html for the url.
    """
    html = ''
    try:
        conn = requests.get(url)
        for line in conn:
            html += line.strip()
        if check_page(html):
            return html
    except:
        return

def check_page(html):
    if html.find('We were unable to locate this zip code') > 0:
        return false
    return True

def parse_city_name(html, zip_code):
    """
    Returns the city name linked to zip_code according to the html from uszip.com.
    """
    try:
        leading_index = html.find('> is the zip code for')
        city_tag_index = html.find('<strong>', leading_index)
        trailing_comma_index = html.find(',', city_tag_index)
        result = html[city_tag_index + len('<strong>'):trailing_comma_index]
        if len(result) < 100:
            return result
        else:
            print ValueError, 'No city name found for zip code %s.' % (zip_code)
    except:
        print ValueError, 'No city name found for zip code %s.' % (zip_code)

def parse_population(html, zip_code):
    """
    Returns the population linked to zip_code according to the html from uszip.com.
    """
    try:
        leading_index = html.find('Total population')
        population_tag_index = html.find('<dd>', leading_index)
        trailing_carrot_index = html.find('<', population_tag_index + 1)
        result = html[population_tag_index + len('<dd>'):trailing_carrot_index]
        if len(result) < 15:
            return result
        else:
            print ValueError, 'No population found for zip code %s.' % str(zip_code)
    except:
        print ValueError, 'No population found for zip code %s.' % str(zip_code)

def build_zip_list(html_dict):
    zip_list = []
    for zip_code, html in html_dict.items():
        zip_list.append((zip_code, 
            parse_city_name(html, zip_code),
            parse_population(html, zip_code)
            ))
    return zip_list

def insert_data(table, data, columns):
    """
    Inserts multiple rows of data into a MySQL database.

    Input:
        table: string, name of target table.
        data: list of tuples, rows of data to be inserted.
        columns: list of strings, names of columns according to data order.
    Output:
        None
    """
    values = []
    for c in range(len(columns)):
        values.append('%s')
    cnxn = mysql.connector.connect(host = '127.0.0.1', 
        database = 'zip_dbd',
        user = 'root', 
        password = 'root')
    insert = """
        INSERT INTO %s (%s)
        VALUES (%s)
        """ % (table, ', '.join(columns), ', '.join(values))
    cursor = cnxn.cursor()
    cursor.executemany(insert, data)
    cnxn.commit()

base_url = 'http://www.uszip.com/zip/'

zip_list = generate_zip_list()

html_dict = get_zip_pages(base_url, zip_list)

zip_list = build_zip_list(html_dict)

insert_data('USZip', zip_list, ['zip_code', 'city_name', 'population'])


























