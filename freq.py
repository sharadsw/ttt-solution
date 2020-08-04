import requests
import re
from operators import itemgetter

# Fetches file from given url
# Returns the text contained in the file
def get_file(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as ex:
        print("Error: {}".format(ex))

    return res.text

# Cleans the text fetched from file
# Removes weird-looking unicode chars
# Removes escape characters
def clean_text(text):
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = re.sub('\W+', " ", text)

    return text

# Takes inputs text and n
# Parses text to find frequency of words
# Creates a dict with words and their occurrence
# Returns a list of tuples with n most frequent words
def parse_text(text, n):
    freq = {}
    for word in text.split():
        if word not in freq:
            freq[word] = 0
        else:
            freq[word] = freq.get(word) + 1
    # Sorts the dict values into a list of tuples
    sort_freq = sorted(freq.items(), key=itemgetter(1))

    return sort_freq[:n]
    

if __name__ == "__main__":
    main()