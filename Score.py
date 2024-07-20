import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
#from flask import Flask, render_template

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    points = POINTS_OF_WINNING(difficulty)
    try:
        if not os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'w') as score_file:
                score_file.write('0')

        with open(SCORES_FILE_NAME, 'r+') as score_file:
            current_score = int(score_file.read().strip())
            new_score = current_score + points
            score_file.seek(0)
            score_file.write(str(new_score))
    except Exception as e:
        return BAD_RETURN_CODE
    return new_score