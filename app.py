from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        'name': 'Henrique',
        'skills': ['Python', 'NodeJS'],
    },
    {
        'name': 'Paraguassu',
        'skills': ['Typescript', 'Flutter'],
    },
]


@app.get('/devs')
def get_devs():
    return jsonify(devs)


@app.get('/devs/<int:id>')
def get_dev(id):
    try:
        return jsonify(devs[id]), 200
    except IndexError:
        return jsonify({"msg": "dev not found"}), 404


@app.post('/devs')
def create_dev():
    body = request.get_json()
    try:
        if isinstance(body["skills"], list):
            skills = [skill for skill in body["skills"]]
        else:
            skills = [body["skills"]]

        new_dev = {
            "name": body["name"],
            "skills": skills
        }
        devs.append(new_dev)
        return jsonify(new_dev), 200
    except KeyError or IndexError:
        return jsonify({"msg": "malformed body"}), 400


@app.put('/devs/<int:id>')
def update_dev(id):
    body = request.get_json()
    try:
        if isinstance(body["skills"], list):
            skills = [skill for skill in body["skills"]]
        else:
            skills = [body["skills"]]

        update_dev = {
            "name": body["name"],
            "skills": skills
        }
        devs[id] = update_dev
        return jsonify(update_dev), 200
    except KeyError:
        return jsonify({"msg": "malformed body"}), 400
    except IndexError:
        return jsonify({"msg": "dev no found"}), 404


@app.delete('/devs/<int:id>')
def delete_dev(id):
    try:
        devs.remove(devs[id])
        return jsonify({}), 204
    except IndexError:
        return jsonify({"msg": "dev not found"})


if __name__ == '__main__':
    app.run(debug=True)
