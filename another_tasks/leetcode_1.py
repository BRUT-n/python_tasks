#https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(self, nums: list[int]) -> bool:
    '''
    Учитывая целочисленные числа массив, верните True, если какое -либо значение появляется как минимум дважды в массиве,
    и верните False, если каждый элемент уникальный.
    '''
    return len(set(nums)) != len(nums) # длина сета списка не равна длине исходного списка (сет убирает дубли)

#https://leetcode.com/problems/buddy-strings/
def buddyStrings(self, s: str, goal: str) -> bool:
    '''
    Определить, можно ли получить строку goal из строки s, поменяв местами ровно две буквы в строке s.
    Если s = "abcd", меняете 'a' и 'c', что приводит к строке s = "cbad", а goal = cbad - ТРУ
    '''
    if len(s) == 1: # если длина строки 1, то нельзя поменять символы местами
        return False
    if len(s) != len(goal): # если длины разные, то нельзя получить заданную строку
        return False
    set_s = set(s) # сет для С
    set_goal = set(goal) # сет для ГОЛ
    if set_s != set_goal: # если сеты не равны, то есть повторяющиеся символы
        return False
    if s == goal: # если строки индентичны, то мы можем поменять одинаковые символы местами
        return len(set_s) != len(s) # есть повторяющиеся символы, и обмен допустим?
    count = 0 # счетчик повтороний (максимум 2)
    s_diff = set()
    goal_diff = set()
    for index in range(len(s)): # индекс в рендже строки С
        if s[index] != goal[index]: # если С(индекс) не равно ГОЛ(индекс), то есть символы отличаются
            s_diff.add(s[index]) # кидаем в сет С
            goal_diff.add(goal[index]) # кидаем в сет ГОЛ
            count += 1 # в счетчик изменений +1 (максимум может быть 2)
            if count > 2:
                return False
    return s_diff == goal_diff

# https://leetcode.com/problems/two-sum/
def twoSum(self, nums: list[int], target: int) -> list[int]:
    '''
    вернуть индексы чисел, сумма которах равна ТАРГЕТ
    '''
    for i in range(len(nums)): # для первого индекса (первого числа) по длине спика с каждым следующим числом
        for j in range(i + 1, len(nums)): # следущие числа после первого, потому что (и+1)
            if nums[i] + nums[j] == target: # если сумма равна ТАРГЕТ
                return [i, j]