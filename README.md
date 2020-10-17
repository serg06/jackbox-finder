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

- [JLDevOps](https://github.com/JLDevOps/) for the [original version](https://github.com/JLDevOps/Jackbox.tv-Room-Finder) of this script.

- [Pokelawls](https://www.twitch.tv/pokelawls) for the inspiration.
