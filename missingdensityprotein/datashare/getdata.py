from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import discovery
import requests
import io
import os
from googleapiclient.http import MediaIoBaseDownload


def get_samples():
    """
    This method can download samples used in example from out drive.
    When executing the method, it will prompt a link and an input box.
    To get the verification code, you have to click the link and then
    choose the google account. Copy the code shown on screen and paste
    it to the input box. Then, it will create a token.json and a folder
    named ExampleData. There are four csv files and two zip file including
    20 pdb files and 3000 pdbfiles in the ExampleData folder.
    """
    credential = 'client_id.json'
    url = 'https://github.com/yhchen24/Missing-Density-PDB/\
        raw/master/missingdensityprotein/datashare/client_id.json'
    if not os.path.exists(credential):
        req = requests.get(url)
        with open(credential, 'wb') as f:
            f.write(req.content)
    obj = lambda: None
    lmao = {"auth_host_name": 'localhost',
            'noauth_local_webserver': 'store_true',
            'auth_host_port': [8080, 8090],
            'logging_level': 'ERROR'}
    for k, v in lmao.items():
        setattr(obj, k, v)
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store, obj)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    file_id = ['1GXkUZzSUFu0F_tMMI1FtNA42eTiwx_G8',
               '1Nl1a5GFam5y9J0V9Nm8uo2hDoMdx9BnI',
               '1YwjTZAhtUJwUr54Ao1X40VwUHeCvJ8F7',
               '1PQgmaFljME2WaCiTBRUSWdAV70bWRwax',
               '1Nk9X6zMeDWDQcDHKTg7FtQCOX9nXe32J',
               '1-USFXT-rbCKrrRAyVXZwNgUIyWKFu9JG']
    filename = ['headers_1000.csv',
                'res_data_1000.csv',
                'samples_1000.csv',
                'summary_1000.csv',
                'small_data',
                'all_data']
    if not os.path.exists('ExampleData/'):
        os.mkdir('ExampleData')
    for i in range(len(file_id)):
        if not os.path.exists('ExampleData/' + filename[i]):
            request = DRIVE.files().get_media(fileId=file_id[i])
            fh = io.FileIO('ExampleData/' + filename[i], mode='w')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
    return 'All files exist.'
