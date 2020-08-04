import requests

def get_file(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as ex:
        print("Error: {}".format(ex))
    

if __name__ == "__main__":
    main()