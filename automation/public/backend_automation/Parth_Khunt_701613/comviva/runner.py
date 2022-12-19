import json

import pandas as pd
from brand.app.airbnd import Airbnb
from brand.app.amazon import Amazon
from brand.app.bolt import Bolt
from brand.app.coinbase import Coinbase
from brand.app.gmail import Gmail
from brand.app.googlemeet import Googleduo
from brand.app.letshego import Letshego
from brand.app.microsoftteam import Microsoftteam
from brand.app.signal import Signal
from brand.app.skype import Skype
from brand.app.snapchat import SnapChat
from brand.app.spotify import Spotify
from brand.app.telegram import Telegram
from brand.app.tinder import Tinder
from brand.app.viber import Viber
from brand.app.vkmusic import VKMusic
from brand.app.whatsapp import WhatsApp
from brand.app.imo import Imo
from brand.app.instagram import Instagram
from brand.app.afyapap import Afyapap
from brand.app.badoo import Badoo
from brand.app.binance import Binance
from brand.app.boomplay import Boomplay
from brand.app.clubhouse import Clubhouse
from brand.app.ding import Ding
from brand.app.hooper import Hopper
from brand.app.instgramlite import Instagramlite
from brand.app.line import Line
from brand.app.linkedin import Linkedin
from brand.app.sharechat import Sharechat
from brand.app.twitter import Twitter
from brand.app.truecaller import Truecaller
from brand.app.uber import Uber
from brand.app.whtsappbusiness import WhatsAppbusiness
from brand.app.yahoo import Yahoo

from brand.web.facebook import FaceBookWeb
from brand.web.googleweb import GoogleWeb
from brand.app.vkmusic import VKMusic
from  brand.web.airbnbweb import AirbnbWeb
from  brand.web.amazonweb import AmazonWeb
from  brand.web.badooweb import BadooWeb
from  brand.web.dingweb import DingWeb
from  brand.web.groupweb import GroupWeb
from  brand.web.instagram import InstagramWeb
from  brand.web.linkdin import LinkedinWeb
from  brand.web.microsoftteamweb import MicrosoftteamWeb
from  brand.web.skypeweb import SkypeWeb
from brand.web.telegram import TelegramWeb

from  brand.web.twitterweb import TwitterWeb
from  brand.web.nimbuzzweb import NimbuzzWeb
from  brand.web.uberweb import UberWeb
from brand.web.xbet import XBetWeb
from  brand.web.yahooweb import YahooWeb
from  brand.web.youtubeweb import YoutubeWeb

from config.config import brand_file_path
from postmancode import update_recored


