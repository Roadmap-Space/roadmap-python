from . import model


class Ideas(model.Model):
    list_filters = {
        "none": "",
        "archived": "archive",
        "completed": "completed",
        "all": "all"
    }

    sortOptions = {
        "date": 0,
        "oldest": 1,
        "popular": 2,
        "effort": 3,
        "value": 4,
        "magic": 5,
        "widget": 6,
        "wins": 7,
        "liked": 8
    }

    def add(self, idea, cb, limit_reached):
        def err_handler(err, status_code):
            if status_code is 406:
                limit_reached()
            else:
                cb(err)

        self.post(
            "/ideas",
            idea,
            lambda result: cb(None, result),
            err_handler
        )

    def get_by_id(self, id, cb):
        if not id or id.find("|") == -1:
            cb("invalid parameter")
            return

        parts = id.split("|")
        if len(parts) is not 2:
            cb("invalid format")
            return

        def success_handler(result):
            if result:
                if result.category:
                    result.objectives = result.category.split(",")
                else:
                    result.objectives = []

                if not result.tags:
                    result.tags = []

            cb(None, result)

        self.get(
            "/ideas/" + self.compress_id(parts[0], parts[1]),
            success_handler,
            lambda err: cb(err)
        )

    def list(self, roadmap_id, filter, cb):
        filter_str = "/" + \
            filter if filter is not self.list_filters['none'] else ""

        self.get(
            "/ideas/list/" + roadmap_id + filter_str,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def to_widget(self, id, roadmap_id, cb):
        self.post(
            "/ideas/move/widget",
            {"id": id, "roadmapId": roadmap_id},
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def to_idea(self, id, roadmap_id, cb):
        self.post(
            "/ideas/move/idea",
            {"id": id, "roadmapId": roadmap_id},
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def save(self, idea, cb):
        self.put(
            "/ideas",
            idea,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def like(self, id, token, cb):
        self.put(
            "/ideas/like/" + self.compress_id(id, token),
            None,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def archive(self, id, token, cb):
        self.delete(
            "/ideas/" + self.compress_id(id, token),
            None,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def un_archive(self, id, token, cb):
        self.post(
            "/ideas/move/active",
            {"id": id, "token": token},
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def set_as_completed(self, id, token, completed, cb):
        self.put(
            "/ideas/setcompleted/" + self.compress_id(id, token),
            {"completed": completed},
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def push_to_pm(self, id, token, party, cb):
        trello = party == "trello"
        gh = party == "github"
        jira = party == "jira"

        data = {
            "id": id,
            "token": token,
            "trello": trello,
            "gh": gh,
            "jira": jira
        }

        self.post(
            "/ideas/push",
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def convert(self, idea, cb):
        self.put(
            "/ideas/convert",
            idea,
            lambda ok: cb(None, ok),
            lambda err: cb(err)
        )
