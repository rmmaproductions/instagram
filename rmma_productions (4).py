#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="rmma_productions", password="PASSWORD_AQUI",
               like_per_day=1800, # How many likes set bot in one day.
               comments_per_day=0,
	          tag_list=['manchester','brighton','londonmusic','roundhouse','staplescenter','o2','madisonsquaregarden','musicfestival','musician','musicbox','musicvideos','recordingartist','manchesterarena','theforum','rodlaverarena','barclayscenter','berlin','london','madrid','barcelona','miami','losangeles', 'paris','tokyo','amsterdam','oslo','selfie','california','newyork', 'music', 'spotify','spotifypremium','concert','liveshow', 'liveperformance', 'musicianlife', 'musicians', 'musiclife', 'musiclovers','guitar','piano','guitarist','pianist','violin','violinist','drummer','dj','rockstar','rock','pop','singer','singersongwriter','cover','vocalist','vocals','hiphop', 'playlist','songs','gig','liveshow','spotifyplaylist','edm','edmlifestyle'],
               max_like_for_one_tag=5, # maximum likes on one tag in a row
               media_max_like=5, # Don't like if media have more than n likes.
               media_min_like=0, # Don't like if media have less than n likes.
               follow_per_day=150,
               follow_time=12*60*60, # how long in seconds we are going to follow them for
               unfollow_per_day=130,
               unfollow_break_min=15, # Minimum seconds for unfollow break pause
               unfollow_break_max=30, # Maximum seconds for unfollow break pause
               log_mod=0) # log_mod = 0 log to console, log_mod = 1 log to file, log_mod = 2 no log

bot.new_auto_mod()
