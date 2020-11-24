import discord

from .helper import Letter, Symbol

class ThreatLevelMenu():
    def __init__(self, welcome):
        self.menu = {
    "main": {
        "embed": welcome.embed(title="Welcome", color=discord.Color.orange(),
                       description="Welcome to the **Threat Level** Server, {0.mention}! "
                                   "We are one of the oldest and biggest families in "
                                   "Clash Royale with our 700 members and 15 clans! "
                                   "<a:goblinstab:468708996153475072>\n\n"
                                   "We are glad you joined us, can we ask a few questions "
                                   "to customize your experience?"),
        "thumbnail": "https://i.imgur.com/8SRsdQz.png",
        "options": [
            {
                "name": "Yes please!",
                "emoji": Letter.a,
                "execute": {
                    "menu": "refferal_menu"
                }
            },
            {
                "name": "Skip it, and talk to our friendly staff.",
                "emoji": Letter.b,
                "execute": {
                    "menu": "leave_alone"
                }
            }
        ],
        "go_back": False
    },
    "refferal_menu": {
        "embed": welcome.embed(title="How did you get here?", color=discord.Color.orange(),
                       description="We know you are from the interwebz. "
                                   "But where exactly did you find us?"),
        "options": [
            {
                "name": "Legend Website",
                "emoji": Letter.a,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "RoyaleAPI Website",
                "emoji": Letter.b,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "Reddit",
                "emoji": Letter.c,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "Discord",
                "emoji": Letter.d,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "Twitter",
                "emoji": Letter.e,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "From in-game",
                "emoji": Letter.f,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "Friend or Family",
                "emoji": Letter.g,
                "execute": {
                    "menu": "location_menu"
                }
            },
            {
                "name": "Other",
                "emoji": Letter.h,
                "execute": {
                    "menu": "location_menu"
                }
            }
        ],
        "go_back": True,
        "track": True
    },
    "location_menu": {
        "embed": welcome.embed(title="What part of the world do you come from?", color=discord.Color.orange(),
                       description="To better serve you, "
                                   "pick the region you currently live in."),
        "options": [
            {
                "name": "North America",
                "emoji": Letter.a,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "South America",
                "emoji": Letter.b,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Northern Africa",
                "emoji": Letter.c,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Southern Africa",
                "emoji": Letter.d,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Europe",
                "emoji": Letter.e,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Middle East",
                "emoji": Letter.f,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Asia",
                "emoji": Letter.g,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Southeast Asia",
                "emoji": Letter.h,
                "execute": {
                    "menu": "age_menu"
                }
            },
            {
                "name": "Australia",
                "emoji": Letter.i,
                "execute": {
                    "menu": "age_menu"
                }
            }
        ],
        "go_back": True,
        "track": True
    },
    "age_menu": {
        "embed": welcome.embed(title="How old are you?", color=discord.Color.orange(),
                       description="Everyone is welcome! "
                                   "However, some clans do require you to be of a"
                                   " certain age group. Please pick one."),
        "options": [
            {
                "name": "Under 16",
                "emoji": Letter.a,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "16-20",
                "emoji": Letter.b,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "21-30",
                "emoji": Letter.c,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "31-40",
                "emoji": Letter.d,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "41-50",
                "emoji": Letter.e,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "51-60",
                "emoji": Letter.f,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "61 or Above",
                "emoji": Letter.g,
                "execute": {
                    "menu": "save_tag_menu"
                }
            },
            {
                "name": "Prefer Not to Answer",
                "emoji": Letter.h,
                "execute": {
                    "menu": "save_tag_menu"
                }
            }
        ],
        "go_back": True,
        "track": True
    },
    "save_tag_menu": {
        "embed": welcome.embed(title="What is your Clash Royale player tag?", color=discord.Color.orange(),
                       description="Before we let you talk in the server, we need to take a look at your stats. "
                                   "To do that, we need your Clash Royale player tag.\n\n"),
        "options": [
            {
                "name": "Continue",
                "emoji": Letter.a,
                "execute": {
                    "menu": "save_tag"
                }
            },
            {
                "name": "I don't play Clash Royale",
                "emoji": Letter.b,
                "execute": {
                    "function": "guest"
                }
            }
        ],
        "go_back": True
    },
    "save_tag": {
        "embed": welcome.embed(title="Type in your tag", color=discord.Color.orange(),
                       description="Please type **!savetag #YOURTAG** below to submit your ID.\n\n"
                                   "You can find your player tag in your profile in game."),
        "image": "https://legendclans.com/wp-content/uploads/2017/11/profile_screen3.png",
        "options": [],
        "go_back": True
    },
    "choose_path": {
        "embed": welcome.embed(title="So, why are you here?", color=discord.Color.orange(),
                       description="Please select your path "
                                   "below to get started."),
        "options": [
            {
                "name": "I am just visiting.",
                "emoji": Letter.a,
                "execute": {
                    "function": "guest"
                }
            },
            {
                "name": "I want to join a clan.",
                "emoji": Letter.b,
                "execute": {
                    "menu": "join_clan"
                }
            },
            {
                "name": "I am already in one of your clans.",
                "emoji": Letter.c,
                "execute": {
                    "function": "verify_membership"
                }
            }
        ],
        "go_back": False,
        "track": True
    },
    "join_clan": {
        "embed": welcome.embed(title="Legend Family Clans", color=discord.Color.orange(),
                       description="Here are all our clans, which clan do you prefer?"),
        "dynamic_options": "clans_options",
        "options": [],
        "go_back": True,
        "track": True
    },
    "end_member": {
        "embed": welcome.embed(title="That was it", color=discord.Color.orange(),
                       description="Your chosen clan has been informed. "
                                   " Please wait in #welcome-gate channel "
                                   "while a discord officer comes to approve you.\n\n"
                                   " Please do not join any clans without talking to an officer.\n\n"
                                   "**Enjoy your stay!**"),
        "options": [
            {
                "name": "Go to #welcome-gate",
                "emoji": Letter.a,
                "execute": {
                    "menu": "welcome_gate"
                }
            }
        ],
        "go_back": False,
        "finished": True
    },
    "end_human": {
        "embed": welcome.embed(title="Requesting assistance", color=discord.Color.orange(),
                       description="We have notified our officers about your information."
                                   " Please wait in #welcome-gate "
                                   "channel while an officer comes and helps you.\n\n"
                                   " Please do not join any clans without talking to an officer.\n\n"
                                   "**Enjoy your stay!**"),
        "options": [
            {
                "name": "Go to #welcome-gate",
                "emoji": Letter.a,
                "execute": {
                    "menu": "welcome_gate"
                }
            }
        ],
        "go_back": False,
        "finished": True
    },
    "end_guest": {
        "embed": welcome.embed(title="Enjoy your stay", color=discord.Color.orange(),
                       description="Welcome to the **Legend Family** Discord server. "
                       "If you would like guest role, please ping any of officer in #visitor-guest-welcome."
                       "Thanks + enjoy!\n"),
        "options": [],
        "go_back": False,
        "finished": True
    },
    "give_tags": {
        "embed": welcome.embed(title="Membership verified", color=discord.Color.orange(),
                       description="We have unlocked all member channels for you, enjoy your stay!"),
        "options": [
            {
                "name": "Go to #global-chat",
                "emoji": Letter.a,
                "execute": {
                    "menu": "global_chat"
                }
            }
        ],
        "go_back": False,
        "finished": True
    },
    "leave_alone": {
        "embed": welcome.embed(title="Enjoy your stay", color=discord.Color.orange(),
                       description="We look forward to welcoming "
                                   "you into the Legend Clan Family!\n\n"
                                   "You can go talk to an officer in #welcome-gate. "),
        "options": [
            {
                "name": "Go to #welcome-gate",
                "emoji": Letter.a,
                "execute": {
                    "menu": "welcome_gate"
                }
            }
        ],
        "go_back": False,
        "finished": True
    },
    "global_chat": {
        "embed": welcome.embed(title="#global-chat", color=discord.Color.orange(),
                       description="Click here: https://discord.gg/T7XdjFS"),
        "options": [
            {
                "name": "Done",
                "emoji": Symbol.white_check_mark,
                "execute": {}
            }
        ],
        "go_back": False,
        "hide_options": True
    },
    "welcome_gate": {
        "embed": welcome.embed(title="#welcome-gate", color=discord.Color.orange(),
                       description="Click here: https://discord.gg/yhD84nK"),
        "options": [
            {
                "name": "Done",
                "emoji": Symbol.white_check_mark,
                "execute": {}
            }
        ],
        "go_back": False,
        "hide_options": True
    }
}