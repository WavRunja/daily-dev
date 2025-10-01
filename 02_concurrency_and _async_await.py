# Concurrency and  async / await


@app.get('/')
async def read_results():
    results = await some_library()
    return results


async def get_burgers(number: int):
    # Готовим бургеры по специальному асинхронному рецепту
    return burgers


# Это не асинхронный код
def get_sequential_burgers(number: int):
    # Готовим бургеры последовательно по шагам
    return burgers


# Это не заработает, поскольку get_burgers объявлена с использованием async def
burgers = get_burgers(2)


@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
