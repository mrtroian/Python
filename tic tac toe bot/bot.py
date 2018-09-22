from telegram import InlineKeyboardButton, InlineKeyboardMarkup, \
		InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, \
		InlineQueryHandler
from game import Game
from uuid import uuid4
import os.path as path

TOKEN = str() # Here should be your token


def start(bot, update):
	update.message.reply_text('Hi!')


def help(bot, update):
	update.message.reply_text('Help Options:\nNone\nNone\nNone')


def get_choose_markup(side = 0):
	if side is 1:
		keyboard = [[InlineKeyboardButton('play for X', callback_data='-1')]]
	elif side is 2:
		keyboard = [[InlineKeyboardButton('play for O', callback_data='-2')]]
	else:
		keyboard = [
			[InlineKeyboardButton('play for X', callback_data='-1'),
				InlineKeyboardButton('play for O', callback_data='-2'),]
			]
	return InlineKeyboardMarkup(keyboard)


def get_markup(grid):
	keyboard = [
		[InlineKeyboardButton(grid[0][0], callback_data='0'),
			InlineKeyboardButton(grid[0][1], callback_data='1'),
			InlineKeyboardButton(grid[0][2], callback_data='2')],
		[InlineKeyboardButton(grid[1][0], callback_data='3'),
			InlineKeyboardButton(grid[1][1], callback_data='4'),
			InlineKeyboardButton(grid[1][2], callback_data='5')],
		[InlineKeyboardButton(grid[2][0], callback_data='6'),
			InlineKeyboardButton(grid[2][1], callback_data='7'),
			InlineKeyboardButton(grid[2][2], callback_data='8')],
		]

	return InlineKeyboardMarkup(keyboard)


def play(bot, update):
	game = Game()
	update.message.reply_text('Play tic tac toe!', reply_markup=get_markup(game.grid))


def button(bot, update):
	query = update.callback_query
	cell = int(query.data)
	play_no = query.inline_message_id + '.json'
	player = query.from_user.username
	game = Game()

	if not path.isfile(play_no):
		game.save(play_no)
	else:
		game.resume(play_no)

	text = game.last + '\'s move' if game.last else 'Choose your side'
	result = game.declare(cell, player)
	print(update)

	if isinstance(result, bool):
		game.save(play_no)
		if game.eval() != game.NOT_OVER:
			text = player + ' won!'
		bot.edit_message_text(text, inline_message_id=query.inline_message_id, reply_markup=get_markup(game.grid))
		return
	elif isinstance(result, str):
		bot.answer_callback_query(callback_query_id=query.id, show_alert=True, text=result)
		return
	elif cell < 0:
		game.save(play_no)
		vals = game.players.values()
		i = 0
		if not 'X' in vals:
			i = 1
		elif not 'O' in vals:
			i = 2
		markup = get_choose_markup(i) if len(vals) is not 2 else get_markup(game.grid)
	else:
		markup = get_markup(game.grid)
	bot.edit_message_text(text, inline_message_id=query.inline_message_id, reply_markup=markup)


def inline_query(bot, update):
	result = list()
	game = Game()
	result.append(InlineQueryResultArticle(
		id=uuid4(),
		title="Play tic tac toe!",
		input_message_content=InputTextMessageContent('Play tic tac toe!'),
		reply_markup=get_choose_markup()
		))
	bot.answerInlineQuery(update.inline_query.id, results=result)


def echo(bot, update):
	update.message.reply_text(update.message.text)


def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', help))
	dp.add_handler(CommandHandler('play', play))
	dp.add_handler(InlineQueryHandler(inline_query))
	updater.dispatcher.add_handler(CallbackQueryHandler(button))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	try:
		main()
	except:
		exit()
