# jackbox-finder

This script finds active Jackbox rooms matching a regex pattern.

```
python room_finder.py [-r <regex>]
```

## Requirements:

- The latest version of [Python 3](https://www.python.org/downloads/)

- Probably some `pip` packages which it'll ask you to install on first run

## Example:

Let's say you're watching a Twitch streamer and they say "My Jackbox room code begins with the letters QW."

You can find all rooms that begin with `QW` by running

```
python room_finder.py -r QW..
```

## Credits:

This script is just a specialized version of [this other script](https://github.com/JLDevOps/Jackbox.tv-Room-Finder).
