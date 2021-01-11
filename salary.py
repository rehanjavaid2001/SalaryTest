#Rehan Javaid rj3dxu
import urllib.request
import re

def name_to_url(a):
    """
    This function is used to change a name inserted into a url to be used in another function
    :param a: A name input in a certain way (i.e. James E. Ryan or Ryan, James E, etc.)
    :return: the proper formatted name to be used in a url
    """
    a = a.lower()
    if '.' in a:
        a = a.replace('.', '')
    if ',' in a:
        location = a.index(',')
        last_name = a[0:location]
        slice = a[0:location+2]
        a = a.replace(slice, '')
        a = a + ' ' + last_name
    a = a.replace(' ', '-')
    return a

def report(a):
    """
    This function returns the occupation, salary, and ranking compared to other employees for a specific name that is input into the function by a user
    :param a: Is a name for which information is obtained on
    :return: the occupation, salary, and rank for the individual
    """
    job = None
    money = 0
    rank = 0
    url = 'http://cs1110.cs.virginia.edu/files/uva2018/'
    url_final = url + name_to_url(a)
    try:
        urllib.request.urlopen(url_final)
    except:
        return job, money, rank

    read = urllib.request.urlopen(url_final).read().decode('utf-8')

    job_find = re.compile(r'Job title: ((([a-zA-Z]*[^<])*\s*)+[^<])')
    for match in job_find.finditer(read):
        job = match.group(1)

    money_find = re.compile(r'total gross pay: \$([0-9]+(,?[0-9]+))')
    for match in money_find.finditer(read):
        money = match.group(1)
    money = money.replace(',', '')

    rank_find = re.compile(r'rank</td><td>([0-9]+(,?[0-9]+)*)')
    for match in rank_find.finditer(read):
        rank = match.group(1)
    rank = str(rank).replace(',', '')

    job = job.replace('&#39;', "'")
    job = job.replace('amp;', '')

    return job, money, rank
