import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict

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
    work = State()
    work1 = State()
    work2 = State()


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
async def process_name(message: Message, state: FSMContext) -> None:
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
stats_level_2_study = {
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
stats_level_3_study = {
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
requirers_stats_lowyer = {"iq": 60, "insolence": 50}
requirers_stats_doctor = {"iq": 50, "physical power": 50}
requirers_stats_builder = {"iq": 30, "physical power": 50}
requirers_stats_programist = {"iq": 50, "physical power": 50}

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
    await state.update_data(study_and_play=message.text)
    await state.set_state(Form.study_and_play)
    await message.answer(
        f" Okey.\nYou choose easy level.\nYour stats{curent_stats.append(stats_level_1)},you born rich want you want to do?",
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
async def process_play(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play2=message.text)
    await state.set_state(Form.study_and_play2)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{stats_level_1_study}",
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
async def process_play(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play3=message.text)
    await state.set_state(Form.study_and_play3)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{stats_level_2_study}",
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
async def process_play(message: Message, state: FSMContext) -> None:
    await state.update_data(work=message.text)

    await state.set_state(Form.work)
    await message.answer(
        f"You study\nYou get +10 to all atributes\nYour curent state:{stats_level_3_study}\nIts time to make some money, which way will you do it?",
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


# -----------------------------------------------------------------------------------------------------#
@router.message(Form.level, F.text.casefold() == "2")
async def process_middle_level(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play=message.text)
    await state.set_state(Form.study_and_play)
    await message.answer(
        f"Okey\nYou choose middle level.{stats_level_2},you born,want want you want to do?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="play"),
                    KeyboardButton(text="study"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# -----------------------------------------------------------------------------------------------------#
@router.message(Form.level, F.text.casefold() == "3")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(study_and_play=message.text)
    await state.set_state(Form.study_and_play)
    await message.answer(
        f"Okey\nYou hard middle level.{stats_level_3},you born poor want you want to do?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="play"),
                    KeyboardButton(text="study"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.level)
async def process_unknown_write_bots(message: Message) -> None:
    await message.reply("I don't understand you :(")


# -----------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------#


@router.message(Form.study_and_play3)
async def process_work(message: Message, state: FSMContext) -> None:
    await state.update_data(work=message.text)
    await state.set_state(Form.work)
    await message.answer(
        "Its time to make some money, which way will you do it?:",
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
async def process_easy_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{stats_level_3},choose your profession",
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


@router.message(Form.work1, F.text.casefold() == "lowyer")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose lowyer.\nrequirers stats lowyer:{requirers_stats_lowyer},now you have{stats_level_3_study}",
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


@router.message(Form.work1, F.text.casefold() == "doctor")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose doctor.\nrequirers stats doctor:{requirers_stats_doctor},now you have{stats_level_3_study}",
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


@router.message(Form.work1, F.text.casefold() == "builder")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose builder.\nrequirers stats builder:{requirers_stats_builder},now you have{stats_level_3_study}",
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


@router.message(Form.work1, F.text.casefold() == "programist")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work2=message.text)
    await state.set_state(Form.work2)
    await message.answer(
        f"Okey\nYou choose programist.\nrequirers stats programist:{requirers_stats_programist},now you have{stats_level_3_study}",
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


#-----------------------------------------------------------------------------------------------------#



@router.message(Form.work2, F.text.casefold() == "back")
async def process_hard_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{stats_level_3},choose your profession",
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


@router.message(Form.work, F.text.casefold() == "illegal")
async def process_easy_level(message: Message, state: FSMContext) -> None:
    await state.update_data(work1=message.text)
    await state.set_state(Form.work1)
    await message.answer(
        f" Okey.\nYou choose legal work.\nYour stats{stats_level_3},choose your branch",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="haker"),
                    KeyboardButton(text="drugs"),
                    KeyboardButton(text="robbery"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# # -----------------------------------------------------------------------------------------------------#


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
