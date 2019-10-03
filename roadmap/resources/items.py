from . import model


class Items(model.Model):
    itemTypes = {
        "idea": 0,
        "story": 1,
        "done": 2,
        "attached": 3
    }
    columnIndexes = {
        "current": 2,
        "soon": 1,
        "future": 0,
        "team": 2,
        "user": 1,
        "widget": 0,
        "completed": 99
    }
    commentTypes = {
        "system": 0,
        "message": 1,
        "like": 2,
        "email": 3
    }

    def is_feedback(self, item):
        return \
            (item.type == self.itemTypes['idea']
             and item.column == self.columnIndexes['user']) or \
            (item.type == self.itemTypes['attached']
             and item.column == self.columnIndexes['user'])

    def is_idea(self, item):
        return \
            (item.type == self.itemTypes["idea"] and
             (item.column == self.columnIndexes["widget"] or
              item.column == self.columnIndexes["team"])) or \
            (item.type == self.itemTypes["attached"] and
                (item.column == self.columnIndexes["widget"] or
                 item.column == self.columnIndexes["team"]))

    def is_story(self, item):
        return item.type == self.itemTypes["story"]

    def get_new_id(self, cb):
        self.get(
            "/items/newid",
            lambda id: cb(None, id),
            lambda err: cb(err)
        )

    def get_by_id(self, id, cb):
        if not id or id.find("|") == -1:
            cb("invalid parameter")
            return

        parts = id.split("|")
        if parts.length != 2:
            cb("invalid format")
            return

        self.get(
            "/item/" + self.compress_id(parts[0], parts[1]),
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_by_type(self, roadmap_id, is_story, cb):
        type = "story" if is_story else "idea"

        self.get(
            "/items/" + roadmap_id + "/" + type,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def add_comment(self, comment, cb):
        self.post(
            "/items/comment",
            comment,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def update_comment(self, roadmap_id, item_id, comment_id, body, cb):
        self.put(
            "/items/comment",
            {
                "roadmapId": roadmap_id,
                "itemId": item_id,
                "commentId": comment_id,
                "body": body
            },
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def delete_comment(self, id, token, comment_id, cb):
        self.delete(
            "/items/" + self.compress_id(id, token) + "/comment/" + comment_id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def move_to_roadmap(self, id, token, roadmap_id, cb):
        self.put(
            "/items/" + id + "/roadmap",
            {"itemId": id, "token": token, "toRoadmapId": roadmap_id},
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def force_delete(self, id, token, cb):
        self.delete(
            "/items/force/" + self.compress_id(id, token),
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_engagements(self, params, cb):
        self.post(
            "/items/findengagements",
            params,
            lambda results: cb(None, results),
            lambda err: cb(err)
        )

    def remove_pm_links(self, roadmap_id, item_id, token, cb):
        data = {
            "roadmapId": roadmap_id,
            "itemId": item_id,
            "token": token
        }

        self.post(
            "/items/removepmlinks",
            data,
            lambda item: cb(None, item),
            lambda err: cb(err)
        )

    def get_parent(self, roadmap_id, idea_id, idea_token, cb):
        self.get(
            "/items/" + roadmap_id + "/fromattached/" +
            self.compress_id(idea_id, idea_token),
            lambda result: cb(None, result),
            lambda err: cb(err)
        )
