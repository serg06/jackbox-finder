import argparse
import csv
import datetime
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import product
import re

import requests

base_url = "https://blobcast.jackboxgames.com/room/"


def test_room_code(code, csv_file=None):
    try:
        jackbox_url = base_url + str(code)
        r = requests.get(url=jackbox_url)
        data = r.json()
        if r.status_code == 200:
            return code
        return None

    except Exception as e:
        return "Error: [" + code + "] - " + str(e)


def generate_room_codes(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code_list = [''.join(i) for i in product(chars, repeat=length)]
    return code_list


def main():
    st = time.time()
    parser = argparse.ArgumentParser(description='Checks if there are any available room in Jackbox.Tv')
    parser.add_argument('-r', '--room', help='Room code (regex)', required=False)

    args = vars(parser.parse_args())
    room_code = args['room']
    code_list = generate_room_codes(4)

    if room_code:
        p = re.compile(room_code)
        code_list = [code for code in code_list if p.match(code)]

    print("searching through", len(code_list), "codes:")

    with ThreadPoolExecutor(max_workers=13) as executor:
        futures = [executor.submit(test_room_code, code) for code in code_list]
        try:
            for future in as_completed(futures):
                result = future.result()
                if result:
                    print(result)
        except KeyboardInterrupt as e:
            raise
            # executor._threads.clear()
            # thread._threads_queues.clear()

    print("total time: %s" % (time.time() - st))


if __name__ == "__main__":
    main()
