n_tuple=("shradha", "Nikhil", "chakuli", "Bubu")
m_list=[1,2,3]
def func(words,numbers):
    result= tuple(w[:][:3] for w in words or numbers)
    return result


print(func(n_tuple, m_list))