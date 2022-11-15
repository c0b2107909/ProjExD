# pygame version

import numpy as np
import sys
import random
import copy
import time
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN


class DrawWindow():

    def draw_number(self):
        fontsize = 80
        color = (0, 0, 0)
        sysfont_number = pygame.font.SysFont(None, fontsize)
        one = sysfont_number.render("1", True, color)
        one_rect = one.get_rect()
        one_rect.center = (60, 130)
        two = sysfont_number.render("2", True, color)
        two_rect = two.get_rect()
        two_rect.center = (160, 130)
        three = sysfont_number.render("3", True, color)
        three_rect = three.get_rect()
        three_rect.center = (260, 130)
        four = sysfont_number.render("4", True, color)
        four_rect = four.get_rect()
        four_rect.center = (360, 130)
        five = sysfont_number.render("5", True, color)
        five_rect = five.get_rect()
        five_rect.center = (460, 130)
        six = sysfont_number.render("6", True, color)
        six_rect = six.get_rect()
        six_rect.center = (560, 130)
        seven = sysfont_number.render("7", True, color)
        seven_rect = seven.get_rect()
        seven_rect.center = (660, 130)
        # output
        SURFACE.blit(one, one_rect)
        SURFACE.blit(two, two_rect)
        SURFACE.blit(three, three_rect)
        SURFACE.blit(four, four_rect)
        SURFACE.blit(five, five_rect)
        SURFACE.blit(six, six_rect)
        SURFACE.blit(seven, seven_rect)

    def draw_disc(self, field):
        if( (PLAYER == 1) and (COMPUTER == -1) ):
            player_color = 0xe60033
            computer_color = 0xe6b400
        elif( (PLAYER == -1) and (COMPUTER == 1) ):
            player_color = 0xe6b400
            computer_color = 0xe60033
        else:
            print("Error : class DrawWindow, function draw_dict")
            sys.exit()
        for i in range(len(field)):
            for j in range(len(field[0])):
                disc = field[(i, j)]
                ypos = 190 + (100 * i) + 5
                xpos = 10 + (100 * j) + 5
                if(disc == PLAYER):
                    pygame.draw.ellipse(SURFACE, player_color, ((xpos, ypos), (90, 90)))
                elif(disc == COMPUTER):
                    pygame.draw.ellipse(SURFACE, computer_color, ((xpos, ypos), (90, 90)))
                elif(disc == EMPTY):
                    pass
                else:
                    print("Error : function darw_disc")
                    sys.exit()

    def draw_field(self):
        # 6*7
        weight = 5
        for xpos in range(10, 711, 100):
            pygame.draw.line(SURFACE, 0x000000, (xpos, 190), (xpos, 791))
            pass
        for ypos in range(190, 791, 100):
            pygame.draw.line(SURFACE, 0x000000, (10, ypos), (711, ypos))
            pass
        # above number
        for xpos in range(10, 711, 100):
            pygame.draw.line(SURFACE, 0x000000, (xpos, 80), (xpos, 180))
        for ypos in range(80, 181, 100):
            pygame.draw.line(SURFACE, 0x000000, (10, ypos), (711, ypos))

    def draw_all(self, field):
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
            SURFACE.fill((255, 255, 255))
            self.draw_field()
            self.draw_disc(field)
            self.draw_number()
            pygame.display.update()
            FPSCLOCK.tick(3)