class Runner:

    def executeRequest(self):

        df = pd.read_excel(brand_file_path)

        user_Id = ""

        master_data = {}

        for count, i in df.iterrows():

            user_Id = df.at[0, 'Run by']

            if i['Generate OTP'] == "Y":

                if i['Brand URL'] == "-":

                    if str(i['Brand Name']).lower() == "whatsapp":
                        page_whatsapp = WhatsApp()
                        whatsapp_data = page_whatsapp.generateOTP(i['Country Code'], i['Mobile Number'])
                        whatsapp_result = {"Country Code": i['Country Code'], "Mobile Number": i['Mobile Number']}
                        whatsapp_result.update(whatsapp_data)
                        master_data.update({str(i['Brand Name']): whatsapp_result})

                    if str(i['Brand Name']).lower() == "whatsappbusiness":
                        page_whatsappbusiness = WhatsAppbusiness()
                        whatsappbusiness_data = page_whatsappbusiness.generateOTP(i['Country Code'], i['Mobile Number'])
                        whatsappbusiness_result = {"Country Code": i['Country Code'], "Mobile Number": i['Mobile Number']}
                        whatsappbusiness_result.update(whatsappbusiness_data)
                        master_data.update({str(i['Brand Name']): whatsappbusiness_result})

                    if str(i['Brand Name']).lower() == "snapchat":
                        page_snapchat = SnapChat()
                        snapchat_data = page_snapchat.generateOTP(i['Country Code'], i['Mobile Number'])
                        snapchat_result = {"Country Code": i['Country Code'], "Mobile Number": i['Mobile Number']}
                        snapchat_result.update(snapchat_data)
                        master_data.update({str(i['Brand Name']): snapchat_result})

                    if str(i['Brand Name']).lower() == "skype":
                        page_skype = Skype()
                        skype_data = page_skype.generateOTP(i['Country Code'], i['Mobile Number'])
                        skype_result = {"Country Code": i['Country Code'], "Mobile Number": i['Mobile Number']}
                        skype_result.update(skype_data)
                        master_data.update({str(i['Brand Name']): skype_result})

                    if str(i['Brand Name']).lower() == "gmail":
                        page_gmail = Gmail()
                        gmail_data = page_gmail.generateOTP(i['Mobile Number'], i['Country Code'])
                        gmail_result = {"Mobile Number": i['Mobile Number'],
                                             "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        gmail_result.update(gmail_data)
                        master_data.update({str(i['Brand Name']): gmail_result})

                    if str(i['Brand Name']).lower() == "twitter":
                        page_twitter = Twitter()
                        twitter_data = page_twitter.generateOTP(i['Mobile Number'], i['Country Code'])
                        twitter_result = {"Mobile Number": i['Mobile Number'],
                                             "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        twitter_result.update(twitter_data)
                        master_data.update({str(i['Brand Name']): twitter_result})

                    if str(i['Brand Name']).lower() == "uber":
                        page_uber = Uber()
                        uber_data = page_uber.generateOTP(i['Mobile Number'], i['Country Code'])
                        uber_result = {"Mobile Number": i['Mobile Number'],
                                          "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        uber_result.update(uber_data)
                        master_data.update({str(i['Brand Name']): uber_result})

                    if str(i['Brand Name']).lower() == "airbnb":
                        page_airbnb = Airbnb()
                        airbnb_data = page_airbnb.generateOTP(i['Mobile Number'], i['Country Code'])
                        airbnb_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        airbnb_result.update(airbnb_data)
                        master_data.update({str(i['Brand Name']): airbnb_result})

                    if str(i['Brand Name']).lower() == "hopper":
                        page_hopper = Hopper()
                        hopper_data = page_hopper.generateOTP(i['Mobile Number'], i['Country Code'])
                        hopper_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        hopper_result.update(hopper_data)
                        master_data.update({str(i['Brand Name']): hopper_result})

                    # if str(i['Brand Name']).lower() == "ding":
                    #     page_ding = Ding()
                    #     ding_data = page_ding.generateOTP(i['Country Code'], i['Mobile Number'])
                    #     ding_result = {"Mobile Number": i['Mobile Number'],
                    #                       "Device Name": i['Device Name'], "Device Id": i['Device id']}
                    #     ding_result.update(ding_data)
                    #     master_data.update({str(i['Brand Name']): ding_result})

                    if str(i['Brand Name']).lower() == "clubhouse":
                        page_cloubhouse = Clubhouse()
                        clubhouse_data = page_cloubhouse.generateOTP(i['Mobile Number'], i['Country Code'])
                        clubhouse_result = {"Mobile Number": i['Mobile Number'],
                                               "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        clubhouse_result.update(clubhouse_data)
                        master_data.update({str(i['Brand Name']): clubhouse_result})

                    if str(i['Brand Name']).lower() == "badoo":
                        page_badoo = Badoo()
                        badoo_data = page_badoo.generateOTP(i['Mobile Number'], i['Country Code'])
                        badoo_result = {"Mobile Number": i['Mobile Number'],
                                           "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        badoo_result.update(badoo_data)
                        master_data.update({str(i['Brand Name']): badoo_result})

                    if str(i['Brand Name']).lower() == "afyapap":
                        page_afyapap = Afyapap()
                        afyapap_data = page_afyapap.generateOTP(i['Mobile Number'], i['Country Code'])
                        afyapap_result = {"Mobile Number": i['Mobile Number'],
                                             "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        afyapap_result.update(afyapap_data)
                        master_data.update({str(i['Brand Name']): afyapap_result})


                    if str(i['Brand Name']).lower() == "boomplay":
                        page_boomplay = Boomplay()
                        boomplay_data = page_boomplay.generateOTP(i['Mobile Number'], i['Country Code'])
                        boomplay_result = {"Mobile Number": i['Mobile Number'],
                                              "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        boomplay_result.update(boomplay_data)
                        master_data.update({str(i['Brand Name']): boomplay_result})

                    if str(i['Brand Name']).lower() == "instagramlite":
                        page_instagramlite = Instagramlite()
                        instagramlite_data = page_instagramlite.generateOTP(i['Mobile Number'], i['Country Code'])
                        instagramlite_result = {"Mobile Number": i['Mobile Number'],
                                                "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        instagramlite_result.update(instagramlite_data)
                        master_data.update({str(i['Brand Name']): instagramlite_result})

                    if str(i['Brand Name']).lower() == "truecaller":
                        page_truecaller = Truecaller()
                        truecaller_data = page_truecaller.generateOTP(i['Mobile Number'], i['Country Code'])
                        truecaller_result = {"Mobile Number": i['Mobile Number'],
                                             "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        truecaller_result.update(truecaller_data)
                        master_data.update({str(i['Brand Name']): truecaller_result})

                    if str(i['Brand Name']).lower() == "linkedin":
                        page_linkedin = Linkedin()
                        linkedin_data = page_linkedin.generateOTP(i['Mobile Number'], i['Country Code'])
                        linkedin_result = {"Mobile Number": i['Mobile Number'],
                                              "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        linkedin_result.update(linkedin_data)
                        master_data.update({str(i['Brand Name']): linkedin_result})

                    if str(i['Brand Name']).lower() == "microsoftteam":
                        page_microsoftteam = Microsoftteam()
                        microsoftteam_data = page_microsoftteam.generateOTP(i['Mobile Number'], i['Country Code'])
                        microsoftteam_result = {"Mobile Number": i['Mobile Number'],
                                              "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        microsoftteam_result.update(microsoftteam_data)
                        master_data.update({str(i['Brand Name']): page_microsoftteam})

                    if str(i['Brand Name']).lower() == "binance":
                        page_binance = Binance()
                        binance_data = page_binance.generateOTP(i['Country Code'], i['Mobile Number'])
                        binance_result = {"Mobile Number": i['Mobile Number'],
                                          "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        binance_result.update(binance_data)
                        master_data.update({str(i['Brand Name']): binance_result})

                    if str(i['Brand Name']).lower() == "imo":
                        page_imo = Imo()
                        imo_data = page_imo.generateOTP(i['Mobile Number'], i['Country Code'])
                        imo_result = {"Mobile Number": i['Mobile Number'],
                                         "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        imo_result.update(imo_data)
                        master_data.update({str(i['Brand Name']): imo_result})

                    if str(i['Brand Name']).lower() == "instagram":
                        page_instagram = Instagram()
                        instagram_data = page_instagram.generateOTP(i['Mobile Number'], i['Country Code'])
                        instagram_result = {"Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        instagram_result.update(instagram_data)
                        master_data.update({str(i['Brand Name']): instagram_result})

                    if str(i['Brand Name']).lower() == "line":
                        page_line = Line()
                        line_data = page_line.generateOTP(i['Mobile Number'],i['Country Code'])
                        line_result = {"Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        line_result.update(line_data)
                        master_data.update({str(i['Brand Name']): line_result})

                    if str(i['Brand Name']).lower() == "sharechat":
                        page_sharechat = Sharechat()
                        sharechat_data = page_sharechat.generateOTP(i['Brand URL'], i['Mobile Number'])
                        sharechat_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        sharechat_result.update(sharechat_data)
                        master_data.update({str(i['Brand Name']): sharechat_result})

                    if str(i['Brand Name']).lower() == "bemydate":
                        page_sharechat = Sharechat()
                        sharechat_data = page_sharechat.generateOTP(i['Brand URL'], i['Mobile Number'])
                        sharechat_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        sharechat_result.update(sharechat_data)
                        master_data.update({str(i['Brand Name']): sharechat_result})

                    if str(i['Brand Name']).lower() == "vkmusic":
                        page_vkmusic = VKMusic()
                        vkmusic_data = page_vkmusic.generateOTP(i['Country Code'], i['Mobile Number'])
                        vkmusic_result = {"Country Code": i['Country Code'], "Mobile Number": i['Mobile Number']}
                        vkmusic_result.update(vkmusic_data)
                        master_data.update({str(i['Brand Name']): vkmusic_result})

                    if str(i['Brand Name']).lower() == "tinder":
                        page_tinder = Tinder()
                        tinder_data = page_tinder.generateOTP(i['Mobile Number'], i['Country Code'])
                        tinder_result = {"Mobile Number": i['Mobile Number'],
                                         "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        tinder_result.update(tinder_data)
                        master_data.update({str(i['Brand Name']): tinder_result})

                    if str(i['Brand Name']).lower() == "telegram":
                        page_telegram = Telegram()
                        telegram_data = page_telegram.generateOTP(i['Mobile Number'], i['Country Code'])
                        telegram_result = {"Mobile Number": i['Mobile Number'],
                                         "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        telegram_result.update(telegram_data)
                        master_data.update({str(i['Brand Name']): telegram_result})

                    if str(i['Brand Name']).lower() == "letshego":
                        page_letshego = Letshego()
                        letshego_data = page_letshego.generateOTP(i['Mobile Number'], i['Country Code'])
                        letshego_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        letshego_result.update(letshego_data)
                        master_data.update({str(i['Brand Name']): letshego_result})

                    if str(i['Brand Name']).lower() == "spotify":
                        page_spotify = Spotify()
                        spotify_data = page_spotify.generateOTP(i['Mobile Number'], i['Country Code'])
                        spotify_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        spotify_result.update(spotify_data)
                        master_data.update({str(i['Brand Name']): spotify_result})

                    if str(i['Brand Name']).lower() == "coinbase":
                        page_coinbase = Coinbase()
                        coinbase_data = page_coinbase.generateOTP(i['Mobile Number'], i['Country Code'])
                        coinbase_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        coinbase_result.update(coinbase_data)
                        master_data.update({str(i['Brand Name']): coinbase_result})

                    if str(i['Brand Name']).lower() == "googleduo":
                        page_googleduo = Googleduo()
                        googleduo_data = page_googleduo.generateOTP(i['Mobile Number'], i['Country Code'])
                        googleduo_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        googleduo_result.update(googleduo_data)
                        master_data.update({str(i['Brand Name']): googleduo_result})

                    if str(i['Brand Name']).lower() == "signal":
                        page_signal = Signal()
                        signal_data = page_signal.generateOTP(i['Mobile Number'], i['Country Code'])
                        signal_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        signal_result.update(signal_data)
                        master_data.update({str(i['Brand Name']): signal_result})

                    if str(i['Brand Name']).lower() == "viber":
                        page_viber = Viber()
                        viber_data = page_viber.generateOTP(i['Mobile Number'], i['Country Code'])
                        viber_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        viber_result.update(viber_data)
                        master_data.update({str(i['Brand Name']): viber_result})

                    if str(i['Brand Name']).lower() == "yahoo":
                        page_yahoo = Yahoo()
                        yahoo_data = page_yahoo.generateOTP(i['Mobile Number'], i['Country Code'])
                        yahoo_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        yahoo_result.update(yahoo_data)
                        master_data.update({str(i['Brand Name']): yahoo_result})

                    if str(i['Brand Name']).lower() == "bolt":
                        page_bolt = Bolt()
                        bolt_data = page_bolt.generateOTP(i['Mobile Number'], i['Country Code'])
                        bolt_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        bolt_result.update(bolt_data)
                        master_data.update({str(i['Brand Name']): bolt_result})

                    if str(i['Brand Name']).lower() == "amazon":
                        page_amazon = Amazon()
                        amazon_data = page_amazon.generateOTP(i['Mobile Number'], i['Country Code'])
                        amazon_result = {"Mobile Number": i['Mobile Number'],
                                            "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        amazon_result.update(amazon_data)
                        master_data.update({str(i['Brand Name']): amazon_result})




                else:

                    if str(i['Brand Name']).lower() == "facebook":
                        page_telegram = FaceBookWeb()
                        telegram_data = page_telegram.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        telegram_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        telegram_result.update(telegram_data)
                        master_data.update({str(i['Brand Name']): telegram_result})

                    if str(i['Brand Name']).lower() == "google":
                        page_google = GoogleWeb()
                        google_data = page_google.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        google_result = {"Brand URL": i['Brand URL'], "Mobile Numer": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id'], "Run by": i['Run by']}
                        google_result.update(google_data)
                        master_data.update({str(i['Brand Name']): google_result})

                    if str(i['Brand Name']).lower() == "instagram":
                        page_instagram = InstagramWeb()
                        instagram_data = page_instagram.generateOTP(i['Brand URL'], i['Mobile Number'], i['Country Code'])
                        instagram_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        instagram_result.update(instagram_data)
                        master_data.update({str(i['Brand Name']+"Web"): instagram_result})

                    if str(i['Brand Name']).lower() == "twitter":
                        page_twitter = TwitterWeb()
                        twitter_data = page_twitter.generateOTP(i['Brand URL'],i['Mobile Number'],i['Country Code'])
                        twitter_result = {"Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        twitter_result.update(twitter_data)
                        master_data.update({str(i['Brand Name']): twitter_result})

                    if str(i['Brand Name']).lower() == "uber":
                        page_uber = UberWeb()
                        uber_data = page_uber.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        uber_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        uber_result.update(uber_data)
                        master_data.update({str(i['Brand Name']): uber_result})

                    if str(i['Brand Name']).lower() == "linkedin":
                        page_linkedin = LinkedinWeb()
                        linkedin_data = page_linkedin.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        linkedin_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        linkedin_result.update(linkedin_data)
                        master_data.update({str(i['Brand Name']): linkedin_result})

                    if str(i['Brand Name']).lower() == "microsoftteam":
                        page_microsoftteam = MicrosoftteamWeb()
                        microsoftteam_data = page_microsoftteam.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        microsoftteam_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        microsoftteam_result.update(microsoftteam_data)
                        master_data.update({str(i['Brand Name']): microsoftteam_result})

                    if str(i['Brand Name']).lower() == "airbnb":
                        page_airbnb = AirbnbWeb()
                        airbnb_data = page_airbnb.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        airbnb_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        airbnb_result.update(airbnb_data)
                        master_data.update({str(i['Brand Name']): airbnb_result})

                    if str(i['Brand Name']).lower() == "nimbuzz":
                        page_nimbuzz = NimbuzzWeb()
                        nimbuzz_data = page_nimbuzz.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        nimbuzz_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        nimbuzz_result.update(nimbuzz_data)
                        master_data.update({str(i['Brand Name']): nimbuzz_result})

                    if str(i['Brand Name']).lower() == "yahoo":
                        page_yahoo = YahooWeb()
                        yahoo_data = page_yahoo.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        yahoo_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        yahoo_result.update(yahoo_data)
                        master_data.update({str(i['Brand Name']): yahoo_result})


                    if str(i['Brand Name']).lower() == "amazon":
                        page_amazon = AmazonWeb()
                        amazon_data = page_amazon.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        amazon_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        amazon_result.update(amazon_data)
                        master_data.update({str(i['Brand Name']): amazon_result})

                    if str(i['Brand Name']).lower() == "group":
                        page_group = GroupWeb()
                        group_data = page_group.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        group_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        group_result.update(group_data)
                        master_data.update({str(i['Brand Name']): group_result})

                    if str(i['Brand Name']).lower() == "skype":
                        page_skype = SkypeWeb()
                        skype_data = page_skype.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        skype_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        skype_result.update(skype_data)
                        master_data.update({str(i['Brand Name']): skype_result})

                    if str(i['Brand Name']).lower() == "badoo":
                        page_badoo = BadooWeb()
                        badoo_data = page_badoo.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        badoo_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        badoo_result.update(badoo_data)
                        master_data.update({str(i['Brand Name']): badoo_result})

                    if str(i['Brand Name']).lower() == "youtube":
                        page_youtube = YoutubeWeb()
                        youtube_data = page_youtube.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        youtube_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        youtube_result.update(youtube_data)
                        master_data.update({str(i['Brand Name']): youtube_result})


                    if str(i['Brand Name']).lower() == "ding":
                        page_ding = DingWeb()
                        ding_data = page_ding.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        ding_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        ding_result.update(ding_data)
                        master_data.update({str(i['Brand Name']+"Web"): ding_result})

                    # if str(i['Brand Name']).lower() == "telegram":
                    #     page_telegram = TelegramWeb()
                    #     telegram_data = page_telegram.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                    #     telegram_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                    #               "Device Name": i['Device Name'], "Device Id": i['Device id']}
                    #     telegram_result.update(telegram_data)
                    #     master_data.update({str(i['Brand Name']+"Web"): telegram_result})

                    if str(i['Brand Name']).lower() == "xbet":
                        page_xbet = XBetWeb()
                        xbet_data = page_xbet.generateOTP(i['Brand URL'], i['Mobile Number'],i['Country Code'])
                        xbet_result = {"Brand URL": i['Brand URL'], "Mobile Number": i['Mobile Number'],
                                  "Device Name": i['Device Name'], "Device Id": i['Device id']}
                        xbet_result.update(xbet_data)
                        master_data.update({str(i['Brand Name']+"Web"): xbet_result})


        automation_brand_data = {"Parth_Khunt_701613": [master_data]}
        json_object = json.dumps(automation_brand_data, indent=4)
        print(automation_brand_data)

        update_recored(automation_brand_data, user_Id)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        return True


otpRunner = Runner()
otpRunner.executeRequest()
