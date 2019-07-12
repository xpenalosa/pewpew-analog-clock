import random

import pew
pew.init()


class Player():
    def __init__(self, x = 1, y = 4, color=1):
        self.x = x
        self.y = y
        self.color = color
        self.jumping = False


    def parse_keys(self, keys):
        press_jump = keys & pew.K_UP or keys & pew.K_O
        if not self.jumping and press_jump:
            self.y = max(self.y - 1, 1)
        self.jumping = self.jumping != press_jump


    def clear_jump(self):
        self.jumping = False


    def fall(self):
        if not self.jumping:
            self.y = min(self.y + 1, 7)


    def blit(self, screen, clear=False):
        if clear:
            screen.pixel(self.x, self.y, 0)
        else:
            screen.pixel(self.x, self.y, self.color)


    def collides(self, pos_list):
        return self.y in pos_list


class Obstacle():
    def __init__(self, color=2):
        self.randomize_gap()
        self.x = 8
        self.color = color

    def randomize_gap(self): 
        gap_pos = random.randint(2, 6) 
        self.gaps = (gap_pos, gap_pos + 1)
    

    def get_collisions(self):
        return [i for i in range(1,8) if i not in self.gaps]


    def move(self):
        self.x -= 1
        if self.x < 0:
            self.x = 8
            self.randomize_gap()


    def get_pos(self):
        return self.x


    def blit(self, screen, clear=False):
        for i in self.get_collisions():
            if clear:
                screen.pixel(self.x, i, 0)
            else:
                screen.pixel(self.x, i, self.color)


def get_score_array(score):
    return [int(b) for b in bin(score)[2::]]



def play():

    sc = pew.Pix()
    keys = pew.keys()

    player_x = 1
    p = Player(x=player_x)
    o = Obstacle()

    score = 0
    player_collided = False

    # Game loop
    while not keys & pew.K_X and not player_collided:
        # Parse events
        p.parse_keys(keys)
        if o.get_pos() == player_x:
            if p.collides(o.get_collisions()):
                player_collided = True
        elif o.get_pos() == player_x - 1:
            score += 1

        p.fall()

        score_array = get_score_array(score)[::-1]
        for i in range(len(score_array)):
            sc.pixel(7-i ,0, 3 * score_array[i])

        p.blit(sc)
        o.blit(sc)

        pew.show(sc)
        pew.tick(1/2)

        # Clear last player position
        p.blit(sc, clear=True)
        o.blit(sc, clear=True)
        o.move()
        p.clear_jump()
        keys = pew.keys()

    

    if p.collides(o.get_collisions()):
        # Display score
        print(f"Game ended with a score of {score}!!")
    else:
        print("Quit game.")

play()
