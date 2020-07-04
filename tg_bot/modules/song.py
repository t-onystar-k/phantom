import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "🎶 Put your wings on me, wings on me \n When I was so heavy \n Pour on a symphony \n When I'm low, low, low, low \n Ah, oh-ah, oh-ah \nGot me feeling drunk and high \n So high, so high🎶.",
    "🎶 You say you love me, I say you crazy \n We're nothing more than friends \n You're not my lover, more like a brother \n I known you since we were like ten, yeah...🎶",
    "🎶 Lately, I've been, I've been thinking \n I want you to be happier, I want you to be happier....  🎶", 
    "🎶 If we go down then we go down together... \n They'll say you could do anything... \n They'll say that I was clever🎶", 
    "🎶 Take me through the night \n Fall into the dark side \n We don't need the light\n We'll live on the dark side...🎶", 
    "🎶 I know it breaks your heart \n Moved to the city in a broke down car \n And four years, no calls \n Now you're looking pretty in a hotel bar...🎶", 
    "🎶I'm so alone \n Nothing feels like home \n I'm so alone \n Trying to find my way back home to you...  🎶", 
    "🎶 I'm not looking for somebody \n With some superhuman gifts \n Some superhero\n Some fairytale bliss\n Just something I can turn to \n Somebody I can kiss... 🎶", 
    "🎶 He said, One day you'll leave this world behind So live a life you will remember \n My father told me when I was just a child \n These are the nights that never die \n My father told me...🎶", 
    "🎶 So wake me up when it's all over \n When I'm wiser and I'm older \n All this time I was finding myself \n And I didn't know I was lost 🎶", 
    "🎶 Yeah, I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more \n I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more... 🎶", 
    "🎶 Then you're left in the dust \n Unless I stuck by ya \n You're a sunflower \n I think your love would be too much \n Or you'll be left in the dust \n Unless I stuck by ya \n You're the sunflower \n You're the sunflower 🎶", 
    "🎶 I love it when you call me señorita \n I wish I could pretend I didn't need ya \n But every touch is ooh la la la \n It's true, la la la \n Ooh, I should be running \n Ooh, you keep me coming for ya... 🎶", 
    "🎶 Maybe we're perfect strangers \n Maybe it's not forever \n Maybe the night will change us \n Maybe we'll stay together \n Maybe we'll walk away \n Maybe we'll realize \n We're only human \n Maybe we don't need no reason...🎶", 
    "🎶 You just want attention, you don't want my heart \n Maybe you just hate the thought of me with someone new \n Yeah, you just want attention, I knew from the start \n You're just making sure I'm never gettin' over you...🎶", 
    "🎶 Cause girls like you \n Run around with guys like me \n Til sundown, when I come through \n I need a girl like you, yeah yeah... 🎶", 
    "🎶 We don't talk anymore, we don't talk anymore \n We don't talk anymore, like we used to do \n We don't love anymore \n What was all of it for? \n oh, we don't talk anymore, like we used to do...🎶", 
    "🎶I'm in love with the shape of you \n We push and pull like a magnet do \n Although my heart is falling too \n I'm in love with your body...🎶",
    "🎶 Lately I been, I been losing sleep \n Dreaming about the things that we could be \n But baby I been, I been prayin' hard \n Said no more counting dollars \n We'll be counting stars \n Yeah, we'll be counting stars... 🎶",
  )

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /sing  ചില മലയാളം പാട്ടുകളുടെ ആദ്യ വരികൾ ലഭിക്കും.
"""

__mod_name__ = "Song Commands"

SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(SING_HANDLER)
