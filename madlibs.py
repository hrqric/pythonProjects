from sample_stories import st3, parkadv, misterio
import random

if __name__ == "__main__":
    m = random.choice([parkadv,misterio,st3])
    print(m())