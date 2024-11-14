import pychromecast

# pychromecast.get_chromecasts() returns a tuple(list, pychromecast.discovery.CastBrowser)
(chromecasts, castBrowser) = pychromecast.get_chromecasts()

print(chromecasts[0].cast_info.friendly_name)
