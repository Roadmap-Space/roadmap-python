from . import model


class AppUsers(model.Model):
    events = {
        "submitted": "submitted",
        "followed": "followed",
        "clapped": "clapped",
        "converted": "converted",
        "emailed": "emailed"
    }

    def list(self, roadmap_id, cb):
        self.get(
            "/appusers/list/" + roadmap_id,
            lambda results: cb(None, results),
            lambda err: cb(err)
        )

    def get_by_id(self, id, roadmap_id, cb):
        self.get(
            "/appusers/detail/" + id + "/" + roadmap_id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def update(self, id, email, first, last, company, tags, cb):
        update = {
            "id": id,
            "email": email,
            "first": first,
            "last": last,
            "company": company,
            "tags": tags
        }

        self.put(
            "/appusers/" + id,
            update,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def remove(self, id, cb):
        self.delete(
            "/appusers/" + id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_tags(self, cb):
        self.get(
            "/appusers/tags",
            lambda tags: cb(None, tags),
            lambda err: cb(err)
        )

    def set_tags(self, tags, cb):
        self.put(
            "/appusers/tags",
            tags,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def match_subscribers(self, subscribers, item_id, token, cb):
        if not subscribers:
            cb(None, [])

        def handler(users):
            # extending subscriber with app user data
            i = 0
            while i < len(subscribers):
                idx = -1
                j = 0
                while j < len(users):
                    if subscribers[i].email == users[j].email:
                        subscribers[i].user = users[j]
                        idx = j
                        break
                if idx > -1:
                    users.splice(idx, 1)

            cb(None, subscribers)

        self.get(
            "/appusers/matchsubscribers/" + self.compress_id(item_id, token),
            lambda users: handler(users),
            lambda err: cb(err)
        )

    def send_mail(self, data, cb):
        self.post(
            "/appusers/message",
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def find_id_by_email(self, email, roadmap_id, cb):
        data = {
            "email": email,
            "roadmapId": roadmap_id,
            "forceCreate": True
        }

        self.post(
            "/appusers/findbyemail",
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def search_by_email(self, query, cb):
        self.post(
            "/appusers/searchbyemail",
            {"query": query},
            lambda results: cb(None, results),
            lambda err: cb(err)
        )
