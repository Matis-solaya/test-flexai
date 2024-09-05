import time 
from tqdm import tqdm

if __name__=="__main__":
    for i in tqdm(range(20)):
        time.sleep(1)
