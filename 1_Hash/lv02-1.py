from itertools import islice

def solution(phone_book):
    phone_book = sorted(phone_book)
    i = 0
    for p in islice(phone_book, len(phone_book) - 1):
        f = phone_book[i+1].startswith(phone_book[i])
        if f:
            return False
        i = i + 1
    return True

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(83.3)                       "
"                                time: OK(16.7)                       "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
