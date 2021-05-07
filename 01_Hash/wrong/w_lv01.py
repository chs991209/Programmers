# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lv01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Euimin Chung <github.com/euiminnn>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/17 01:41:40 by echung            #+#    #+#              #
#    Updated: 2021/04/17 01:54:11 by echung           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def solution(participant, completion):
    for p in participant:
        flag = 0
        for c in completion:
            if p == c:
                flag = 1
                completion.remove(c)
                break
        if not flag:
            return p

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              try again :(                           "
"                                                                     "
"                               logic: OK                             "
"                                time: KO                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
