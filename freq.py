import requests
import re
from operator import itemgetter
import sys

# Fetches file from given url
# Returns the text contained in the file
def get_file(url):
    try:
        res = requests.get(url)
    except Exception as ex:
        print("URL possibly incorrect")
        print("Error: {}".format(ex))
        sys.exit()

    try:
        res.raise_for_status()
    except Exception as ex:
        print("Site possibly unavailable")
        print("Error: {}".format(ex))
        sys.exit()

    return res.text

# Cleans the text fetched from file
def clean_text(text):
    # Removes unicode chars
    text = text.encode("ascii", "ignore").decode("utf-8")
    # Removes escape chars, punctuations   
    text = re.sub(r'\W+', " ", text)
    # Remove excess spaces and change to lowercase           
    text = text.strip().lower()

    return text

# Takes inputs text and n
# Parses text to find frequency of words
# Creates a dict with words and their occurrence
# Returns a list of tuples with n most frequent words
def parse_text(text, n=None):
    flag = False
    freq = {}

    for word in text.split():
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] = freq.get(word) + 1
    # Sorts the dict values into a list of (key, value) tuples
    sort_freq = sorted(freq.items(), key=itemgetter(1), reverse=True)

    # if n is too high, set flag to true
    if n is not None and int(n) > len(sort_freq):
        flag = True

    if n is None or flag:
        return sort_freq, flag

    return sort_freq[:int(n)], flag
    
def main():
    if len(sys.argv) < 2:
        print("Invalid args")
        exit()

    url = sys.argv[1]
    try:
        num = sys.argv[2]
    except Exception as ex:
        print("Input n not provided in args: {}".format(ex))
        num = None

    if num is not None and int(num) < 1:
        print("N can't be negative")
        sys.exit()

    file_text = get_file(url)
    cleaned = clean_text(file_text)
    nfreq, flag = parse_text(cleaned, num)

    if num is None or flag:
        print("N not provided or too high, displaying all words instead:")
    else:
        print("{} most frequent words:".format(num))

    for k, v in nfreq:
        print("{}\t{}".format(k, v))

if __name__ == "__main__":
    main()