class PlayerClass(DrawWindow):

    def update_point(self, field, number):
        (x, y) = field.shape
        if((number <= 0) or (y < number)):
            print("Error: number is out of range.(select_point)")
            sys.exit()
        for i in range(len(field)-1, -1, -1):
            point = field[(i, number - 1)]
            if(point == 0):
                return (i, number - 1)
        print("Error: that column in not empty.(select_point)")
        sys.exit()

    def update_field(self, field, xpos, ypos):
        if(field[(xpos, ypos)] != 0):
            print("Error: that point is not 0.(update_field)")
            sys.exit()
        field[xpos, ypos] = PLAYER
        return field

    def from_pos_to_number(self, xpos, ypos):
        if( 10 < xpos and xpos < 110 ):    # 1
            return 1
        elif( 110 < xpos and xpos < 210 ):  # 2
            return 2
        elif( 210 < xpos and xpos < 310 ):  # 3
            return 3
        elif( 310 < xpos and xpos < 410 ):  # 4
            return 4
        elif( 410 < xpos and xpos < 510 ):  # 5
            return 5
        elif( 510 < xpos and xpos < 610 ):  # 6
            return 6
        elif( 610 < xpos and xpos < 710 ):  # 7
            return 7
        else:
            print("Error : function from_pos_to_number.")
            sys.exit()

    def draw_sentence(self):
        fontsize = 36
        color = (0, 0, 0)
        sysfont = pygame.font.SysFont(None, fontsize)
        # select sentence
        s = "Please select number from one to seven."
        ss = sysfont.render(s, True, color)
        ss_rect = ss.get_rect()
        ss_rect.left = 170
        ss_rect.bottom = 60
        # turn sentence
        s = "Your turn : "
        ts = sysfont.render(s, True, color)
        ts_rect = ts.get_rect()
        ts_rect.left = 20
        ts_rect.bottom = 60
        # draw
        SURFACE.blit(ss, ss_rect)
        SURFACE.blit(ts, ts_rect)

    def draw_all(self, field):
        border = [10, 110, 210, 310, 410, 510, 610, 710]
        x, y = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN and event.button == 1):
                    x, y = event.pos[0], event.pos[1]
                    #print("({0}, {1})".format(x, y))
                    break
            SURFACE.fill((255, 255, 255))
            self.draw_field()
            self.draw_disc(field)
            self.draw_number()
            # add
            self.draw_sentence()
            pygame.display.update()
            FPSCLOCK.tick(3)

            if( (10 < x and x < 710) and (80 < y and y < 180) and (x not in border) ):
                break
            else:
                # loop continue
                pass
        number = self.from_pos_to_number(x, y)
        return number



class ComputerClass(DrawWindow):

    def choose_number(self, field):
        number_list = []
        transpose_field = np.transpose(field)
        for i in range(len(transpose_field)):
            if(0 in transpose_field[i]):
                number_list.append(i+1)
        r = random.randrange(0, len(number_list))
        return number_list[r]

    def choose_number2_func1(self, field):
        # rowにリーチがかかっているか確認
        point_list = []
        tmp_field = copy.copy(field)
        # -1を削除
        tmp_field[field < 0] = 0
        for i in range(0, len(field)):
            val = 0
            for j in range(0, len(field[0])):
                val = val * tmp_field[(i, j)] + tmp_field[(i, j)]
                tmp_field[(i, j)] = val
                # val == 2
                if((val == 2) and ((j+1) < len(field[0])) and ((j+2) < len(field[0]))):
                    if((field[(i, j+1)] == 0) and (field[(i, j+2)] == 1)):
                        point_list.append((i, j+1))
                if((val == 2) and ((j-2) >= 0) and ((j-3) >= 0)):
                    if((field[(i, j-2)] == 0) and (field[(i, j-3)] == 1)):
                        point_list.append((i, j-2))
                # val == 3
                if((val == 3) and ((j+1) < len(field[0]))):
                    if((field[(i, j+1)] == 0) and ((i, j+1) not in point_list)):
                        point_list.append((i, j+1))
                if((val == 3) and ((j-3) >= 0)):
                    if((field[(i, j-3)] == 0) and ((i, j-3) not in point_list)):
                        point_list.append((i, j-3))
        return point_list

    def choose_number2_func2(self, field):
        # colにリーチがかかっていないか確認
        transpose_field = np.transpose(field)
        point_list = self.choose_number2_func1(transpose_field)
        new_point_list = []
        for i in range(0, len(point_list)):
            v1, v2 = point_list[i]
            new_point_list.append((v2, v1))
        return new_point_list

    def choose_number2(self, field):
        func1_list = self.choose_number2_func1(field)
        func2_list = self.choose_number2_func2(field)
        point_list = list(set(func1_list) | set(func2_list))
        if(len(point_list) != 0):
            number_list = []
            for i in point_list:
                v1, v2 = i
                if((v2+1) not in number_list):
                    number_list.append(v2+1)
            r = random.randrange(0, len(number_list))
            return number_list[r]
        elif(len(point_list) == 0):
            return self.choose_number(field)
        else:
            print("Error: choose_number2")
            sys.exit()

    def update_point(self, field, number):
        (x, y) = field.shape
        if((number <= 0) or (y < number)):
            print("Error: number is out of range.(select_point)")
            sys.exit()
        for i in range(len(field)-1, -1, -1):
            point = field[(i, number - 1)]
            if(point == 0):
                return (i, number - 1)
        print("Error: that column in not empty.(select_point)")
        sys.exit()

    def update_field(self, field, xpos, ypos):
        if(field[(xpos, ypos)] != 0):
            print("Error: that point is not 0.(update_field)")
            sys.exit()
        field[xpos, ypos] = COMPUTER
        return field

    def draw_sentence(self):
        fontsize = 36
        color = (0, 0, 0)
        sysfont = pygame.font.SysFont(None, fontsize)
        # please sentence
        s = "Please click right bottom."
        ps = sysfont.render(s, True, color)
        ps_rect = ps.get_rect()
        ps_rect.left = 220
        ps_rect.bottom = 60
        # turn computer
        s = "Computer turn : "
        ts = sysfont.render(s, True, color)
        ts_rect = ts.get_rect()
        ts_rect.left = 20
        ts_rect.bottom = 60
        # next sentence
        s = "NEXT."
        ns = sysfont.render(s, True, (255, 255, 255))
        ns_rect = ns.get_rect()
        ns_rect.center = (610, 40)
        # draw
        SURFACE.blit(ts, ts_rect)
        SURFACE.blit(ps, ps_rect)
        x, y, w, h = 560, 20, 100, 40
        pygame.draw.rect(SURFACE, color, ((x, y), (w, h)))
        SURFACE.blit(ns, ns_rect)
        return x, y, w, h

    def draw_all(self, field):
        x, y = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN and event.button == 1):
                    x, y = event.pos[0], event.pos[1]
                    break
            SURFACE.fill((255, 255, 255))
            self.draw_field()
            self.draw_disc(field)
            self.draw_number()
            # add
            lx, uy, w, h = self.draw_sentence()
            pygame.display.update()
            FPSCLOCK.tick(3)

            if( (lx <= x and x <= (lx+w)) and (uy <= y and y <= (uy + h)) ):
                break
            else:
                pass


