from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Monokuma",
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3',
logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'])

conversation = [
   "Oi",
   "Olá",
   "Tudo bem?",
   "Tudo sim",
   "Qual o seu nome?",
   "Monokuma"
]

trainer = ListTrainer(bot)
trainer.train(conversation)