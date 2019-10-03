from . import model


class Stories(model.Model):
    def add(self, story, cb):
        self.post(
            "/stories",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def list(self, id, cb):
        self.get(
            "/stories/" + id,
            lambda results: cb(None, results),
            lambda err: cb(err)
        )

    def done(self, id, cb):
        self.get(
            "/stories/" + id + "/done",
            lambda results: cb(None, results),
            lambda err: cb(err)
        )

    def save(self, story, cb):
        self.put(
            "/stories",
            story,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def add_idea(self, id, token, idea, cb):
        self.post(
            "/stories/" + self.compress_id(id, token) + "/ideas",
            idea,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def attach_idea(self, data, cb, limit_reached):
        def err_handler(err, status_code):
            if status_code is 406:
                limit_reached()
            else:
                cb(err)

        self.post(
            "/stories/ideas",
            data,
            lambda result: cb(None, result),
            err_handler
        )

    def exchange(self, roadmap_id, idea_id, cb):
        self.get(
            "/stories/exchange/" + roadmap_id + "/" + idea_id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def to_backlog(self, roadmap_id, story_id, idea_id, idea_token, cb):
        self.put(
            "/stories/ideas/tobacklog",
            {
                "roadmapId": roadmap_id,
                "storyId": story_id,
                "ideaId": idea_id,
                "ideaToken": idea_token
            },
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def set_feature(self, id, token, mockup_id, cb):
        self.put(
            "/stories/mockups/feature",
            {
                "storyId": id,
                "token": token,
                "mockupId": mockup_id
            },
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def re_order(self, roadmap_id, items, cb):
        self.put(
            "/stories/reorder",
            items,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def set_as_completed(self, id, token, completed, cb):
        self.put(
            "/stories/setcompleted/" + self.compress_id(id, token),
            {
                "completed": completed
            },
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def remove(self, id, token, cb):
        self.delete(
            "/stories/" + self.compress_id(id, token),
            lambda result: cb(None, result),
            lambda err: cb(err)
        )
