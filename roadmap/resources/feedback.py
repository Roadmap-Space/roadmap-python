from . import model


class Feedback(model.Model):
    def add(self, feedback, cb):
        self.post(
            "/feedback",
            feedback,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def list(self, roadmap_id, archive, cb):
        archive = "/archive" if archive else ""
        self.get(
            "/feedback/list/" + roadmap_id + archive,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def save(self, feedback, cb):
        self.put(
            "/feedback",
            feedback,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def archive(self, id, token, cb):
        self.delete(
            "/feedback/" + self.compress_id(id, token),
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

    def convert(self, idea, cb):
        self.put(
            "/feedback/convert",
            idea,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def attach_to(self, params, cb):
        self.post(
            "/feedback/attach",
            params,
            lambda feedback: cb(None, feedback),
            lambda err: cb(err)
        )

    def unlink(self, parent_id, id, token, cb):
        self.delete(
            "/feedback/" +
            self.compress_id(id, token) + "/unlink/" + parent_id,
            lambda feedback: cb(None, feedback),
            lambda err: cb(err)
        )
