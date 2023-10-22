# Author: Tahmid Mehdi
# Date: Oct 22, 2023
# Takes a uuidv6 (no hyphens) as an arg and extract the datetime for it
import datetime
import sys


def extract_timestamp_from_uuidv6(uuid_string: str) -> datetime.datetime:
    # gets timestamp from uuidv6 (13th char must be 6)
    try:
        # Extract timestamp characters from the UUID string
        timestamp_hex = uuid_string[:12] + uuid_string[13:16]
        timestamp_int = int(timestamp_hex, 16)
        # UUID epoch: October 15, 1582
        uuid_epoch = datetime.datetime(1582, 10, 15)
        # Convert 100-nanoseconds intervals to seconds and add to UUID epoch
        timestamp_seconds = timestamp_int / 10000000
        timestamp_datetime = uuid_epoch + datetime.timedelta(
            seconds=timestamp_seconds
        )
        return timestamp_datetime
    except (ValueError, IndexError):
        return None


def main(uuid_string: str) -> None:
    dt = extract_timestamp_from_uuidv6(uuid_string)
    print(dt)


if __name__ == '__main__':
    main(sys.argv[1])
