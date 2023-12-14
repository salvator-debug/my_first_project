import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from random import randint
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

TOKEN = getenv("6897293959:AAGYqbQ0-UP4TkTSf_m7XN3ZI8fDwWQU3jc")

router = Router()


class Form(StatesGroup):
    name = State()
    level = State()
    study_and_play = State()
    study_and_play2 = State()
    study_and_play3 = State()
    study_and_play4 = State()
    study_and_play5 = State()
    work = State()
    work1 = State()
    work2 = State()
    work3 = State()
    work4 = State()
    work5 = State()
    illegal = State()
    illegal1 = State()
    illegal2 = State()
    illegal3 = State()
    illegal4 = State()
    illegal5 = State()


curent_stats = []


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.name)
    await message.answer(
        "hello, welcome to simulator real life, under which name you want to born?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.name)
async def choose_level(message: Message, state: FSMContext) -> None:
    await state.update_data(level=message.text)
    await state.set_state(Form.level)
    await message.answer(
        f"Nice to meet you, {html.quote(message.text)}!\nchose your level of hardcore",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="1"),
                    KeyboardButton(text="2"),
                    KeyboardButton(text="3"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


stats_level_1 = {
    "iq": 20,
    "physical power": 20,
    "knowledge": {
        "chemistry": 20,
        "math": 20,
        "physics": 20,
        "literature": 20,
        "geography": 20,
    },
}

stats_level_1_study = {
    "iq": 30,
    "physical power": 30,
    "knowledge": {
        "chemistry": 30,
        "math": 30,
        "physics": 30,
        "literature": 30,
        "geography": 30,
    },
}
stats_level_1_study2 = {
    "iq": 40,
    "physical power": 40,
    "knowledge": {
        "chemistry": 40,
        "math": 40,
        "physics": 40,
        "literature": 40,
        "geography": 40,
    },
}
stats_level_1_study3 = {
    "iq": 50,
    "physical power": 50,
    "knowledge": {
        "chemistry": 50,
        "math": 50,
        "physics": 50,
        "literature": 50,
        "geography": 50,
    },
}
stats_level_1_study4 = {
    "iq": 60,
    "physical power": 60,
    "knowledge": {
        "chemistry": 60,
        "math": 60,
        "physics": 60,
        "literature": 60,
        "geography": 60,
    },
}
list_of_stats = [
    stats_level_1_study,
    stats_level_1_study2,
    stats_level_1_study3,
    stats_level_1_study4,
]
curent_stats = []

requirers_stats_lowyer = {"iq": 60, "insolence": 50}
requirers_stats_doctor = {"iq": 50, "physical power": 50}
requirers_stats_builder = {"iq": 30, "physical power": 50}
requirers_stats_programist = {"iq": 50, "math": 50}
requirers_stats_haker = {"iq": 60, "math": 50}
requirers_stats_selldrugs = {"iq": 50, "physical power": 50}
requirers_stats_robbery = {"iq": 30, "physical power": 50}


stats_level_2 = {
    "iq": 10,
    "physical power": 10,
    "knowledge": {
        "chemistry": 10,
        "math": 10,
        "physics": 10,
        "literature": 10,
        "geography": 10,
    },
}
stats_level_3 = {
    "iq": 0,
    "physical power": 0,
    "knowledge": {
        "chemistry": 0,
        "math": 0,
        "physics": 0,
        "literature": 0,
        "geography": 0,
    },
}


# -----------------------------------------------------------------------------------------------------#
@router.message(Form.level, F.text.casefold() == "1")
async def process_easy_level(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1]
    await state.update_data(study_and_play=message.text)
    await state.set_state(Form.study_and_play)
    await message.answer(
        f" Okey.\nYou choose easy level.\nYour stats{curent_stats},you born rich want you want to do?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="study"),
                    KeyboardButton(text="play"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play, F.text.casefold() == "play")
async def process_play(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play2=message.text)
    await state.set_state(Form.study_and_play2)
    await message.answer(
        f"You play\nYou get nothing\nYou are 15",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="study"),
                    KeyboardButton(text="play"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play, F.text.casefold() == "study")
async def process_study(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study]
    await state.update_data(study_and_play2=message.text)
    await state.set_state(Form.study_and_play2)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{curent_stats}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="study"),
                    KeyboardButton(text="play"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play2, F.text.casefold() == "play")
async def process_play2(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play3=message.text)
    await state.set_state(Form.study_and_play3)
    await message.answer(
        f"You play\nYou get nothing\nYou are 30",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="study"),
                    KeyboardButton(text="play"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play2, F.text.casefold() == "study")
async def process_study2(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study2]
    await state.update_data(study_and_play3=message.text)
    await state.set_state(Form.study_and_play3)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{curent_stats}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="study"),
                    KeyboardButton(text="play"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play3, F.text.casefold() == "play")
async def process_play3(message: Message, state: FSMContext) -> None:
    await state.update_data(work=message.text)
    await state.set_state(Form.work)
    await message.answer(
        f"You play\nYou get nothing\nYou are 45\nIts time to make some money, which way will you do it?:",
        reply_markup=ReplyKeyboardRemove(
            keyboard=[
                [
                    KeyboardButton(text="legal"),
                    KeyboardButton(text="illegal"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play3, F.text.casefold() == "study")
async def process_study3(message: Message, state: FSMContext) -> None:
    await state.update_data(work=message.text)
    curent_stats = [stats_level_1_study3]
    await state.set_state(Form.work)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{curent_stats}\nIts time to make some money, which way will you do it?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="legal"),
                    KeyboardButton(text="illegal"),
                    KeyboardButton(text="study more"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work, F.text.casefold() == "study more")
async def process_study4(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study4]
    await state.update_data(study_and_play3=message.text)
    await state.set_state(Form.study_and_play3)
    await message.answer(
        f" You study\nYou get +10 to all atributes.\nYour stats{curent_stats}\nIts time to make some money, which way will you do it?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="legal"),
                    KeyboardButton(text="illegal"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# ---------------------------------------------------------------------------------------#
@router.message(Form.work, F.text.casefold() == "legal")
async def process_legal(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study3]
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{curent_stats},choose your profession",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="programist"),
                    KeyboardButton(text="lowyer"),
                    KeyboardButton(text="doctor"),
                    KeyboardButton(text="builder"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play3, F.text.casefold() == "legal")
async def process_legal(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study4]
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{curent_stats},choose your profession",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="programist"),
                    KeyboardButton(text="lowyer"),
                    KeyboardButton(text="doctor"),
                    KeyboardButton(text="builder"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work1, F.text.casefold() == "programist")
async def programist(message: Message, state: FSMContext) -> None:
    # тут я хотів створити змінну curent stats щоб знати скільки людина провчилася і перевірити але через це програма не йшла далі
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose programist.\nrequirers stats programist:{requirers_stats_programist},now you have{stats_level_1_study3}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="back"),
                    KeyboardButton(text="study for programist"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work2, F.text.casefold() == "study for programist")
async def study_for_programist(message: Message, state: FSMContext) -> None:
    await state.update_data(work3=message.text)
    await state.set_state(Form.work3)
    await message.answer(
        f"You worked hard and die happy\nTHE END",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work3, F.text.casefold() == "start again")
async def restart(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.name)
    await message.answer(
        "hello, welcome to simulator real life, under which name you want to born?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.work1, F.text.casefold() == "lowyer")
async def lowyer(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose lowyer.\nrequirers stats lowyer:{requirers_stats_lowyer},now you have{stats_level_1_study4}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="back"),
                    KeyboardButton(text="study for lowyer"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work2, F.text.casefold() == "study for lowyer")
async def study_for_lowyer(message: Message, state: FSMContext) -> None:
    await state.update_data(work3=message.text)
    await state.set_state(Form.work3)
    await message.answer(
        f"Okey\nYou choose study for lowyer,are you have insolence?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Yes"),
                    KeyboardButton(text="No"),
                    KeyboardButton(text="you can't put insolence in your pocket"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work3, F.text.casefold() == "yes")
async def yes(message: Message, state: FSMContext) -> None:
    await state.update_data(work4=message.text)
    await state.set_state(Form.work4)
    await message.answer(
        f"You worked hard and die happy\nTHE END",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work3, F.text.casefold() == "no")
async def no(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study3]
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{curent_stats},choose your profession",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="programist"),
                    KeyboardButton(text="doctor"),
                    KeyboardButton(text="builder"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(
    Form.work3, F.text.casefold() == "you can't put insolence in your pocket"
)
async def yes(message: Message, state: FSMContext) -> None:
    await state.update_data(work4=message.text)
    await state.set_state(Form.work4)
    await message.answer(
        f"You worked hard and die happy\nTHE END",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work4, F.text.casefold() == "start again")
async def restart(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.name)
    await message.answer(
        "hello, welcome to simulator real life, under which name you want to born?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.work1, F.text.casefold() == "doctor")
async def doctor(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose doctor.\nrequirers stats doctor:{requirers_stats_builder},now you have{stats_level_1_study3}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="back"),
                    KeyboardButton(text="study for doctor"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work2, F.text.casefold() == "study for doctor")
async def study_for_doctor(message: Message, state: FSMContext) -> None:
    await state.update_data(work3=message.text)
    await state.set_state(Form.work3)
    await message.answer(
        f"You worked hard and die happy\nTHE END",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work1, F.text.casefold() == "builder")
async def builder(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose builder.\nrequirers stats builder:{requirers_stats_builder},now you have{stats_level_1_study3}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="back"),
                    KeyboardButton(text="study for builder"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.work2, F.text.casefold() == "study for builder")
async def study_for_builder(message: Message, state: FSMContext) -> None:
    await state.update_data(work3=message.text)
    await state.set_state(Form.work3)
    await message.answer(
        f"You worked hard and die happy\nTHE END",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# -----------------------------------------------------------------------------------------------------#


@router.message(Form.work2, F.text.casefold() == "back")
async def back(message: Message, state: FSMContext) -> None:
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{stats_level_1_study3},choose your profession",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="programist"),
                    KeyboardButton(text="lowyer"),
                    KeyboardButton(text="doctor"),
                    KeyboardButton(text="builder"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# # -----------------------------------------------------------------------------------------------------#
@router.message(Form.work, F.text.casefold() == "illegal")
async def illegal(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study3]
    await state.update_data(illegal1=message.text)
    await state.set_state(Form.illegal1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{curent_stats},choose your branch",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="haker"),
                    KeyboardButton(text="illegal trade"),
                    KeyboardButton(text="robbery"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.study_and_play3, F.text.casefold() == "illegal")
async def illegal(message: Message, state: FSMContext) -> None:
    curent_stats = [stats_level_1_study4]
    await state.update_data(illegal1=message.text)
    await state.set_state(Form.illegal1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{curent_stats},choose your profession",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="haker"),
                    KeyboardButton(text="illegal trade"),
                    KeyboardButton(text="robber"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal1, F.text.casefold() == "illegal trade")
async def illegal_trade(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal2=message.text)
    await state.set_state(Form.illegal2)
    await message.answer(
        f"Okey\nYou choose haker.\nrequirers stats doctor:{requirers_stats_haker},now you have{stats_level_1_study4}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="sell weapon"),
                    KeyboardButton(text="sell drugs"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "sell weapon")
async def sell_weapon(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "sell drugs")
async def sell_drugs(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal1, F.text.casefold() == "robber")
async def robber(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal2=message.text)
    await state.set_state(Form.illegal2)
    await message.answer(
        f"Okey\nYou choose haker.\nrequirers stats doctor:{requirers_stats_haker},now you have{stats_level_1_study4}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="robbery"),
                    KeyboardButton(text="break the bank"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "robbery")
async def robbery(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "break the bank")
async def break_the_bank(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal1, F.text.casefold() == "haker")
async def haker(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal2=message.text)
    await state.set_state(Form.illegal2)
    await message.answer(
        f"Okey\nYou choose haker.\nrequirers stats doctor:{requirers_stats_haker},now you have{stats_level_1_study4}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="fishing"),
                    KeyboardButton(text="ddos-attack"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "fishing")
async def fishing(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal2, F.text.casefold() == "ddos-attack")
async def ddos_attack(message: Message, state: FSMContext) -> None:
    await state.update_data(illegal3=message.text)
    await state.set_state(Form.illegal3)
    hhh = []
    hhh.append(randint(1, 2))
    if 1 in hhh:
        consequence = " worked hard and die happy\nTHE END"
    if 2 in hhh:
        consequence = " worked hard and die in the jail\nTHE END"
    await message.answer(
        f"Okey\nYou{consequence}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="start again"),
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.illegal3, F.text.casefold() == "start again")
async def restart(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.name)
    await message.answer(
        "hello, welcome to simulator real life, under which name you want to born?",
        reply_markup=ReplyKeyboardRemove(),
    )


async def main():
    bot = Bot(
        token="6897293959:AAGYqbQ0-UP4TkTSf_m7XN3ZI8fDwWQU3jc",
        parse_mode=ParseMode.HTML,
    )
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