class VictoryCondition:
    # 勝利条件
    def victory_condition_row(self, field):
        tmp_field_first = copy.copy(field)
        tmp_field_second = copy.copy(field)
        tmp_field_first[field < 0] = 0     # -1を排除
        tmp_field_second[field > 0] = 0   # 1を排除
        for i in range(len(field[:,0])):
            val_f = 0
            val_s = 0
            for j in range(len(field[0])):
                val_f = val_f * tmp_field_first[(i, j)] + tmp_field_first[(i, j)]
                val_s = val_s * np.absolute(tmp_field_second[(i, j)]) + tmp_field_second[(i, j)]
                tmp_field_first[(i, j)] = val_f
                tmp_field_second[(i, j)] = val_s
        boolean_value_first, boolean_value_second = False, False
        if(np.max(tmp_field_first) >= 4): boolean_value_first = True    # 4以上が含まれているか
        if(np.min(tmp_field_second) <= -4): boolean_value_second = True # -4以下が含まれているか
        return boolean_value_first, boolean_value_second

    def victory_condition_col(self, field):
        transpose_field = np.transpose(field)
        bvp, bvc = self.victory_condition_row(transpose_field)
        return bvp, bvc

    def victory_condition_slash(self, field):
        shift_field_upper = np.zeros(field.shape, dtype=int)
        shift_field_lower = np.zeros(field.shape, dtype=int)
        shift_field_middle = np.zeros(field.shape, dtype=int)
        for i in range(len(field)):
            shift_field_upper[i] = np.roll(field[i], -i)
            shift_field_middle[i] = np.roll(field[i], 1-i)
            shift_field_lower[i] = np.roll(field[i], 2-i)
        for i in range(len(field)):
            for j in range(len(field[0])):
                if( (i >= 4) or (j >= 4) ): shift_field_upper[(i, j)] = 0
                if( (i==0) or (i==5) or (j >= 4) ): shift_field_middle[(i, j)] = 0
                if( (i <= 1) or (j >= 4) ): shift_field_lower[(i, j)] = 0
        bvuf, bvus = self.victory_condition_col(shift_field_upper)
        bvmf, bvms = self.victory_condition_col(shift_field_middle)
        bvlf, bvls = self.victory_condition_col(shift_field_lower)
        bvf, bvs = False, False
        if(bvuf or bvmf or bvlf): bvf = True
        if(bvus or bvms or bvls): bvs = True
        return bvf, bvs

    def victory_condition_backslash(self, field):
        shift_field_upper = np.zeros(field.shape, dtype=int)
        shift_field_lower = np.zeros(field.shape, dtype=int)
        shift_field_middle = np.zeros(field.shape, dtype=int)
        for i in range(len(field)):
            shift_field_upper[i] = np.roll(field[i], i)
            shift_field_middle[i] = np.roll(field[i], i-1)
            shift_field_lower[i] = np.roll(field[i], i-2)
        for i in range(len(field)):
            for j in range(len(field[0])):
                if( (i >= 4) or (j <= 2) ): shift_field_upper[(i, j)] = 0
                if( (i==5) or (i==0) or (j <= 2) ): shift_field_middle[(i, j)] = 0
                if( (i <= 1) or (j <= 2) ): shift_field_lower[(i, j)] = 0
        bvuf, bvus = self.victory_condition_col(shift_field_upper)
        bvmf, bvms = self.victory_condition_col(shift_field_middle)
        bvlf, bvls = self.victory_condition_col(shift_field_lower)
        bvf, bvs = False, False
        if(bvuf or bvmf or bvlf): bvf = True
        if(bvus or bvms or bvls): bvs = True
        return bvf, bvs

    def victory_condition(self, field):
        result_first = False
        result_second = False
        vcr_first, vcr_second = self.victory_condition_row(field)
        vcc_first, vcc_second = self.victory_condition_col(field)
        vcs_first, vcs_second = self.victory_condition_slash(field)
        vcb_first, vcb_second = self.victory_condition_backslash(field)
        if( (vcr_first or vcc_first or vcs_first or vcb_first) and (PLAYER == 1) ):
            result_first = True
            print("You won.(first)")
        elif( (vcr_first or vcc_first or vcs_first or vcb_first) and (COMPUTER == 1) ):
            result_first = True
            print("computer won.(first)")
        else:
            pass
        if( (vcr_second or vcc_second or vcs_second or vcb_second) and (PLAYER == -1) ):
            result_second = True
            print("You won.(second)")
        elif( (vcr_second or vcc_second or vcs_second or vcb_second) and (COMPUTER == -1) ):
            result_second = True
            print("Computer won.(second)")
        else:
            pass
        return result_first, result_second


