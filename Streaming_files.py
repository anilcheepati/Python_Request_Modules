import requests
from tqdm import tqdm

url="https://javadl.oracle.com/webapps/download/AutoDL?BundleId=249550_4d245f941845490c91360409ecffb3b4"
r= requests.get(url,stream=True)
totalExpectedbytes=int(r.headers["Content-Length"])
bytesreceived=0
progress_bar=tqdm(total=totalExpectedbytes,unit='iB',unit_scale=True)
with open("java.exe",'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        progress_bar.update(128)
        f.write(chunk)
        bytesreceived+=128

progress_bar.close()

