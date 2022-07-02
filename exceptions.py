import json


class EnemyDown(Exception):
    pass


class Score:
    def __init__(self, score, name, json_list):
        self.score = score
        self.name = name
        self.json_list = json_list

    def count_of_score(self):
        new_dict = {}
        json_list = self.json_list
        search_user_list = self.search_user()
        search_user_list.append(self.score)
        search_user_list.sort(reverse=True)
        new_dict[self.name] = search_user_list[:10]
        for elem in json_list:
            for key in elem.keys():
                if key == self.name:
                    json_list.remove(elem)
        json_list.append(new_dict)
        return json_list

    def search_user(self) -> list:
        for dictionary in self.json_list:
            for keys, value in dictionary.items():
                if keys == self.name:
                    return value
        return []

    @staticmethod
    def show_scores():
        with open('scores.txt', 'r') as f:
            json_list = json.loads(f.read())
        result_dict = {}
        for dictionary in json_list:
            i = 0
            for keys, values in dictionary.items():
                for elem in values:
                    i += 1
                    result_dict[str(keys) + str(i)] = elem

        if len(result_dict) > 10:
            for i in range(10):
                for key, values in result_dict.items():
                    if values == max(result_dict.values()):
                        print(key[:-1], values)
                        del result_dict[key]
                        break
        else:
            for i in range(len(result_dict)):
                for key, values in result_dict.items():
                    if values == max(result_dict.values()):
                        print(key[:-1], values)
                        del result_dict[key]
                        break


class GameOver(Exception, Score):
    def __init__(self, scores, name):
        self.scores = scores
        self.name = name

        with open('scores.txt', 'r') as f:
            json_d = json.loads(f.read())
            json_d = Score(self.scores, self.name, json_d).count_of_score()
            json_d = json.dumps(json_d)
        with open('scores.txt', 'w') as f:
            f.write(json_d)
        print("You lose,", name)
        print("You got", self.scores, "points")