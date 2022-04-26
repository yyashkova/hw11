from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    """ returns page with list of candidates """
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """ returns page of the candidate """
    candidate = utils.get_candidate_by_id(candidate_id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    """ returns list or one page of the candidate by search by name """
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/skill/<skill_name>")
def get_candidate_by_skill(skill_name):
    """ returns list or one page of the candidate by search by skill name """
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))


app.run()
