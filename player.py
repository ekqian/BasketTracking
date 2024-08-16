import numpy as np
class Player:
    def __init__(self, ID, team, color):
        self.ID = ID
        self.team = team
        self.color = color
        self.previous_bb = None
        # dict of tuples {timestamp: (position_y, position_x), ...}
        self.positions = {}
        self.has_ball = False
        self.is_open = False
    
    
    def calculate_is_open(self, player_with_ball, opposing_team, dist_threshold, padding, timestamp):
        if timestamp not in self.positions:
            return False
        
        for opp_player in opposing_team:
            player_pos = self.positions[timestamp]
            player_with_ball_pos = player_with_ball.positions[timestamp]
            if timestamp not in opp_player.positions:
                continue
            opp_player_pos = opp_player.positions[timestamp]

            if self.calculate_distance(player_pos, opp_player_pos) < dist_threshold:
                return False
            
            dist_to_line = self.distance_to_line(player_pos, player_with_ball_pos, opp_player_pos)
            if dist_to_line < padding:
                return False
            
        return True


    def calculate_distance(self, player_pos, opp_player_pos):
        return np.sqrt((player_pos[0] - opp_player_pos[0]) ** 2 + (player_pos[1] - opp_player_pos[1]) ** 2)


    def distance_to_line(self, player_pos, player_with_ball_pos, opp_player_pos):
        np_ball_pos = np.array(player_with_ball_pos)
        np_player_pos = np.array(player_pos)
        np_opp_pos = np.array(opp_player_pos)
        return np.abs(np.cross(np_ball_pos - np_player_pos, np_player_pos - np_opp_pos)) / np.linalg.norm(np_ball_pos - np_player_pos)
