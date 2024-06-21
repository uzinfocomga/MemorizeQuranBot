from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _
from icecream import ic

from tgbot.keyboards.inline import go_back_keyboard
from tgbot.misc.init import cmc_client

user_stats_router = Router()


@user_stats_router.callback_query(F.data == "user_stats")
async def send_user_stats(callback: CallbackQuery, state: FSMContext):
    today_memorized = await cmc_client.get_user_memorized_count(chat_id=callback.from_user.id, today=True)
    week_memorized = await cmc_client.get_user_memorized_count(chat_id=callback.from_user.id, week=True)
    total_memorized = await cmc_client.get_user_memorized_count(chat_id=callback.from_user.id, total=True)
    percentage_memorized = (total_memorized / 604) * 100 if total_memorized is not None else 0
    user_data = await state.get_data()
    a = _("📊 All your statistics:")
    b = _("📖 Number of pages you have memorized: <b>{total_memorized}</b>").format(total_memorized=total_memorized if total_memorized is not None else 0)
    c = _("🔋 You have memorized <b>{:.2f}</b>% of the whole Quran!").format(percentage_memorized)
    d = _("📆 You memorized <b>{today_memorized}</b> pages in one day!").format(today_memorized=today_memorized if total_memorized is not None else 0)
    e = _("📆 You memorized <b>{week_memorized}</b> pages per week!").format(week_memorized=week_memorized if week_memorized is not None else 0)
    result = "\n".join([a, b, c, d, e])
    ic(result)
    await callback.message.edit_text(text=result, reply_markup=go_back_keyboard())
