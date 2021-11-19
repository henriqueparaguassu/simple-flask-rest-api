# Simple flask API

a simple api used for test the knowledge with flask
that api use an array of devs and their skills
the 4 most used http methods are implemented

to run this code:

```bash
$ pip install -r requirements.txt
$ python3 app.py
```

then access your http://localhost:5000/devs
the list of routes maybe viewed on routes.txt

# Routes

### [GET]

> **route**: "/devs"  
> **action**: return all devs  
> **require**: nothing

> **route**: "/devs/id"  
> **action**: return the dev with respective id  
> **require**: replace "_id_" by the _id_ of the dev you want to return

### [POST]

> **route**: "/devs"  
> **action**: create a dev  
> **require**: a body like:

1. this:

```json
{
  "name": "Henrique Paraguassu",
  "skills": [
    "Python",
    "Flask"
  ]
}
```

2. or this:

```json
{
  "name": "Dev With Single Skill",
  "skills": "Pascal"
}
```

### [PUT]

> **route**: "/devs/id"  
> **action**: update an existent dev  
> **require**: a body like:

1. this:

```json
{
  "name": "Henrique Paraguassu",
  "skills": [
    "Python",
    "Flask"
  ]
}
```

2. or this:

```json
{
  "name": "Dev With Single Skill",
  "skills": "Pascal"
}
```

### [DELETE]

> **route**: "/devs/id"  
> **action**: delete an existent dev  
> **require**: replace "_id_" by the _id_ of the dev you want to delete
