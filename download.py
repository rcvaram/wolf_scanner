import requests


def download(url, path):
    get_response = requests.get( url )
    file_name = url.split( "/" )[-1]
    with open( path + "/" + file_name, "wb" ) as out_file:
        out_file.write( get_response.content )

