import json


def load_candidates_from_json(path):
    """ returns list of the candidates """
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)



def get_candidate_by_id(candidate_id):
    """ returns candidate by id """
    candidates = load_candidates_from_json('candidates.json')

    for c in candidates:
        if c['id'] == candidate_id:
            return c
    return None


def get_candidates_by_name(candidate_name):
    """ returns candidates by name """
    candidates = load_candidates_from_json('candidates.json')
    result = []
    for c in candidates:
        if candidate_name.lower() in c['name'].lower():
            result.append(c)
    return result


def get_candidates_by_skill(skill_name):
    """ returns candidate by skill name"""
    candidates = load_candidates_from_json('candidates.json')
    result = []
    for c in candidates:
        candidate_skills = c['skills'].lower().split(', ')
        if skill_name.lower() in candidate_skills:
            result.append(c)
    return result

#test = load_candidates_from_json('candidates.json')
#print(test)