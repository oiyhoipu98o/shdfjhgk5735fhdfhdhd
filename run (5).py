import os
import time
from threading import Thread
from flask import Flask
from threading import Thread
from highrise import Position
from highrise.__main__ import *
from highrise.__main__ import *
import time
import traceback
import time
from highrise.models import (
    Item,
    Position,
    Reaction,
    SessionMetadata,
    User,
    AnchorPosition,
    CurrencyItem ,
)

class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


class RunBot():
  room_id = "6675aa8f840f2275e5766ca8"
  bot_token = "6e9d9483f3e23a2edcf320b9b5567a2b4df809f1d958993a75b34b283822932e"
  bot_file = "main"
  bot_class = "Bot"

  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file), self.bot_class)(),
            self.room_id, self.bot_token)
    ]  # More BotDefinition classes can be added to the definitions list

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions))

      except Exception as e:
        # Print the full traceback for the exception
        import traceback
        print("Caught an exception:")
        traceback.print_exc()  # This will print the full traceback
        time.sleep(1)
        continue

if __name__ == "__main__":
  WebServer().keep_alive()

RunBot().run_loop()