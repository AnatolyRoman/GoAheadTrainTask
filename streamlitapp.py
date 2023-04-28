import streamlit as st
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt



st.set_page_config(page_title="Go Ahead: Train Task")

st.markdown('''
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #fd7e14; font-size: 100px;">Go Ahead</h1>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #007aff; font-size: 70px;">Train Task</h1>
''', unsafe_allow_html=True)

st.markdown('''
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF; font-size: 40px;">Задание 1. Логика</h1>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 25px;"></h1>
''', unsafe_allow_html=True)

st.markdown('''
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF; font-size: 40px;">Условие:</h1>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 25px;"></h1>
''', unsafe_allow_html=True)

st.markdown('''
    <p style="text-align: left; font-family: 'Gill Sans'; color: #D8D8D8; font-size: 20px;">
        У вас есть два шарика, которые разбиваются при падении с одной и той же высоты и здание из 100 этажей. 
        Вы можете подниматься на любой этаж и бросать с него один из шариков. 
        За какое минимальное количество бросков шариков можно выяснить наименьший номер этажа, 
        при падении с которого шарики разбиваются?
    </p>
''', unsafe_allow_html=True)
    
st.markdown(f'''
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF">Рассуждение:</h1>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"></h1>
    <p style="text-align: left; font-family: 'Gill Sans'; font-size: 20px; color: #D8D8D8">
        Для решения этой задачи можно использовать алгоритм <span style='color:green'>бинарного поиска</span>. Конечно, если мы будем подниматься по лестнице и проверять каждый этаж — это <span style='color:green'>долго</span>, и мы устанем. Лучше взять лифт подняться на 50 этаж и сбросить шар с балкона на этой высоте. Если шар разбился, мы будем проверять этажи <span style='color:green'>с 1 по 49 этаж</span>, если нет — будем проверять этажи <span style='color:green'>с 51-го по 100-й этаж</span>. При таком подходе мы каждый раз убираем <span style='color:green'>половину этажей</span>, которые мы не станем проверять, вообще мы их просто <span style='color:green'>исключаем</span>. Таким образом с помощью лифта нам понадобится <span style='color:green'>в худшем случае 7 проверок всего лишь</span>. Тут можно еще и использовать <span style='color:green'>логарифм</span>. Например, для Бурдж Халифа, чтобы узнать на каком этаже сидит ваш друг и смотрит на город, в худшем случае нам понадобится 8 попыток. А для воображаемого задания с 1 000 000 000 этажей нам понадобится в худшем случае всего log2 1000000000 ≈ 29.9 == <span style='color:green'>30 попыток</span>.
    </p>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF; font-size: 25px;">Краткий ответ: Нужно 7 попыток в худшем случае</h1>
    <h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 36px;"></h1>
''', unsafe_allow_html=True)


def binary_search(num_floors, num_attempts):
    start = 0
    end = num_floors
    attempt_count = 0
    while start <= end and attempt_count < num_attempts:
        mid = (start + end) // 2
        attempt = st.checkbox(f"Шар разбился с {mid+1} этажа?")
        attempt_count += 1
        if attempt:
            end = mid - 1
        else:
            # Если шар не разбился, то нижняя граница интервала должна быть больше, чем текущий этаж
            start = mid + 1
    if start > end:
        # Если шар не разбился ни на одном этаже, значит, мы исчерпали все попытки
        # и не можем точно определить минимальный этаж
        return None, None

    # Если шарик не разбился на первом этаже, то это значит, что этот этаж - минимальный возможный этаж
    if start == 1:
        return start, (start, start)

    # Определяем интервал, где, вероятно, находится минимальный этаж
    if start == end:
        floor_interval = (max(1, start - num_attempts), min(num_floors, end + num_attempts))
    else:
        floor_interval = (max(1, start - num_attempts + 1), min(num_floors, end + num_attempts))

    if floor_interval[0] > floor_interval[1]:
        # Интервал не определен
        return start, "Не удалось определить интервал"

    return start, floor_interval

def main():
    st.title("A game with crystal balls")
    num_floors = st.number_input("Введите количество этажей здания", min_value=2, step=1)
    num_attempts = st.number_input("Введите количство хрустальных шариков", min_value=1, max_value=100, step=1)

    min_floor, floor_interval = binary_search(num_floors, num_attempts)

    if min_floor is not None:
        st.success(f"Минимальный этаж: {min_floor+1}")
        if isinstance(floor_interval, tuple):
            st.success(f"Оставшийся интервал: от {floor_interval[0]} до {floor_interval[1]}")
        else:
            st.warning(floor_interval)
    else:
        st.warning("Не удалось определить минимальный этаж")

if __name__ == "__main__":
    main()




st.markdown(
    f'<hr style="border-top: 5px solid #fd7e14; margin-top: 30px; margin-bottom: 30px;">',
    unsafe_allow_html=True)



st.markdown('''<h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF"
            >Математика + Программирование
            </h1><h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"
            ></h1>''', 
            unsafe_allow_html=True)

st.markdown('''<h1 style="text-align: left; font-family: 'Gill Sans'; color: #928FFF"
            >Условие:</h1><h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"
            ></h1>''', 
            unsafe_allow_html=True)


def piecewise_constant(x, params):
    a, b, c = params
    return np.piecewise(x, [x < c, x >= c], [a, b])

def mse(params, x, y):
    y_pred = piecewise_constant(x, params)
    return np.mean((y - y_pred)**2)

def optimize_params(x, y):
    # Используем метод перебора для поиска минимума функции mse
    params = np.zeros((3,))
    min_mse = float('inf')
    for i in range(1, x.size):
        a = y[:i].mean()
        b = y[i:].mean()
        c = x[i-1]
        mse_val = mse([a, b, c], x, y)
        if mse_val < min_mse:
            min_mse = mse_val
            params = [a, b, c]
    return tuple(params)

def app():
    st.title("Оптимизация параметров кусочно-постоянной функции")
    n = st.slider("Выберите количество точек", 2, 100, 10)
    A = np.random.rand(n, 2)
    A[:, 0] = np.sort(A[:, 0])
    x = A[:, 0]
    y = A[:, 1]
    a, b, c = optimize_params(x, y)

    st.header("График данных и оптимальной кусочно-постоянной функции")
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x, piecewise_constant(x, [a, b, c]), c='r')

    # добавляем настройки для matplotlib
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)

if __name__ == '__main__':
    app()








st.markdown('')
st.markdown('''<h3 style="text-align: right; font-family: 'Gill Sans'; color: #fd7e14"
            >by Ròman Anatoly</h3>''', 
            unsafe_allow_html=True)
