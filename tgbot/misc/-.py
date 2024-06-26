import asyncio


# @alru_cache
async def add_memorized_hadith(self, user_id, hadith_id):
    data = {
        "user_id": user_id,
        "hadith_id": hadith_id
    }
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.post(self.base_url + "/memorized/", json=data) as resp:
                return await resp.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def add_liked_hadith(self, user_id, hadith_id):
    data = {
        "user_id": user_id,
        "hadith_id": hadith_id,
    }
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.post(self.base_url + "/like/", json=data) as resp:
                return await resp.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def update_memorized_hadith_id(self, user_id, hadith_id=1):
    data = {
        "pending_hadith_id": hadith_id
    }
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.patch(self.base_url + f"/user/{user_id}", json=data) as resp:
                return await resp.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache


# @alru_cache
async def create_memorized_history(self, user_id, hadith_id=1):
    data = {
        "user_id": user_id,
        "hadith_id": hadith_id
    }
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.post(self.base_url + "/memorized_history/", json=data) as resp:
                if resp.status == 200:
                    return await resp.json()
                return None
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def get_hadith(self, hadith_id=1):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.get(self.base_url + f"/hadith/{hadith_id}") as resp:
                return await resp.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def get_hadiths(self, start_num: int, size: int = 50, q: str | None = None):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            # ic("session")
            endpoint = "/hadith/all" if q is None else f"/hadith/search/{q}"
            ic(endpoint)
            # "http://127.0.0.1:5173/hadith/search/yunusov"
            async with session.get(self.base_url + endpoint) as resp:
                # ic(resp.text)
                data = await resp.json()
                if not data:
                    return
                # ic(data)
                all_items: list = data.get('hadiths')
                # ic(all_items)
                overall_items_count: int = len(all_items)
                ic(overall_items_count)

                # Если результатов больше нет, отправляем пустой список
                if start_num >= overall_items_count:
                    ic([])
                    return []
                # Отправка неполной пачки (последней)
                elif start_num + size >= overall_items_count:
                    ic('elif')
                    return all_items[start_num:overall_items_count + 1]
                else:
                    ic('else')
                    return all_items[start_num:start_num + size]
    except Exception as e:
        return {"Error": str(e)}

# @alru_cache
async def get_current_books(self, skip=0, limit=10):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.get(self.base_url + f"/necessary_book/?skip={skip}&limit={limit}") as resp:
                return await resp.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

async def get_friends(self, start_num: int, size: int = 50, q: str | None = None):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            endpoint = "/user/all" if q is None else f"/user/search/{q}"
            # "http://127.0.0.1:5173/user/search/yunusov"
            async with session.get(self.base_url + endpoint) as resp:
                data = await resp.json()
                ic(data)
                ic(start_num)
                all_items: list = data.get('users')
                overall_items_count: int = len(all_items)

                # Если результатов больше нет, отправляем пустой список
                if start_num >= overall_items_count:
                    return []
                # Отправка неполной пачки (последней)
                elif start_num + size >= overall_items_count:
                    return all_items[start_num:overall_items_count + 1]
                else:
                    return all_items[start_num:start_num + size]
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def get_user_memorized_count(self, chat_id, today=False, week=False, total=False):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            # ex = "http://localhost:5173/memorized/user/557407324?today=false&week=false"
            async with session.get(
                    self.base_url + f"/memorized/user/{chat_id}?today={today}&week={week}&total={total}") as resp:
                data = await resp.json()
                ic(data)
                return data.get('memorized_count')
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

# @alru_cache
async def get_top_users_stats(self, top_total=False, top_week=False, top_today=False):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            async with session.get(
                    self.base_url + f"/memorized/?top_total={top_total}&top_week={top_week}&top_today={top_today}") as resp:
                data = await resp.json()
                ic(data)
                return data
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

async def get_chapters(self, start_num: int, size: int = 50, q: str | None = None):
    session = await self._get_session()
    try:
        async with asyncio.timeout(10):  # Set a timeout for the request
            # endpoint = "/user/all" if q is None else f"/chapters"
            endpoint = "/chapters"
            async with session.get(self.base_url + endpoint) as resp:
                data = await resp.json()
                all_items: list = data.get("chapters")
                overall_items_count: int = len(all_items)

                # Если результатов больше нет, отправляем пустой список
                if start_num >= overall_items_count:
                    return []
                # Отправка неполной пачки (последней)
                elif start_num + size >= overall_items_count:
                    return all_items[start_num:overall_items_count + 1]
                else:
                    return all_items[start_num:start_num + size]
    except asyncio.TimeoutError:
        print("Request timed out")
        return None