class DisplayOutput(VictoryCondition, DrawWindow):

    def draw_title(self):
        color = (0, 0, 0)
        # tile sentence
        s = "Connect Four."
        sysfont_title = pygame.font.SysFont(None, 80)
        ts = sysfont_title.render(s, True, color)
        ts_rect = ts.get_rect()
        ts_rect.center = (500, 250)
        # start sentence
        s = "start."
        sysfont_start = pygame.font.SysFont(None, 60)
        ss = sysfont_start.render(s, True, (255, 255, 255))
        ss_rect = ss.get_rect()
        ss_rect.center = (500, 550)
        # square Rect
        w, h = 150, 50
        lx, uy = 500-(w/2), 550-(h/2)
        # initial value
        x, y = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN and event.button == 1):
                    x, y = event.pos[0], event.pos[1]
                    break
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(ts, ts_rect)
            pygame.draw.rect(SURFACE, color, ((lx, uy), (w, h)) )
            SURFACE.blit(ss, ss_rect)
            pygame.display.update()
            FPSCLOCK.tick(3)
            if( (lx <= x and x <= (lx+w)) and (uy <= y and y <= (uy+h)) ):
                break
            else:
                pass

    def draw_select(self):
        # please sentence
        s = "Please select first or second."
        sysfont_ps = pygame.font.SysFont(None, 60)
        ps = sysfont_ps.render(s, True, (0, 0, 0))
        ps_rect = ps.get_rect()
        ps_rect.center = (500, 250)
        # first sentence
        s = "Fisrt."
        sysfont_fs = pygame.font.SysFont(None, 40)
        fs = sysfont_fs.render(s, True, (0, 0, 0))
        fs_rect = fs.get_rect()
        fs_rect.center = (300, 400)
        # second sentence
        s = "Second."
        sysfont_ss = pygame.font.SysFont(None, 40)
        ss = sysfont_ss.render(s, True, (0, 0, 0))
        ss_rect = ss.get_rect()
        ss_rect.center = (700, 400)
        # detail
        redx, redy = 300, 530
        yellowx, yellowy = 700, 530
        radius = 100
        # initial value
        x, y = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if( event.type == MOUSEBUTTONDOWN and event.button == 1):
                    x, y = event.pos[0], event.pos[1]
                    break
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(ps, ps_rect)
            SURFACE.blit(fs, fs_rect)
            SURFACE.blit(ss, ss_rect)
            pygame.draw.circle(SURFACE, 0xe60033, (redx, redy), radius, 0)
            pygame.draw.circle(SURFACE, 0xe6b400, (yellowx, yellowy), radius, 0)
            pygame.display.update()
            FPSCLOCK.tick(3)

            red_radius = np.sqrt( (x - redx)**2 + (y - redy)**2 )
            yellow_radius = np.sqrt( (x - yellowx)**2 + (y - yellowy)**2 )
            if( red_radius <= radius ):
                player, computer = 1, -1
                turn = player
                print("PLAYER = first")
                return turn, player, computer
                #break
            elif( yellow_radius <= radius ):
                player, computer = -1, 1
                turn = computer
                print("COMPUTER = first")
                return turn, player, computer
                #break
            elif( red_radius > radius and yellow_radius > radius ):
                pass
            else:
                print("Error : class DisplayOutput. function draw_select()")
                sys.exit()

    def draw_winner(self, field, result_first, result_second):
        if( (result_first == True) and (PLAYER == 1) ): s = "You won."
        elif( (result_first == True) and (COMPUTER == 1) ): s = "Computer won."
        else: pass
        if( (result_second == True) and (PLAYER == -1) ): s = "You won."
        elif( (result_second == True) and (COMPUTER == -1) ): s = "Computer won."
        else: pass
        sysfont = pygame.font.SysFont(None, 60)
        winner = sysfont.render(s, True, (0, 0, 0))
        winner_rect = winner.get_rect()
        winner_rect.center = (360, 40)
        # next sentence
        s = "NEXT."
        sysfont_ns = pygame.font.SysFont(None, 36)
        ns = sysfont_ns.render(s, True, (255, 255, 255))
        ns_rect = ns.get_rect()
        ns_rect.center = (855, 690)
        x, y, w, h = 805, 670, 100, 40
        xpos, ypos = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if( event.type == MOUSEBUTTONDOWN and event.button == 1 ):
                    xpos, ypos = event.pos[0], event.pos[1]
                    break
            SURFACE.fill((255, 255, 255))
            self.draw_field()
            self.draw_disc(field)
            self.draw_number()
            SURFACE.blit(winner, winner_rect)
            pygame.draw.rect(SURFACE, 0x000000, ((x, y), (w, h)))
            SURFACE.blit(ns, ns_rect)
            pygame.display.update()
            FPSCLOCK.tick(3)
            if( (x <= xpos and xpos <= (x+w)) and (y <= ypos and ypos <= (y + h)) ):
                break
            else:
                pass

    def draw_continue_or_end(self):
        color = (0, 0, 0)
        # heading sentence
        s = "Continue?"
        sysfont_hs = pygame.font.SysFont(None, 72)
        hs = sysfont_hs.render(s, True, color)
        hs_rect = hs.get_rect()
        hs_rect.center = (500, 250)
        # continue sentence
        s = "continue."
        sysfont_cs = pygame.font.SysFont(None, 52)
        cs = sysfont_cs.render(s, True, (255, 255, 255))
        cs_rect = cs.get_rect()
        csx, csy = 350, 500
        csw, csh = 200, 40
        cs_rect.center = (csx, csy)
        # end sentence
        s = "end."
        sysfont_es = pygame.font.SysFont(None, 40)
        es = sysfont_es.render(s, True, (239, 239, 239))
        es_rect = es.get_rect()
        esx, esy = 700, 500
        esw, esh = 80, 30
        es_rect.center = (esx, esy)
        # initial value
        x, y = 0, 0
        while(True):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN and event.button == 1):
                    x, y = event.pos[0], event.pos[1]
                    break
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(hs, hs_rect)
            pygame.draw.rect(SURFACE, color, ((csx-csw/2, csy-csh/2), (csw, csh)))
            SURFACE.blit(cs, cs_rect)
            pygame.draw.rect(SURFACE, color, ((esx-esw/2, esy-esh/2), (esw, esh)))
            SURFACE.blit(es, es_rect)
            pygame.display.update()
            FPSCLOCK.tick(3)
            if( ((csx-csw/2) <= x and x <= (csx+csw/2)) and ((csy-csh/2) <= y and y <= (csy+csh/2)) ):
                print("continue")
                return self.initialization()
            elif( ((esx-esw/2) <= x and x <= (esx+esw/2)) and ((esy-esh/2) <= y and y <= (esy+esh/2)) ):
                print("end")
                self.draw_end()
                #return 0, 0, 0
            elif( not((csx-csw/2) <= x and x <= (csw+csw/2)) or not((csy-csh/2) <= y and y <= (csy+csh/2)) or not((esx-esw/2) <= x and x <= (esx+esw/2)) or not((esy-esh/2) <= y and y <= (esy+esh/2)) ):
                pass
            else:
                print("Error : function draw_continue_or_end()")
                sys.exit()

    def draw_end(self):
        fontsize = 72
        color = (128, 128, 128)
        # end sentence
        s = "END."
        sysfont_es = pygame.font.SysFont(None, 72)
        es = sysfont_es.render(s, True, color)
        es_rect = es.get_rect()
        es_rect.center = (500, 250)
        # See you next time sentence
        s = "See you next time."
        sysfont_synt = pygame.font.SysFont(None, 72)
        synt = sysfont_synt.render(s, True, color)
        synt_rect = synt.get_rect()
        synt_rect.center = (500, 500)
        count = 0
        while(count < 1):
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                    sys.exit()
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(es, es_rect)
            SURFACE.blit(synt, synt_rect)
            pygame.display.update()
            FPSCLOCK.tick(3)
            time.sleep(1)
            pygame.quit()
            sys.exit()
            count += 1

    def initialization(self):
        field = np.zeros((6, 7), dtype=int)
        result_player, result_computer = False, False
        return field, result_player, result_computer


