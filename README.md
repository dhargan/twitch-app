# twitch-app
Playing around with Twitch API

- Login with your Twitch account
- Enter your favorite streamer to the input line and press watch.
- Enjoy :)

This is a very simple app yet relatively there are bottlenecks:
- In order to get streamers video information, two calls need to be made to the Twitch API. One for getting user_id using login info 
and one for getting stream information using user_id
- Again, two calls are being made to get authenticated and use authentication token to get user data.

If millions of requests a day are going to be made with this app;
- 1 dyno won't be enough (in terms of Heroku deployment). Apps like AdeptScale in Heroku might do the trick.
- Twitch API's token bucket algorithm might prevent users to continue. Working with multiple client_id's might be useful. 
I.E. each dyno might use different client_id.

