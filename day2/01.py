

class Constants:
    DELIMITER = ";"
    GREEN = "green"
    BLUE = "blue"
    RED = "red"
    BALLS_DELIMITER = ","
    GAMES_DELIMITER = ":"
    TOTAL_PERMITTED = {
        RED: 12,
        GREEN: 13,
        BLUE: 14
    }



def parse_ball_input(ball_input):
    count, color = ball_input.strip().split(" ")
    return int(count), color

def get_ball_count(input, ball_hash):
    for ball_input in input.split(Constants.BALLS_DELIMITER):
        count, color = parse_ball_input(ball_input)
        if color not in ball_hash:
            ball_hash[color] = 0
        ball_hash[color] += count
    return ball_hash

def is_valid(ball_hash):
    for color, count in ball_hash.items():
        if Constants.TOTAL_PERMITTED[color] < count:
            return False
    return True
    

if __name__ == "__main__":
    result = 0
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            delimited = line.split(Constants.GAMES_DELIMITER)
            game_id = int(delimited[0].split(" ")[1])
            include = True
            for input in delimited[1].split(Constants.DELIMITER): # Skip first as it contains game meta info
                ball_hash = {}
                ball_hash = get_ball_count(input, ball_hash)
                if not is_valid(ball_hash):
                    include = False
                    break
            if include:
               result += game_id 
    print(result)