def main():
    global FIELD
    FIELD = np.array([[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],])

    global EMPTY
    EMPTY = 0       # マスが空の状態
    global PLAYER   # マスに自分の駒がある状態
    global COMPUTER # マスに相手の駒がある状態
    global TURN     # 現在、どちらの手番か示す

    pygame.init() # pygameを初期化
    global SURFACE
    SURFACE = pygame.display.set_mode((1000, 800))
    global FPSCLOCK
    FPSCLOCK = pygame.time.Clock()

    result_first = False
    result_second = False

    pc = PlayerClass()
    cc = ComputerClass()
    do = DisplayOutput()
    #dw = DrawWindow()

    while(True):
        do.draw_title()
        TURN, PLAYER, COMPUTER = do.draw_select()
        print("PLAYER = ", PLAYER)
        print("COMPUTER = ", COMPUTER)
        while( (result_first == False) and (result_second == False) ):
            if( TURN == PLAYER ):
                print(" TURN = PLAYER ")
                number = pc.draw_all(FIELD)
                xpos, ypos = pc.update_point(FIELD, number)
                FIELD = pc.update_field(FIELD, xpos, ypos)
                TURN = COMPUTER
                pass
            elif( TURN == COMPUTER ):
                print(" TURN = COMPUTER ")
                cc.draw_all(FIELD)
                number = cc.choose_number2(FIELD)
                xpos, ypos = cc.update_point(FIELD, number)
                FIELD = cc.update_field(FIELD, xpos, ypos)
                TURN = PLAYER
                pass
            else:
                print("Error : TURN")
                sys.exit()
            result_first, result_second = do.victory_condition(FIELD)
        do.draw_winner(FIELD, result_first, result_second)
        FIELD, result_first, result_second =  do.draw_continue_or_end()
        print(result_first, result_second)
        pass


if __name__ == '__main__':
    main()
